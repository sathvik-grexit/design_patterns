from typing import List, Dict
from abc import ABC, abstractmethod
from src.animals import Animal


class Habitat(ABC):

    animals: Dict[str, List[Animal]] = dict()

    @abstractmethod
    def add_animal(self, animal: Animal) -> None:
        pass
    
    @abstractmethod
    def interact_with_animal(self, animal: Animal) -> None:
        pass

    def get_all_animals(self) -> Dict[str, List[Animal]]:
        return self.animals

    def get_all_animals_of_type(self, animal_type: str) -> List[Animal]:
        return self.animals[animal_type]

    def get_animal_by_type_and_name(self, animal_type: str, name: str) -> Animal | str:
        animals_of_type = self.animals[animal_type]
        for animal in animals_of_type:
            if animal.name == name:
                return animal
        return "Animal Not Found"