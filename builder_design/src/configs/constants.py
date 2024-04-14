from enum import Enum

class PizzaSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class PizzaCrust(Enum):
    HAND_TOSSED = "hand_tossed"
    THIN_CRUST = "thin_crust"
    CHEESE_BURST = "cheese_burst"
    FRESH_PAN = "fresh_pan"

class BurgerPatty(Enum):
    VEG = "veg"
    CHICKEN = "chicken"
    MUTTON = "mutton"
    BEEF = "beef"
    PORK = "pork"

class BurgerSauce(Enum):
    MUSTARD = "mustard"
    MAYONNAISE = "mayonnaise"
    KETCHUP = "ketchup"
    MAC_SAUCE = "mac_sauce"