from src.products import Burger
from src.configs import BurgerPatty, BurgerSauce
from src.concrete_builders import BurgerConcreteBuilder

class BurgerDirector:

    def chicken_big_mac(burger_concrete_builder: BurgerConcreteBuilder) -> Burger:
        burger_concrete_builder.reset()
        burger_concrete_builder.patty(BurgerPatty.CHICKEN.value, 2)
        burger_concrete_builder.sauce([BurgerSauce.MAC_SAUCE.value, BurgerSauce.MUSTARD.value, BurgerSauce.MAYONNAISE.value])
        burger_concrete_builder.veggies(["olives", "onions", "tomatoes", "lettuce"])
        burger_concrete_builder.cheese_slices(2)
        return burger_concrete_builder.pack_and_serve()

    def hamburger(burger_concrete_builder: BurgerConcreteBuilder) -> Burger:
        burger_concrete_builder.reset()
        burger_concrete_builder.patty(BurgerPatty.BEEF.value, 1)
        burger_concrete_builder.sauce([BurgerSauce.MUSTARD.value, BurgerSauce.KETCHUP.value])
        burger_concrete_builder.veggies(["pickles", "onions"])
        burger_concrete_builder.cheese_slices(1)
        return burger_concrete_builder.pack_and_serve()