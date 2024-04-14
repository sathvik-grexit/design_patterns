from src.products import Pizza
from src.configs import PizzaSize, PizzaCrust
from src.concrete_builders import PizzaConcreteBuilder

class PizzaDirector:

    def farm_house(pizza_concrete_builder: PizzaConcreteBuilder, size: PizzaSize, crust: PizzaCrust) -> Pizza:
        pizza_concrete_builder.reset()
        pizza_concrete_builder.size(size)
        pizza_concrete_builder.crust(crust)
        pizza_concrete_builder.toppings(["bell-pepper", "olives", "onions", "tomatoes"])
        pizza_concrete_builder.cheese(2)
        return pizza_concrete_builder.pack_and_serve()

    def veg_extravaganza(pizza_concrete_builder: PizzaConcreteBuilder, size: PizzaSize, crust: PizzaCrust) -> Pizza:
        pizza_concrete_builder.reset()
        pizza_concrete_builder.size(size)
        pizza_concrete_builder.crust(crust)
        pizza_concrete_builder.toppings(["bell-pepper", "olives", "onions", "tomatoes", "grilled-mushroom", "corn"])
        pizza_concrete_builder.cheese(2)
        return pizza_concrete_builder.pack_and_serve()