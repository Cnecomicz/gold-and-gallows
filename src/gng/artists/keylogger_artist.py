import gng.global_constants as gc
import gng.functions.text_handling as th

class KeyloggerArtist:
    def __init__(self, keylogger_manager):
        self.keylogger_manager = keylogger_manager
        self.left = 100
        self.top = 200
        self.text_width = 800
        self.font = gc.BASIC_FONT
        self.color = gc.WHITE

    def draw(self, DISPLAY_SURF):
        th.make_hovered_option(
            DISPLAY_SURF, 
            gc.BGCOLOR, 
            self.left, 
            self.top, 
            self.text_width, 
            th.bdlr(self.keylogger_manager.user_string, self.font, self.color)
        )