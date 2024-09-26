import pygame

import gng.global_constants as gc
import gng.functions.text_handling as th

class CharacterSheetArtist:
    def __init__(self, character_sheet_manager, player):
        self.character_sheet_manager = character_sheet_manager
        self.player = player

    def draw(self, DISPLAY_SURF):
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            50,
            50,
            800,
            th.bdlr(f"{self.character_sheet_manager.current_state.name = }")
        )
        list_of_options = []
        for state in self.character_sheet_manager.list_of_submenus:
            list_of_options.append(th.bdlr(f"{state.name}"))
        th.make_all_options(
            DISPLAY_SURF,
            gc.BGCOLOR,
            50, # Fiddle with these constants (left / top / width) later
            100,
            800,
            self.character_sheet_manager.cursor_index,
            *list_of_options
        )