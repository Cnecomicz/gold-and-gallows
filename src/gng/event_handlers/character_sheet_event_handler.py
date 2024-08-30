import pygame

import gng.global_constants as gc
import gng.event_handlers.pygame_event_handler as peh

class CharacterSheetEventHandler(peh.PygameEventHandler):
    def __init__(self, character_sheet_manager):
        self.character_sheet_manager = character_sheet_manager
        super().__init__()
        for up_key in gc.UP:
            self.register_keydown_event_handler(
                up_key, self.handle_keydown_up
            )
        for down_key in gc.DOWN:
            self.register_keydown_event_handler(
                down_key, self.handle_keydown_down
            )
        for left_key in gc.LEFT:
            self.register_keydown_event_handler(
                left_key, self.handle_keydown_left
            )
        for right_key in gc.RIGHT:
            self.register_keydown_event_handler(
                right_key, self.handle_keydown_right
            )
        for use_key in gc.USE:
            self.register_keydown_event_handler(
                use_key, self.handle_keydown_use
            )

    def handle_keydown_up(self, pygame_event):
        if self.character_sheet_manager.current_state in {
            self.character_sheet_manager.co_abilities,
            self.character_sheet_manager.co_class_and_level,
            self.character_sheet_manager.co_equipment,
            self.character_sheet_manager.co_portrait,
            self.character_sheet_manager.co_spells,
            self.character_sheet_manager.co_stats_HP_AC_and_AV
        }:
            self.character_sheet_manager.send("cursor_up")
        elif self.character_sheet_manager.current_state == \
        self.character_sheet_manager.is_equipment:
            self.character_sheet_manager.cursor_index = \
                (self.character_sheet_manager.cursor_index - 1) \
                % self.character_sheet_manager.number_of_options

    def handle_keydown_down(self, pygame_event):
        if self.character_sheet_manager.current_state in {
            self.character_sheet_manager.co_abilities,
            self.character_sheet_manager.co_class_and_level,
            self.character_sheet_manager.co_equipment,
            self.character_sheet_manager.co_portrait,
            self.character_sheet_manager.co_spells,
            self.character_sheet_manager.co_stats_HP_AC_and_AV
        }:
            self.character_sheet_manager.send("cursor_down")
        elif self.character_sheet_manager.current_state == \
        self.character_sheet_manager.is_equipment:
            self.character_sheet_manager.cursor_index = \
                (self.character_sheet_manager.cursor_index + 1) \
                % self.character_sheet_manager.number_of_options

    def handle_keydown_left(self, pygame_event):
        if self.character_sheet_manager.current_state in {
            self.character_sheet_manager.co_abilities,
            self.character_sheet_manager.co_class_and_level,
            self.character_sheet_manager.co_equipment,
            self.character_sheet_manager.co_portrait,
            self.character_sheet_manager.co_spells,
            self.character_sheet_manager.co_stats_HP_AC_and_AV
        }:
            self.character_sheet_manager.send("cursor_left")

    def handle_keydown_right(self, pygame_event):
        if self.character_sheet_manager.current_state in {
            self.character_sheet_manager.co_abilities,
            self.character_sheet_manager.co_class_and_level,
            self.character_sheet_manager.co_equipment,
            self.character_sheet_manager.co_portrait,
            self.character_sheet_manager.co_spells,
            self.character_sheet_manager.co_stats_HP_AC_and_AV
        }:
            self.character_sheet_manager.send("cursor_right")

    def handle_keydown_use(self, pygame_event):
        if self.character_sheet_manager.current_state in {
            self.character_sheet_manager.co_abilities,
            self.character_sheet_manager.co_class_and_level,
            self.character_sheet_manager.co_equipment,
            self.character_sheet_manager.co_portrait,
            self.character_sheet_manager.co_spells,
            self.character_sheet_manager.co_stats_HP_AC_and_AV
        }:
            self.character_sheet_manager.send("into_submenu")