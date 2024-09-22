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
                th.make_all_options(
                    DISPLAY_SURF,
                    gc.BGCOLOR,
                    100,
                    200,
                    800,
                    self.character_creator.cursor_index,
                    th.bdlr(
                        "EXTREME. Your stats will average about 15.5. "
                        "The highest a stat can be is 20 and the lowest "
                        "is 1."
                    ),
                    th.bdlr(
                        "STANDARD. Your stats will average about 13.5. "
                        "The highest a stat can be is 20 and the lowest "
                        "is 2."
                    ),
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
                th.make_all_options(
                    DISPLAY_SURF, 
                    gc.BGCOLOR, 
                    100, 
                    300, 
                    800,
                    self.character_creator.cursor_index,
                    th.bdlr("Cleric"),
                    th.bdlr("Druid"),
                    th.bdlr("Dwarf"),
                    th.bdlr("Elf"),
                    th.bdlr("Fighter"),
                    th.bdlr("Halfling"),
                    th.bdlr("Magic-User"),
                    th.bdlr("Paladin"),
                    th.bdlr("Ranger"),
                    th.bdlr("Warlock")

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