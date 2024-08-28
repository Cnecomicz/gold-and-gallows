# Thanks to https://github.com/meleneth/cnegng/

import pygame


class DuplicateHandlersError(Exception):
    pass


class KeyEventHandler:
    def __init__(self):
        self.key_event_handlers = {}

    def register_key_event(self, key, handler_method):
        if key in self.key_event_handlers:
            raise DuplicateHandlersError(
                f'Duplicate key handler configured for key "{key}"'
            )
        self.key_event_handlers[key] = handler_method

    def __call__(self, pygame_event):
        if (key_event := self.key_event_handlers.get(pygame_event.key)) \
        is not None:
            key_event(pygame_event)

class GamepadEventHandler:
    # TODO much later, for gamepad support. Mirror KeyEventHandler.
    pass


class PygameEventHandler:
    def __init__(self):
        self.event_handlers = {}

    def handle_pygame_events(self, event_list=pygame.event):
        for pygame_event in event_list.get():
            self.handle_pygame_event(pygame_event)

    def handle_pygame_event(self, pygame_event):
        if (event_handler := self.event_handlers.get(pygame_event.type)) \
        is not None:
            event_handler(pygame_event)

    def register_event_handler(self, event_type, handler_method):
        if event_type in self.event_handlers:
            raise DuplicateHandlersError(
                f"Tried to give a second handler for event_type({event_type})"
            )
        self.event_handlers[event_type] = handler_method

    def register_keydown_event_handler(self, key, handler_method):
        self.register_key_event_handler(pygame.KEYDOWN, key, handler_method)

    def register_keyup_event_handler(self, key, handler_method):
        self.register_key_event_handler(pygame.KEYUP, key, handler_method)

    def register_key_event_handler(self, event_type, key, handler_method):
        if event_type not in self.event_handlers:
            self.event_handlers[event_type] = KeyEventHandler()
        # If it blows up here because NoMethodError for 
        # register_key_event, it means something is already configured 
        # to listen to this event_type that isn't using a 
        # KeyEventHandler.
        self.event_handlers[event_type].register_key_event(key, handler_method)