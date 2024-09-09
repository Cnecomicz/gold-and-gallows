import gng.global_constants as gc
import gng.text_handling as th

class DialogueArtist:
    def __init__(self, dialogue_manager):
        self.dialogue_manager = dialogue_manager

    def draw(self, DISPLAY_SURF):
        th.make_text(DISPLAY_SURF, gc.BGCOLOR, 400, 400, 800, self.dialogue_manager.current_dialogue)
        line = 0
        for response in self.dialogue_manager.current_responses_list:
            if response == self.dialogue_manager.hovered_response:
                th.make_hovered_option(
                    DISPLAY_SURF,
                    gc.BGCOLOR,
                    400,
                    500 + line * response.font.get_height(),
                    800,
                    response,
                )
            else:
                th.make_text(
                    DISPLAY_SURF,
                    gc.BGCOLOR,
                    400,
                    500 + line * response.font.get_height(),
                    800,
                    response,
                )
            line += 1
