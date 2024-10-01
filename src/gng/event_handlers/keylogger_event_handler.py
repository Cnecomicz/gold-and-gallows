import pygame

import gng.event_handlers.pygame_event_handler as peh


class KeyloggerEventHandler(peh.PygameEventHandler):
    def __init__(self, keylogger_manager):
        self.keylogger_manager = keylogger_manager
        super().__init__()
        self.register_event_handler(pygame.KEYDOWN, self.log_keys)

    def log_keys(self, pygame_event):
        if (
            pygame_event.key == pygame.K_RETURN
            and self.keylogger_manager.user_string != ""
        ):
            self.keylogger_manager.set_user_string()
        elif (
            pygame_event.key == pygame.K_BACKSPACE
            and self.keylogger_manager.user_string != ""
        ):
            self.keylogger_manager.user_string = self.keylogger_manager.user_string[:-1]
        elif pygame_event.key == pygame.K_ESCAPE:
            pass
        else:
            self.keylogger_manager.user_string += pygame_event.unicode
