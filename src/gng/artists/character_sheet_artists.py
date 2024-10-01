import pygame

import gng.global_constants as gc
import gng.functions.text_handling as th


class CharacterSheetArtist:
    def __init__(self, character_sheet_manager, player):
        self.character_sheet_manager = character_sheet_manager
        self.player = player

    def draw(self, DISPLAY_SURF):
        th.make_text(DISPLAY_SURF, gc.BGCOLOR, 50, 50, 800, th.bdlr("CHARACTER SHEET"))
        list_of_options = []
        for state in self.character_sheet_manager.list_of_submenus:
            list_of_options.append(th.bdlr(f"{state.name}"))
        th.make_all_options(
            DISPLAY_SURF,
            gc.BGCOLOR,
            50,  # Fiddle with these constants (left / top / width) later
            100,
            800,
            self.character_sheet_manager.cursor_index,
            *list_of_options,
        )


class CharacterSheetArtistEquipment:
    def __init__(self, character_sheet_manager, player):
        self.character_sheet_manager = character_sheet_manager
        self.player = player

    def draw(self, DISPLAY_SURF):
        th.make_text(DISPLAY_SURF, gc.BGCOLOR, 50, 50, 800, th.bdlr("EQUIPMENT"))
        list_of_items = []
        for item in self.player.inventory:
            list_of_items.append(th.bdlr(item.name))
        list_of_items.append(th.bdlr("Back"))
        th.make_all_options(
            DISPLAY_SURF,
            gc.BGCOLOR,
            50,  # Fiddle with these constants (left / top / width) later
            100,
            800,
            self.character_sheet_manager.cursor_index,
            *list_of_items,
        )


class CharacterSheetArtistSpells:
    def __init__(self, character_sheet_manager, player):
        self.character_sheet_manager = character_sheet_manager
        self.player = player

    def draw(self, DISPLAY_SURF):
        th.make_text(DISPLAY_SURF, gc.BGCOLOR, 50, 50, 800, th.bdlr("SPELLS"))
        list_of_spells = []
        for spell in self.player.spells:
            list_of_spells.append(th.bdlr(spell.name))
        list_of_spells.append(th.bdlr("Back"))
        th.make_all_options(
            DISPLAY_SURF,
            gc.BGCOLOR,
            50,  # Fiddle with these constants (left / top / width) later
            100,
            800,
            self.character_sheet_manager.cursor_index,
            *list_of_spells,
        )


class CharacterSheetArtistAbilities:
    pass


class CharacterSheetArtistPortrait:
    pass


class CharacterSheetArtistClassAndLevel:
    pass


class CharacterSheetArtistStatsHPACAndAV:
    pass


class CharacterSheetArtistLog:
    pass


class CharacterSheetArtistQuit:
    def __init__(self, character_sheet_manager):
        self.character_sheet_manager = character_sheet_manager

    def draw(self, DISPLAY_SURF):
        th.make_text(DISPLAY_SURF, gc.BGCOLOR, 50, 50, 800, th.bdlr("QUIT"))
        th.make_text(
            DISPLAY_SURF, gc.BGCOLOR, 50, 75, 800, th.bdlr("Do you want to quit?")
        )
        th.make_all_options(
            DISPLAY_SURF,
            gc.BGCOLOR,
            50,  # Fiddle with these constants (left / top / width) later
            100,
            800,
            self.character_sheet_manager.cursor_index,
            th.bdlr("Yes"),
            th.bdlr("No"),
        )
