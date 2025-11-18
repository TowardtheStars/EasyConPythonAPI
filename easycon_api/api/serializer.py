
from data import Controller
import struct

PRO_CONTROLLER_REPORT_LENGTH = 7

class SerialCommandBuilder():
    def build(self, controller:Controller) -> bytes:
        return bytes(PRO_CONTROLLER_REPORT_LENGTH)
    
    def default(self) -> bytes:
        return self.build(Controller())
    
    pass
        
class EasyConSerialBuilder(SerialCommandBuilder):
    def __init__(self):
        pass

    def build(self, controller:Controller) -> bytes:
        """ Build EasyCon command
        Ref: https://github.com/EasyConNS/EasyCon/blob/b567591f1edcde110fbaafb045ab36cc63d420ce/EC.Device/V1/SwitchReport.cs#L27
        """
        serialized = bytes()
        serialized += struct.pack('>H', controller.buttons)
        serialized += struct.pack('B', controller.dpad)
        serialized += struct.pack('BB', controller.lx, controller.ly)
        serialized += struct.pack('BB', controller.rx, controller.ry)
        
        packet = bytes()
        n = 0
        bits = 0
        for b in serialized:
            n = ((n << 8) | b) & 0xffffffffffffffff # unsigned long
            bits += 8
            while bits >= 7:
                bits -= 7
                packet += struct.pack('B', (n >> bits) & 0xff)
                n &= (1 << bits) - 1
        packet = bytearray(packet)
        packet [-1] |= 0x80
        return bytes(packet)
            
        
        
        

