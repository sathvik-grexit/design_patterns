from src.habitats import Habitat
from src.animals import Animal

class Zoo(Habitat):
    
    def add_animal(self, animal: Animal) -> None:
        if animal.animal_type in self.animals:
            self.animals[animal.animal_type].append(animal)
        else:
            self.animals[animal.animal_type] = [animal]
    
    def interact_with_animal(self, animal: Animal) -> None:
        animal.get_animal_info()
        animal.eat()
        animal.poop()
        animal.sleep()
        animal.roam()