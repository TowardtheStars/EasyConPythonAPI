from dataclasses import dataclass, field
from enum import IntEnum

class Buttons(IntEnum):
    Y = 0x01
    B = 0x02
    A = 0x04
    X = 0x08
    L = 0x10
    R = 0x20
    ZL = 0x40
    ZR = 0x80
    MINUS = 0x100
    PLUS = 0x200
    LCLICK = 0x400
    RCLICK = 0x800
    HOME = 0x1000
    CAPTURE = 0x2000

class DPad(IntEnum):
    TOP         = 0x00
    TOP_RIGHT   = 0X01
    RIGHT = 0x02
    BOTTOM_RIGHT = 0x03
    BOTTOM = 0x04
    BOTTOM_LEFT = 0x05
    LEFT = 0x06
    TOP_LEFT = 0x07
    CENTER = 0x08


def get_enum_name_by_value(enum_class, value):
    enum_members = enum_class.__members__
    for enum_constant_name, enum_constant in enum_members.items():
        if enum_constant.value == value:
            return enum_constant_name


@dataclass
class Controller:
    buttons: int = 0x0000
    dpad: int = DPad.CENTER
    lx: int = 0x80
    ly: int = 0x80
    rx: int = 0x80
    ry: int = 0x80
