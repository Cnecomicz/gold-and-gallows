import pygame

import gng.global_constants as gc
import gng.event_handlers.pygame_event_handler as peh

class DialogueEventHandler(peh.PygameEventHandler):
    def __init__(self, dialogue_manager, clock_manager):
        self.dialogue_manager = dialogue_manager
        self.clock_manager = clock_manager
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
        self.dialogue_manager.cursor_index = \
            (self.dialogue_manager.cursor_index - 1) \
            % self.dialogue_manager.number_of_responses
        self.dialogue_manager.hovered_response = \
            self.dialogue_manager.current_responses_list[
                self.dialogue_manager.cursor_index
            ]

    def handle_keydown_down(self, pygame_event):
        self.dialogue_manager.cursor_index = \
            (self.dialogue_manager.cursor_index + 1) \
            % self.dialogue_manager.number_of_responses
        self.dialogue_manager.hovered_response = \
            self.dialogue_manager.current_responses_list[
                self.dialogue_manager.cursor_index
            ]

    def handle_keydown_use(self, pygame_event):
        self.dialogue_manager.chosen_response = \
            self.dialogue_manager.current_responses_list[
                self.dialogue_manager.cursor_index
            ]
        self.dialogue_manager.conversation_partner.dt.send(
            self.dialogue_manager.current_responses_dict[
                self.dialogue_manager.chosen_response
            ]
        )
        self.clock_manager.add_seconds(6)
        self.dialogue_manager.refresh_dialogue()