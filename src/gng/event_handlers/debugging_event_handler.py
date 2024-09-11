import pygame

import gng.global_constants as gc
import gng.event_handlers.pygame_event_handler as peh

class DebuggingEventHandler(peh.PygameEventHandler):
    def __init__(self, debugging_manager):
        self.debugging_manager = debugging_manager
        super().__init__()
        for debug_key in gc.DEBUG:
            self.register_keydown_event_handler(
                debug_key, self.handle_keydown_debug
            )

    def handle_keydown_debug(self, pygame_event):
        self.debugging_manager.flip_debugging_flag()