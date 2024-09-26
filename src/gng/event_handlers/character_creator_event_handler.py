import pygame

import gng.global_constants as gc
import gng.event_handlers.pygame_event_handler as peh

class YouShouldNotBeHere(Exception):
    pass

class CharacterCreatorEventHandler(peh.PygameEventHandler):
    def __init__(self, character_creator):
        self.character_creator = character_creator
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

    def handle_keydown_up(self, pygame_event):
        self.character_creator.cursor_index = \
            (self.character_creator.cursor_index - 1) \
            % self.character_creator.number_of_options

    def handle_keydown_down(self, pygame_event):
        self.character_creator.cursor_index = \
            (self.character_creator.cursor_index + 1) \
            % self.character_creator.number_of_options

    def handle_keydown_use(self, pygame_event):
        match self.character_creator.current_state:
            case self.character_creator.choosing_power_level:
                self.character_creator.choose_power_level()
            case self.character_creator.choosing_class:
                self.character_creator.choose_class()
            case self.character_creator.choosing_name:
                raise YouShouldNotBeHere(
                    "This handler should not be active at this time."
                )