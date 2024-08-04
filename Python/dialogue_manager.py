import global_constants as gc

class DialogueManager:
	def __init__(self):
		self.conversation_partner = None
		self.current_dialogue     = ""
		self.current_responses    = {} # Text : Transition
		self.number_of_responses  = 0
		self.hovered_index        = 0
		self.hovered_response     = ""

	def initialize_conversation_partner(self, conversation_partner):
		self.conversation_partner = conversation_partner
		self.current_dialogue = self.conversation_partner.dt.current_dialogue
		self.current_responses = self.conversation_partner.dt.current_responses
		self.number_of_responses = len(self.current_responses.keys())
		self.hovered_index = 0
		self.hovered_response = \
			list(self.current_responses.keys())[self.hovered_index]

	def handle_pygame_events(self, pygame_event):
		if pygame_event.type == gc.KEYDOWN:
			if pygame_event.key in gc.USE:
				self.conversation_partner.dt.send(
					self.current_responses[self.hovered_response]
				)
			if pygame_event.key in gc.UP:
				self.hovered_index = \
					(self.hovered_index - 1) % self.number_of_responses
			if pygame_event.key in gc.DOWN:
				self.hovered_index = \
					(self.hovered_index + 1) % self.number_of_responses


