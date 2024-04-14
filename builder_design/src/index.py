from src.concrete_builders import PizzaConcreteBuilder, BurgerConcreteBuilder
from src.configs import PizzaSize, PizzaCrust
from src.directors import PizzaDirector, BurgerDirector

pizza_concrete_builder = PizzaConcreteBuilder()
burger_concrete_builder = BurgerConcreteBuilder()

print("------------------------Welcome To------------------------")
print("-----------------------Dominos Pizza-----------------------")

farm_house_pizza = PizzaDirector.farm_house(
    pizza_concrete_builder, 
    PizzaSize.MEDIUM.value,
    PizzaCrust.HAND_TOSSED.value,
)
print(farm_house_pizza.__dict__)

veg_extravaganza_small = PizzaDirector.veg_extravaganza(
    pizza_concrete_builder, 
    PizzaSize.SMALL.value,
    PizzaCrust.CHEESE_BURST.value,
)
print(veg_extravaganza_small.__dict__)

veg_extravaganza_large = PizzaDirector.veg_extravaganza(
    pizza_concrete_builder, 
    PizzaSize.LARGE.value,
    PizzaCrust.THIN_CRUST.value,
)
print(veg_extravaganza_large.__dict__)


print("------------------------Welcome To------------------------")
print("------------------------Mc Donalds-----------------------")

big_mac = BurgerDirector.chicken_big_mac(burger_concrete_builder)
print(big_mac.__dict__)

hamburger = BurgerDirector.hamburger(burger_concrete_builder)
print(hamburger.__dict__)