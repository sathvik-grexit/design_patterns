from abc import ABC

class Volt(ABC):

    def __init__(self) -> None:
        self.volts: int
    
    def set_volts(self, volts: int) -> None:
        self.volts = volts
    
    def get_volts(self) -> int:
        return self.volts