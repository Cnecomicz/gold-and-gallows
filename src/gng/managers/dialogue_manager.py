import gng.global_constants as gc
import gng.text_handling as th


class DialogueManager:
    def __init__(self):
        self.leave_dialogue()

    def enter_dialogue_with(self, conversation_partner):
        self.conversation_partner = conversation_partner
        self.refresh_dialogue()

    def refresh_dialogue(self):
        if self.conversation_partner is not None:
            self.current_dialogue = self.conversation_partner.dt.current_dialogue
            self.current_responses_dict = self.conversation_partner.dt.current_responses
            self.current_responses_list = list(self.current_responses_dict.keys())
            self.number_of_responses = len(self.current_responses_list)
            self.hovered_index = 0
            self.hovered_response = self.current_responses_list[self.hovered_index]

    def leave_dialogue(self):
        self.conversation_partner = None
        self.current_dialogue = th.TextBundle("")
        self.current_responses_dict = {}
        self.current_responses_list = []
        self.number_of_responses = 0
        self.hovered_index = 0
        self.hovered_response = th.TextBundle("")