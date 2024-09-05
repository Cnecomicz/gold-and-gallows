
import gng.global_constants as gc
import gng.text_handling as th

class CharacterCreatorArtist:
    def __init__(
        self,
        character_creator,
        player,
    ):
        self.character_creator = character_creator
        self.player = player

    def draw(self, DISPLAY_SURF):
        match self.character_creator.current_state:
            case self.character_creator.choosing_power_level:
                th.make_text(
                    DISPLAY_SURF,
                    gc.BGCOLOR,
                    100,
                    100,
                    800,
                    th.bdlr("Choose your capability."),
                )
                if self.character_creator.cursor_index == 0:
                    th.make_hovered_option(
                        DISPLAY_SURF,
                        gc.BGCOLOR,
                        100,
                        200,
                        800,
                        th.bdlr(
                            "EXTREME. Your stats will average about 15.5. "
                            "The highest a stat can be is 20 and the lowest "
                            "is 1."
                        ),
                    )
                else:
                    th.make_text(
                        DISPLAY_SURF,
                        gc.BGCOLOR,
                        100,
                        200,
                        800,
                        th.bdlr(
                            "EXTREME. Your stats will average about 15.5. "
                            "The highest a stat can be is 20 and the lowest "
                            "is 1."
                        ),
                    )
                if self.character_creator.cursor_index == 1:
                    th.make_hovered_option(
                        DISPLAY_SURF,
                        gc.BGCOLOR,
                        100,
                        200 + 2 * gc.BASIC_FONT.get_height(),
                        800,
                        th.bdlr(
                            "STANDARD. Your stats will average about 13.5. "
                            "The highest a stat can be is 20 and the lowest "
                            "is 2."
                        ),
                    )
                else:
                    th.make_text(
                        DISPLAY_SURF,
                        gc.BGCOLOR,
                        100,
                        200 + 2 * gc.BASIC_FONT.get_height(),
                        800,
                        th.bdlr(
                            "STANDARD. Your stats will average about 13.5. "
                            "The highest a stat can be is 20 and the lowest "
                            "is 2."
                        ),
                    )
                if self.character_creator.cursor_index == 2:
                    th.make_hovered_option(
                        DISPLAY_SURF,
                        gc.BGCOLOR,
                        100,
                        200 + 4 * gc.BASIC_FONT.get_height(),
                        800,
                        th.bdlr(
                            "CLASSIC. Your stats will average about 10.5. "
                            "The highest a stat can be is 18 and the lowest "
                            "is 3."
                        ),
                    )
                else:
                    th.make_text(
                        DISPLAY_SURF,
                        gc.BGCOLOR,
                        100,
                        200 + 4 * gc.BASIC_FONT.get_height(),
                        800,
                        th.bdlr(
                            "CLASSIC. Your stats will average about 10.5. "
                            "The highest a stat can be is 18 and the lowest "
                            "is 3."
                        ),
                    )
            case self.character_creator.choosing_class:
                th.make_text(
                    DISPLAY_SURF,
                    gc.BGCOLOR,
                    100,
                    100,
                    800,
                    th.bdlr(
                        "Your stats are as follows: \n "
                        f"Charisma: {self.player.CHA} \n "
                        f"Constitution: {self.player.CON} \n "
                        f"Dexterity: {self.player.DEX} \n "
                        f"Intelligence: {self.player.INT} \n "
                        f"Strength: {self.player.STR} \n "
                        f"Wisdom: {self.player.WIS} \n "
                        "What class would you like to be?"
                    ),
                )
                match self.character_creator.cursor_index:
                    case 0:
                        text = (
                            "CLERIC: Lorem ipsum. \n "
                            "Druid. \n "
                            "Dwarf. \n "
                            "Elf. \n "
                            "Fighter. \n "
                            "Halfling. \n "
                            "Magic-User. \n "
                            "Paladin. \n "
                            "Ranger. \n "
                            "Warlock. \n "
                        )
                    case 1:
                        text = (
                            "DRUID: Lorem ipsum. \n "
                            "Dwarf. \n "
                            "Elf. \n "
                            "Fighter. \n "
                            "Halfling. \n "
                            "Magic-User. \n "
                            "Paladin. \n "
                            "Ranger. \n "
                            "Warlock. \n "
                            "Cleric. \n "
                        )
                    case 2:
                        text = (
                            "DWARF: Lorem ipsum. \n "
                            "Elf. \n "
                            "Fighter. \n "
                            "Halfling. \n "
                            "Magic-User. \n "
                            "Paladin. \n "
                            "Ranger. \n "
                            "Warlock. \n "
                            "Cleric. \n "
                            "Druid. \n "
                        )
                    case 3:
                        text = (
                            "ELF: Lorem ipsum. \n "
                            "Fighter. \n "
                            "Halfling. \n "
                            "Magic-User. \n "
                            "Paladin. \n "
                            "Ranger. \n "
                            "Warlock. \n "
                            "Cleric. \n "
                            "Druid. \n "
                            "Dwarf. \n "
                        )
                    case 4:
                        text = (
                            "FIGHTER: Lorem ipsum. \n "
                            "Halfling. \n "
                            "Magic-User. \n "
                            "Paladin. \n "
                            "Ranger. \n "
                            "Warlock. \n "
                            "Cleric. \n "
                            "Druid. \n "
                            "Dwarf. \n "
                            "Elf. \n "
                        )
                    case 5:
                        text = (
                            "HALFLING: Lorem ipsum. \n "
                            "Magic-User. \n "
                            "Paladin. \n "
                            "Ranger. \n "
                            "Warlock. \n "
                            "Cleric. \n "
                            "Druid. \n "
                            "Dwarf. \n "
                            "Elf. \n "
                            "Fighter. \n "
                        )
                    case 6:
                        text = (
                            "MAGIC-USER: Lorem ipsum. \n "
                            "Paladin. \n "
                            "Ranger. \n "
                            "Warlock. \n "
                            "Cleric. \n "
                            "Druid. \n "
                            "Dwarf. \n "
                            "Elf. \n "
                            "Fighter. \n "
                            "Halfling. \n "
                        )
                    case 7:
                        text = (
                            "PALADIN: Lorem ipsum. \n "
                            "Ranger. \n "
                            "Warlock. \n "
                            "Cleric. \n "
                            "Druid. \n "
                            "Dwarf. \n "
                            "Elf. \n "
                            "Fighter. \n "
                            "Halfling. \n "
                            "Magic-User. \n "
                        )
                    case 8:
                        text = (
                            "RANGER: Lorem ipsum. \n "
                            "Warlock. \n "
                            "Cleric. \n "
                            "Druid. \n "
                            "Dwarf. \n "
                            "Elf. \n "
                            "Fighter. \n "
                            "Halfling. \n "
                            "Magic-User. \n "
                            "Paladin. \n "
                        )
                    case 9:
                        text = (
                            "WARLOCK: Lorem ipsum. \n "
                            "Cleric. \n "
                            "Druid. \n "
                            "Dwarf. \n "
                            "Elf. \n "
                            "Fighter. \n "
                            "Halfling. \n "
                            "Magic-User. \n "
                            "Paladin. \n "
                            "Ranger. \n "
                        )
                th.make_hovered_option(
                    DISPLAY_SURF, gc.BGCOLOR, 100, 300, 800, th.bdlr(text)
                )
            case self.character_creator.choosing_name:
                th.make_text(
                    DISPLAY_SURF,
                    gc.BGCOLOR,
                    100,
                    100,
                    800,
                    th.bdlr(
                        f"You are a {self.player.character_class}. \n "
                        "Please type your name."
                    ),
                )
                if not hasattr(self.player, "name"):
                    self.player.name = th.keylogger(
                        DISPLAY_SURF,
                        gc.BGCOLOR,
                        100,
                        200,
                        800,
                        gc.BASIC_FONT,
                        gc.TEXT_COLOR,
                    )
                else:
                    th.make_hovered_option(
                        DISPLAY_SURF,
                        gc.BGCOLOR,
                        100,
                        200,
                        800,
                        th.bdlr(self.player.name),
                    )
