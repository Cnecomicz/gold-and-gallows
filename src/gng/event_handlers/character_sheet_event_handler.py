import pygame

import gng.global_constants as gc
import gng.event_handlers.pygame_event_handler as peh

class CharacterSheetEventHandler(peh.PygameEventHandler):
    def __init__(
        self, 
        character_sheet_manager, 
        gameplay_state_machine_manager
    ):
        self.character_sheet_manager = character_sheet_manager
        self.gameplay_state_machine_manager = gameplay_state_machine_manager
        super().__init__()
        for up_key in gc.UP:
            self.register_keydown_event_handler(
                up_key, self.handle_keydown_up
            )
        for down_key in gc.DOWN:
            self.register_keydown_event_handler(
                down_key, self.handle_keydown_down
            )
        for use_key in gc.USE:
            self.register_keydown_event_handler(
                use_key, self.handle_keydown_use
            )
        for pause_key in gc.PAUSE:
            self.register_keydown_event_handler(
                pause_key, self.handle_keydown_pause
            )

    def handle_keydown_up(self, pygame_event):
        self.character_sheet_manager.cursor_index = \
            (self.character_sheet_manager.cursor_index - 1) \
            % self.character_sheet_manager.number_of_options

    def handle_keydown_down(self, pygame_event):
        self.character_sheet_manager.cursor_index = \
            (self.character_sheet_manager.cursor_index + 1) \
            % self.character_sheet_manager.number_of_options

    def handle_keydown_use(self, pygame_event):
        if self.character_sheet_manager.current_state in {
            self.character_sheet_manager.co_abilities,
            self.character_sheet_manager.co_class_and_level,
            self.character_sheet_manager.co_equipment,
            self.character_sheet_manager.co_portrait,
            self.character_sheet_manager.co_spells,
            self.character_sheet_manager.co_stats_HP_AC_and_AV,
            self.character_sheet_manager.co_quit,
            self.character_sheet_manager.co_log,
        }:
            self.character_sheet_manager.send("into_submenu")

    def handle_keydown_pause(self, pygame_event):
        self.gameplay_state_machine_manager.send("pause")