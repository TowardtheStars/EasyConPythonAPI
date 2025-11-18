


from math import cos, sin, pi
from data import Buttons, Controller, DPad
from functools import singledispatch

class ControllerButtonBuilder:
    
    def __init__(self):
        self._buffer = 0
        self._dpad = DPad.CENTER
        
    def reset(self):
        self._buffer = 0
        return self
    
    def press(self, key):
        if isinstance(key, Buttons):
            self._buffer |= key
        elif isinstance(key, DPad):
            self._dpad = key
        return self
    
    
    def release(self, key:Buttons):
        if (isinstance(key, Buttons)):
            self._buffer &= ~key
        elif isinstance(key, DPad):
            self._dpad = DPad.CENTER
        return self
    
    
    def __ior__(self, other:"ControllerButtonBuilder"):
        self._buffer |= other._buffer
        self._dpad = other._dpad if other._dpad != DPad.CENTER else self._dpad
        return self
    

class ControllerStickBuilder:
    def __init__(self, angle=0, amplifier=0):
        x, y = self._angle2xy(angle, amplifier)
        self._stick_x = x
        self._stick_y = y
        
    def reset(self):
        self._stick_x = 0x80
        self._stick_y = 0x80
        return self
    
        
    def _angle2xy(self, angle, amplifier):
        rad = angle * pi / 180
        x = cos(rad) * amplifier
        y = sin(rad) * amplifier
        x *= 256
        y *= 256
        x += 128
        y += 128
        x = 255 if x > 255 else 0 if x < 0 else x
        y = 255 if y > 255 else 0 if y < 0 else y
        return int(x), int(y)
    
    def stick(self, angle, amplifier=1.0):
        x, y = self._angle2xy(angle, amplifier)
        self._stick_x = x
        self._stick_y = y
        return self
        


class ControllerBuilder:
    def __init__(self,
        button:ControllerButtonBuilder = None, 
        lstick:ControllerStickBuilder = None, 
        rstick:ControllerStickBuilder = None
    ):
        self._button = button or ControllerButtonBuilder()
        self._lstick = lstick or ControllerStickBuilder()
        self._rstick = rstick or ControllerStickBuilder()
        
    def build(self) -> Controller:
        return Controller(
            self._button._buffer,
            self._button._dpad,
            self._lstick._stick_x,
            self._lstick._stick_y,
            self._rstick._stick_x,
            self._rstick._stick_y
        )
        
    
    def button_press(self, key):
        self._button.press(key)
        return self
    
    def button_release(self, key):
        self._button.release(key)
        return self
    
    def button_reset(self):
        self._button.reset()
        return self
    
    def lstick(self, angle, amplifier=1.0):
        self._lstick.stick(angle, amplifier)
        return self
    
    def lstick_reset(self):
        self._lstick.reset()
        return self
    
    def rstick(self, angle, amplifier=1.0):
        self._rstick.stick(angle, amplifier)
        return self
    
    def rstick_reset(self):
        self._rstick.reset()
        return self
    
