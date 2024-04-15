from abc import ABC
from src.volt import Volt

class Socket(ABC):

    def get_volts(self):
        volt: Volt = Volt()
        volt.set_volts(120)
        return volt.get_volts()