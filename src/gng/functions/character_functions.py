import math

def calculate_AV(character_class, level):
    match character_class:
        case "Cleric":
            return round(2 / 5 * (level - 1) + 10 + (4 / 5))
        case "Druid":
            return round(2 / 5 * (level - 1) + 7 + (4 / 5))
        case "Dwarf" | "Paladin" | "Ranger":
            return math.floor(1 / 2 * (level - 1) + 11)
        case "Elf":
            return round(2 / 3 * (level - 1) + 10 + (2 / 3))
        case "Fighter":
            return math.ceil(2 / 3 * (level - 1) + 10 + (2 / 3))
        case "Halfling":
            return math.floor(1 / 4 * (level - 1) + 12)
        case "Magic-User" | "Warlock":
            return math.ceil(1 / 3 * (level - 1) + 7 + (1 / 3))
