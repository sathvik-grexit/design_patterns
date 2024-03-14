from src.configs import Animals, Habitats
from src.animals.animal_factory import AnimalFactory
from src.habitats.habitat_factory import HabitatFactory

avian = Animals.AVIAN.value
terrestrial = Animals.TERRESTRIAL.value
zoo = Habitats.ZOO.value
wildlife_sanctuary = Habitats.WILDLIFE_SANCTUARY.value

print("------------------------Welcome To------------------------")
print("-----------------------Bengaluru Zoo-----------------------")

bengaluru_zoo = HabitatFactory(zoo)
bengaluru_zoo_animals = [
    {"animal_type": avian, "name": "Dodo", "age": 3}, 
    {"animal_type": avian, "name": "Eagly", "age": 8},
    {"animal_type": terrestrial, "name": "Simba", "age": 10}, 
    {"animal_type": terrestrial, "name": "Sherkhan", "age": 12}, 
    {"animal_type": terrestrial, "name": "Pink-Panther", "age": 6},
]

for animal in bengaluru_zoo_animals:
    animal = AnimalFactory(animal["animal_type"], animal["name"], animal["age"])
    bengaluru_zoo.add_animal(animal)


print("All Animals Count", len(bengaluru_zoo.get_all_animals()[avian]) + len(bengaluru_zoo.get_all_animals()[terrestrial]))
print("Avain Animals", bengaluru_zoo.get_all_animals_of_type(avian))
print("Terrestrial Animals", bengaluru_zoo.get_all_animals_of_type(terrestrial))
animal = bengaluru_zoo.get_animal_by_type_and_name(terrestrial, "Pink-Panther")
bengaluru_zoo.interact_with_animal(animal)

print("--------------------------------Welcome To--------------------------------")
print("-----------------------Bengaluru Wildlife Sanctuary-----------------------")

bengaluru_wildlife_sanctuary = HabitatFactory(wildlife_sanctuary)
bengaluru_wildlife_sanctuary_animals = [
    {"animal_type": avian, "name": "Dodo", "age": 3}, 
    {"animal_type": avian, "name": "Eagly", "age": 8},
    {"animal_type": terrestrial, "name": "Simba", "age": 10}, 
    {"animal_type": terrestrial, "name": "Sherkhan", "age": 12}, 
    {"animal_type": terrestrial, "name": "Pink-Panther", "age": 6},
]

for animal in bengaluru_wildlife_sanctuary_animals:
    animal = AnimalFactory(animal["animal_type"], animal["name"], animal["age"])
    bengaluru_wildlife_sanctuary.add_animal(animal)

print("All Animals Count", len(bengaluru_wildlife_sanctuary.get_all_animals()[avian]) + len(bengaluru_wildlife_sanctuary.get_all_animals()[terrestrial]))
print("Avain Animals", bengaluru_wildlife_sanctuary.get_all_animals_of_type(avian))
print("Terrestrial Animals", bengaluru_wildlife_sanctuary.get_all_animals_of_type(terrestrial))
animal = bengaluru_wildlife_sanctuary.get_animal_by_type_and_name(terrestrial, "Pink-Panther")
bengaluru_wildlife_sanctuary.interact_with_animal(animal)