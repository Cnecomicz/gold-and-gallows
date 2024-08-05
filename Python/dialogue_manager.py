import global_constants as gc
import text_handling    as th

class DialogueManager:
	def __init__(self):
		self.conversation_partner = None
		self.current_dialogue     = ""
		self.current_responses    = {} # Text bundle : Transition
		self.number_of_responses  = 0
		self.hovered_index        = 0
		self.hovered_response     = th.TextBundle("")

	def enter_dialogue_with(self, conversation_partner):
		self.conversation_partner = conversation_partner
		self.refresh_dialogue()

	def refresh_dialogue(self):
		self.current_dialogue = self.conversation_partner.dt.current_dialogue
		self.current_responses = self.conversation_partner.dt.current_responses
		self.number_of_responses = len(self.current_responses.keys())
		self.hovered_index = 0
		self.hovered_response = \
			list(self.current_responses.keys())[self.hovered_index]


	def leave_dialogue(self):
		self.conversation_partner = None
		self.current_dialogue     = ""
		self.current_responses    = {} # Text bundle : Transition
		self.number_of_responses  = 0
		self.hovered_index        = 0
		self.hovered_response     = th.TextBundle("")


	def handle_pygame_events(self, pygame_event):
		if pygame_event.type == gc.KEYDOWN:
			if pygame_event.key in gc.USE:
				self.conversation_partner.dt.send(
					self.current_responses[self.hovered_response]
				)
				self.refresh_dialogue()
			if pygame_event.key in gc.UP:
				self.hovered_index = \
					(self.hovered_index - 1) % self.number_of_responses
				self.hovered_response = \
					list(self.current_responses.keys())[self.hovered_index]
			if pygame_event.key in gc.DOWN:
				self.hovered_index = \
					(self.hovered_index + 1) % self.number_of_responses
				self.hovered_response = \
					list(self.current_responses.keys())[self.hovered_index]

	def update(self):
		pass

	def draw(self, DISPLAY_SURF):
		th.make_text(
			DISPLAY_SURF, 
			gc.BGCOLOR, 
			400, 400, 
			800,
			self.current_dialogue
		)


