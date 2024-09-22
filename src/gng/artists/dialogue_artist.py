import gng.global_constants as gc
import gng.text_handling as th

class DialogueArtist:
    def __init__(self, dialogue_manager):
        self.dialogue_manager = dialogue_manager

    def draw(self, DISPLAY_SURF):
        # Draw NPC dialogue:
        th.make_text(
            DISPLAY_SURF, 
            gc.BGCOLOR, 
            400, 
            400, 
            800, 
            self.dialogue_manager.current_dialogue
        )
        # Draw player responses:
        th.make_all_options(
            DISPLAY_SURF, 
            gc.BGCOLOR, 
            400, 
            500, 
            800, 
            self.dialogue_manager.cursor_index, 
            *self.dialogue_manager.current_responses_list
        )
