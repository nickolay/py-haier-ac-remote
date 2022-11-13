from enum import Enum
from dataclasses import dataclass

class Limits(Enum):
    OFF = 0
    ONLY_VERTICAL = 1
    UNKNOWN_3 = 3

class FanSpeed(Enum):
    MAX = 0
    MID = 1
    MIN = 2
    AUTO = 3

class Mode(Enum):
    SMART = 0
    COOL = 1
    HEAT = 2
    FAN = 3
    DRY = 4

@dataclass
class State:
    current_temp: int
    target_temp: int
    fan_speed: FanSpeed
    mode: Mode
    health: bool
    limits: Limits
    power: bool

    def __str__(self) -> str:
        return """Haier AC State:
        Power: {},
        Current Temp: {}
        Target Temp: {}
        Fan Speed: {}
        Mode: {}
        Health: {}
        Limits: {}""".format(
          self.power, self.current_temp, self.target_temp,
          self.fan_speed, self.mode, self.health, self.limits
        )
