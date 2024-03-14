from src.animals.animal import Animal
from src.configs import Animals

class AvianAnimal(Animal):

    animal_type: str = Animals.AVIAN.value

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
    
    def eat(self) -> None:
        print(f"{self.name} eating grains")
    
    def poop(self) -> None:
        print(f"{self.name} poops on people")

    def sleep(self) -> None:
        print(f"{self.name} sleeps on a perch")

    def roam(self) -> None:
        print(f"{self.name} flies with its wings")

    def get_animal_info(self) -> None:
        print(f"I am {self.name}, {self.age} year(s) old and I am an {self.animal_type} animal")