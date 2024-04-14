from abc import ABC
from typing import List
from src.configs import PizzaSize, PizzaCrust

class Pizza(ABC):
    
    crust: PizzaCrust
    size: PizzaSize
    toppings: List[str]
    cheese: str
