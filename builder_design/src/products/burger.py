from abc import ABC
from typing import List
from src.configs import BurgerPatty, BurgerSauce

class Burger(ABC):

    veggies: List[str]
    patty_type: BurgerPatty
    patty_count: int
    cheese_slices: int
    sauce: List[BurgerSauce]
    