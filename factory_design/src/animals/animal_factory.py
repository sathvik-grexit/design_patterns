from src.animals import Animal, AvianAnimal, TerrestrialAnimal
from src.configs import Animals

def AnimalFactory(animal_type: str, name: str, age: str) -> Animal:
    animal = {
        Animals.AVIAN.value: AvianAnimal,
        Animals.TERRESTRIAL.value: TerrestrialAnimal,

    }
    return animal[animal_type](name, age)
