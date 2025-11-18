
from dataclasses import dataclass, field
from enum import Enum
import serial, asyncio, queue
from typing import Callable, Type


from data import Buttons, DPad
from controller_builder import ControllerBuilder, ControllerStickBuilder, ControllerButtonBuilder
from serializer import EasyConSerialBuilder, SerialCommandBuilder

import logging

class CMDType(Enum):
    TIMED = 1
    CONTINUOUS = 2

@dataclass
class RealTimeCommand:
    cmd_type: CMDType
    cmd: bytes = field(default_factory=bytes)
    data:dict = field(default_factory=dict)
    

class RealTimeController:
    
    
    def __init__(self, serial_device:serial.Serial, serializer:Type[SerialCommandBuilder]=EasyConSerialBuilder):
        self._device = serial_device
        if not self._device.closed:
            self._device.close()
        self._cmd_queue:asyncio.Queue = asyncio.Queue()
        self._serializer = serializer()
        self._default_cmd = self._serializer.default()
        self._running = False
        self._console = False
        
        self._logger = logging.StreamHandler()
        self._logger.setLevel(logging.DEBUG)
        
    
    async def _run(self) -> None:
        
        while self._running:
            try:
                if self._cmd_queue.qsize() > 0:
                    state:RealTimeCommand = self._cmd_queue.get_nowait()
                    # print(state)
                    if state.cmd_type == CMDType.TIMED:
                        self._device.write(state.cmd)
                        await asyncio.sleep(state.data['time'] / 1000)
                    elif state.cmd_type == CMDType.CONTINUOUS:
                        self._device.write(state.cmd)
                        self._default_cmd = state.cmd
                    # logging.debug(self._device.read_all())
                    
                    self._device.flush()
                    self._cmd_queue.task_done()
                elif self._console:
                    print('no cmd', ned = '\r')
                    await asyncio.sleep(0.05)
                else:
                    self._running = False
                    await self.stop()
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                logging.error(e, exc_info=True)
                await self.stop()
                break
        
    
    async def start(self, console:bool=False):
        self._device.open()
        while not self._device.is_open:
            await asyncio.wait(0.05)
        self._running = True
        self._console = console
        self.task = asyncio.create_task(self._run())
    
    async def stop(self):
        self._running = False
        if self.task:
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass
        self._device.close()
        del self._cmd_queue
        self._cmd_queue = asyncio.Queue()
        return
    
    def get_command_builder(self):
        return RealTimeCommandBuilder(self)
    
    
class RealTimeCommandBuilder:
    def __init__(self, target:RealTimeController):
        self._state = queue.Queue()
        self._target = target
        self._seriaizer = target._serializer
        
        self._default_button = ControllerButtonBuilder()
        self._default_lstick = ControllerStickBuilder()
        self._default_rstick = ControllerStickBuilder()
    
        
    async def send(self):
        
        while self._state.qsize() > 0:
            await self._target._cmd_queue.put(self._state.get())
        
        
    def command(self, 
                command_builder:Callable[[ControllerBuilder], ControllerBuilder], 
                time:int=-1
                ):
        cmd = self._seriaizer.build(command_builder(ControllerBuilder()).build())
        if time < 0:
            self._state.put(RealTimeCommand(CMDType.CONTINUOUS, cmd, {}))
        else:
            self._state.put(RealTimeCommand(CMDType.TIMED, cmd, {'time':time}))
        return self
        
    def button(self, key, time:int=50):
        """按下并弹起按键

        Args:
            time (int): 按钮按下时间，单位为 ms。默认 50ms
        """
        if time < 0:
            # 创建一个新的按钮命令构建器，按下指定按键
            button_builder = ControllerButtonBuilder().press(key)
            # 将按键状态合并到默认按钮状态中
            self._default_button._buffer |= button_builder._buffer
        else:
            self.command(lambda builder: builder.button_press(key), time)
            # 结束后自动回弹到默认状态
        return self
            
    def lstick(self, angle, time:int=-1, amplifier=1.0):
        """操作左摇杆

        Args:
            angle (float): 摇杆角度，0°角为摇杆正右方
            time (int, optional): 操作时间，单位为 ms. 默认为 -1，aka 一直操作摇杆
            amplifier (float, optional): 摇杆移动幅度，只能在 0~1 之间。默认为 1.0

        Returns:
            _type_: self
        """
        if time < 0:
            self._default_lstick = ControllerStickBuilder(angle, amplifier)
        else:
            self.command(lambda builder: builder.lstick(angle, amplifier), time)
        return self
        
    def rstick(self, angle, time:int=-1, amplifier=1.0):
        """操作右摇杆

        Args:
            angle (float): 摇杆角度，0°角为摇杆正右方
            time (int, optional): 操作时间. 默认为 -1，aka 一直操作摇杆
            amplifier (float, optional): 摇杆移动幅度，只能在 0~1 之间。默认为 1.0

        Returns:
            _type_: self
        """
        if time < 0:
            self._default_rstick = ControllerStickBuilder(angle, amplifier)
        else:
            self.command(lambda builder: builder.rstick(angle, amplifier), time)
        return self
    
    def wait(self, time:int=50):
        """等待

        Args:
            time (int, optional): 等待时间，单位 ms. 默认等待 50 ms.

        Returns:
            _type_: self
        """
        ctrl = ControllerBuilder(self._default_button, self._default_lstick, self._default_rstick).build()
        cmd = self._seriaizer.build(ctrl)
        
        if time > 100:
            for _ in range(time//100):
                self._state.put(RealTimeCommand(CMDType.TIMED, cmd, {'time': 100}))
            if time % 100 > 0:
                self._state.put(RealTimeCommand(CMDType.TIMED, cmd, {'time': time % 100}))
        else:
            self._state.put(RealTimeCommand(CMDType.TIMED, cmd, {'time': time}))
        
        return self
    
    # 基本按键方法
    # 按下对应按键，time为按下时间，单位为ms
    
    def home(self, time:int=50):
        """按下HOME键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.HOME, time)
    
    def a(self, time:int=50):
        """按下A键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.A, time)

    def b(self, time:int=50):
        """按下B键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.B, time)

    def x(self, time:int=50):
        """按下X键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.X, time)

    def y(self, time:int=50):
        """按下Y键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.Y, time)

    # 肩键和扳机键方法
    
    def r(self, time:int=50):
        """按下R键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.R, time)

    def zr(self, time:int=50):
        """按下ZR键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.ZR, time)

    def l(self, time:int=50):
        """按下L键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.L, time)

    def zl(self, time:int=50):
        """按下ZL键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.ZL, time)

    # 控制按键方法
    
    def minus(self, time:int=50):
        """按下MINUS键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.MINUS, time)

    def plus(self, time:int=50):
        """按下PLUS键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.PLUS, time)

    def rpress(self, time:int=50):
        """按下右摇杆键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.RCLICK, time)

    def lpress(self, time:int=50):
        """按下左摇杆键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.LCLICK, time)

    def capture(self, time:int=50):
        """按下CAPTURE键
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(Buttons.CAPTURE, time)

    # 方向键方法
    
    def dpad_up(self, time:int=50):
        """按下方向键上
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(DPad.TOP, time)

    def dpad_down(self, time:int=50):
        """按下方向键下
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(DPad.BOTTOM, time)

    def dpad_left(self, time:int=50):
        """按下方向键左
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(DPad.LEFT, time)

    def dpad_right(self, time:int=50):
        """按下方向键右
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(DPad.RIGHT, time)

    def dpad_upright(self, time:int=50):
        """按下方向键右上
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(DPad.TOP_RIGHT, time)

    def dpad_upleft(self, time:int=50):
        """按下方向键左上
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(DPad.TOP_LEFT, time)

    def dpad_downright(self, time:int=50):
        """按下方向键右下
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(DPad.BOTTOM_RIGHT, time)

    def dpad_downleft(self, time:int=50):
        """按下方向键左下
        
        Args:
            time (int): 按键持续时间，单位为毫秒，默认为50ms
        """
        return self.button(DPad.BOTTOM_LEFT, time)
  

  