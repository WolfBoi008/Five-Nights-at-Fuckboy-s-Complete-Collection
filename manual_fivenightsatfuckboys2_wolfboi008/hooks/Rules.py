from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def recruitedToyBonnie(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Stick| AND |Toy Bonnie|"

def recruitedToyChica(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Progressive Cupcakes:1| AND |Toy Chica|"

def recruitedMangle(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Sex Toy Voucher| AND |Sex Toy| AND |Mangle|"

def partyAllToys(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Stick| AND |Toy Bonnie| AND |Progressive Cupcakes:1| AND |Toy Chica| AND |Sex Toy Voucher| AND |Sex Toy| AND |Mangle|"

def partyAlmostComplete(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Stick| AND |Toy Bonnie| AND |Progressive Cupcakes:1| AND |Toy Chica| AND |Sex Toy Voucher| AND |Sex Toy| AND |Mangle| AND |Withered Freddy| AND |Withered Bonnie| AND |Withered Chica| AND |Withered Foxy|"

def partyComplete(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Stick| AND |Toy Bonnie| AND |Progressive Cupcakes:1| AND |Toy Chica| AND |Sex Toy Voucher| AND |Sex Toy| AND |Mangle| AND |Withered Freddy| AND |Withered Bonnie| AND |Withered Chica| AND |Withered Foxy| AND |Withered Golden Freddy|"

def equipAlpha(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Progressive Microphone:1| AND (|Stick| AND |Toy Bonnie| AND |Progressive Guitar:1|) AND |Progressive Head Endoskeletons:1| AND |Progressive Body Endoskeletons:1| AND |Progressive Pizza Shields:1| AND |Progressive Caffeine Sodas:1|"

def equipBeta(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Progressive Microphone:2| AND (|Stick| AND |Toy Bonnie| AND |Progressive Guitar:2|) AND (|Toy Chica| AND |Progressive Cupcakes:2|) AND |Progressive Head Endoskeletons:2| AND |Progressive Body Endoskeletons:2| AND |Progressive Pizza Shields:2| AND |Progressive Caffeine Sodas:2|"

def equipGamma(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Progressive Microphone:3| AND (|Stick| AND |Toy Bonnie| AND |Progressive Guitar:3|) AND (|Toy Chica| AND |Progressive Cupcakes:3|) AND (|Sex Toy Voucher| AND |Sex Toy| AND |Mangle| AND |Progressive Hook:3|) AND |Progressive Head Endoskeletons:3| AND |Progressive Body Endoskeletons:3| AND |Progressive Pizza Shields:3| AND |Progressive Caffeine Sodas:3|"

def equipOmega(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Progressive Microphone:4| AND (|Stick| AND |Toy Bonnie| AND |Progressive Guitar:4|) AND (|Toy Chica| AND |Progressive Cupcakes:4|) AND (|Sex Toy Voucher| AND |Sex Toy| AND |Mangle| AND |Progressive Hook:4|) AND |Progressive Head Endoskeletons:4| AND |Progressive Body Endoskeletons:4| AND |Progressive Pizza Shields:4| AND |Progressive Caffeine Sodas:4|"

def equipReal(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    return "|Progressive Microphone:5| AND (|Stick| AND |Toy Bonnie| AND |Progressive Guitar:5|) AND (|Toy Chica| AND |Progressive Cupcakes:5|) AND (|Sex Toy Voucher| AND |Sex Toy| AND |Mangle| AND |Progressive Hook:5|) AND |Progressive Head Endoskeletons:5| AND |Progressive Body Endoskeletons:5| AND |Progressive Pizza Shields:4| AND |Progressive Caffeine Sodas:4|"