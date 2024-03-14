from src.animals.animal import Animal
from src.configs import Animals


class TerrestrialAnimal(Animal):
    
    animal_type: str = Animals.TERRESTRIAL.value

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def eat(self) -> None:
        print(f"{self.name} eating meat")
    
    def poop(self) -> None:
        print(f"{self.name} poop stinks!!!")

    def sleep(self) -> None:
        print(f"{self.name} sleeps like a cat")
    
    def roam(self) -> None:
        print(f"{self.name} walks like a cat")

    def get_animal_info(self) -> None:
        print(f"I am {self.name}, {self.age} year(s) old and I am a {self.animal_type} animal")