from src.habitats import Habitat, Zoo, WildlifeSanctuary
from src.configs import Habitats

def HabitatFactory(habitat_type: str) -> Habitat:
    habitat = {
        Habitats.ZOO.value: Zoo,
        Habitats.WILDLIFE_SANCTUARY.value: WildlifeSanctuary,
    }
    return habitat[habitat_type]()