from typing import List
from src.products import Burger
from src.builders import BurgerBuilder
from src.configs import BurgerSauce, BurgerPatty

class BurgerConcreteBuilder(BurgerBuilder):

    def reset(self) -> None:
        self._burger = Burger()
    
    def patty(self, patty_type: BurgerPatty, patty_count: int) -> None:
        self._burger.patty_type = patty_type
        self._burger.patty_count = patty_count
    
    def cheese_slices(self, slices: int) -> None:
        self._burger.cheese_slices = slices
    
    def veggies(self, veggies: List[str]) -> None:
        self._burger.veggies = veggies
    
    def sauce(self, sauce: List[BurgerSauce]) -> None:
        self._burger.sauce = sauce
    
    def pack_and_serve(self) -> Burger:
        return self._burger
        