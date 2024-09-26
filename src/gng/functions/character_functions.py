import math

class InvalidClass(Exception):
    pass

def calculate_AV(character_class, level):
    match character_class:
        case "Cleric":
            slope = 0.4
            yint = 10.8
        case "Druid":
            slope = 0.4
            yint = 7.8
        case "Dwarf" | "Paladin" | "Ranger":
            slope = 0.5
            yint = 10.5
        case "Elf":
            slope = 0.66
            yint = 10.66
        case "Fighter":
            slope = 0.66
            yint = 11
        case "Halfling":
            slope = 0.25
            yint = 11.75
        case "Magic-User" | "Warlock":
            slope = 0.33
            yint = 8
        case _:
            raise InvalidClass(
                "The inputted character class does not exist. Check if typo."
            )
    return math.floor(slope*level + yint)
