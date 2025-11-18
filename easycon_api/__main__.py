
import asyncio
from re import L
import time
from api.control import RealTimeController
from api.serializer import EasyConSerialBuilder
from serial import Serial

import logging, sys

async def main(test):
    device = Serial('COM12', 115200,)
    device.read_all()
    # device.write(bytes([0xa5, 0xa5, 0x81]))
    # time.sleep(1)
    # print(device.read_all())
    
    
    controller = RealTimeController(device, EasyConSerialBuilder)
    
    commands = controller.get_command_builder()
    commands.lpress().wait(200)
    if test == 1:
        commands.x(200).wait(200)
        for _ in range(3):
            commands.b(200).wait(200)
        commands.x(200).wait(200)
    elif test == 2:
        commands.lstick(0, 2000).wait(200)
        
        for angle in range(0, 360, 1):
            commands.lstick(angle, 8)
        commands.wait(200)
        
    elif test == 3:
        for _ in range(3):
            commands.dpad_right().wait(200)
        
    elif test == -1:
        commands.b().wait().b().wait().b().wait().b().wait().b().wait().b().wait()
    
    
    
    await commands.send()
    await controller.start()
    await controller.task

if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    logging.info('start')
    asyncio.run(main(3))