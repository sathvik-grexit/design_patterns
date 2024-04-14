from typing import List
from src.products import Pizza
from src.builders import PizzaBuilder
from src.configs import PizzaCrust, PizzaSize

class PizzaConcreteBuilder(PizzaBuilder):

    def reset(self) -> None:
        self._pizza = Pizza()

    def crust(self, crust: PizzaCrust) -> None:
        self._pizza.crust = crust
    
    def size(self, size: PizzaSize) -> None:
        self._pizza.size = size
    
    def cheese(self, cheese: int) -> None:
        self._pizza.cheese = cheese
    
    def toppings(self, toppings: List) -> None:
        self._pizza.toppings = toppings
    
    def pack_and_serve(self) -> Pizza:
        return self._pizza
        