from abc import ABC, abstractmethod

class Adapter(ABC):

    @abstractmethod
    def get_3_volts(self) -> int:
        pass

    @abstractmethod
    def get_12_volts(self) -> int:
        pass

    @abstractmethod
    def get_120_volts(self) -> int:
        pass