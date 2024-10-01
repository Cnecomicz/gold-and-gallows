import gng.global_constants as gc
import gng.functions.text_handling as th


class DebuggingArtist:
    def __init__(self, debugging_manager, clock_manager):
        self.debugging_manager = debugging_manager
        self.clock_manager = clock_manager

    def draw(self, DISPLAY_SURF):
        if self.debugging_manager.debugging_flag:
            th.make_text(
                DISPLAY_SURF,
                gc.BGCOLOR,
                10,
                10,
                gc.WINDOW_WIDTH - 20,
                th.bdlr(text="Debug menu: (toggle with `) \n"),
                th.bdlr(
                    text=self.clock_manager.get_datetime_string() + " \n",
                    color=gc.GREEN,
                ),
                th.bdlr(
                    text=self.debugging_manager.debugging_text,
                    color=gc.BLUE,
                ),
            )
