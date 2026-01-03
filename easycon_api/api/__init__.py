from easycon_api.api.controller_builder import ControllerBuilder
from easycon_api.api.data import Buttons, DPad
from easycon_api.api.control import RealTimeController, RealTimeCommandBuilder
import serial

__all__ = [
    "ControllerBuilder",
    "Buttons",
    "DPad",
    "RealTimeCommandBuilder",
    "RealTimeController"
]


class EasyconController:
    
    def __init__(self, device:serial.Serial):
        self.device = device
        
        
    def open(self):
        if self.device.is_open:
            return
        self.device.open()


    def close(self):
        if self.device.is_open:
            self.device.close()
            
    def 
