from abc import abstractmethod
from typing import List
from src.products import Burger
from src.configs import BurgerPatty, BurgerSauce

class BurgerBuilder(Burger):

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def patty(self, patty_type: BurgerPatty, patty_count: int) -> None:
        pass

    @abstractmethod
    def cheese_slices(self, slices: int) -> None:
        pass

    @abstractmethod
    def sauce(self, sauce: List[BurgerSauce]) -> None:
        pass

    @abstractmethod
    def veggies(self, veggies: List[str]) -> None:
        pass

    @abstractmethod
    def pack_and_serve(self) -> Burger:
        pass