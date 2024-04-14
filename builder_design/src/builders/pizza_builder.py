from abc import abstractmethod
from typing import List
from src.products import Pizza
from src.configs import PizzaCrust, PizzaSize

class PizzaBuilder(Pizza):

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def crust(self, crust: PizzaCrust) -> None:
        pass

    @abstractmethod
    def size(self, size: PizzaSize) -> None:
        pass

    @abstractmethod
    def cheese(self, cheese: int) -> None:
        pass

    @abstractmethod
    def toppings(self, toppings: List[str]) -> None:
        pass

    @abstractmethod
    def pack_and_serve(self) -> Pizza:
        pass