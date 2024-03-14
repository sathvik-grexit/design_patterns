from abc import ABC, abstractmethod

class Animal(ABC):

    animal_type: str = "animal"

    @abstractmethod
    def eat(self) -> None:
        pass

    @abstractmethod
    def poop(self) -> None:
        pass

    @abstractmethod
    def sleep(self) -> None:
        pass

    @abstractmethod
    def roam(self) -> None:
        pass

    @abstractmethod
    def get_animal_info(self) -> None:
        pass