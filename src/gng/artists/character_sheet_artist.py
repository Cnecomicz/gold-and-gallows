import pygame

import gng.global_constants as gc
import gng.text_handling as th

import gng.managers.character_statistics as cs

class CharacterSheetArtist:
    def __init__(self, character_sheet_manager, player):
        self.character_sheet_manager = character_sheet_manager
        self.player = player

    def draw(self, DISPLAY_SURF):
        text = f"{self.character_sheet_manager.current_state.name = } \n {self.character_sheet_manager.cursor_index = } \n "
        for state in self.character_sheet_manager.list_of_submenus:
            text += f"{state.name} \n "
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            10, # Fiddle with these constants (left / top / width) later
            10,
            800,
            th.bdlr(text),
        )