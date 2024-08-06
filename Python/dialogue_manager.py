import global_constants as gc
import text_handling    as th

class DialogueManager:
	def __init__(self):
		self.leave_dialogue()
		self.spoken_queue = []

	def enter_dialogue_with(self, conversation_partner):
		self.conversation_partner = conversation_partner
		self.refresh_dialogue()

	def refresh_dialogue(self):
		self.current_dialogue = self.conversation_partner.dt.current_dialogue
		self.current_responses_dict = \
			self.conversation_partner.dt.current_responses
		self.current_responses_list = \
			list(self.current_responses_dict.keys())
		self.number_of_responses = len(self.current_responses_list)
		self.hovered_index = 0
		self.hovered_response = \
			self.current_responses_list[self.hovered_index]


	def leave_dialogue(self):
		self.conversation_partner   = None
		self.current_dialogue       = th.TextBundle("")
		self.current_responses_dict = {}
		self.current_responses_list = []
		self.number_of_responses    = 0
		self.hovered_index          = 0
		self.hovered_response       = th.TextBundle("")

	def listener(self):
		if self.conversation_partner is not None:
			for speech in self.conversation_partner.dt.spoken_queue:
				if speech == "Ending dialogue":
					self.spoken_queue.append("Ending dialogue")
					self.conversation_partner.dt.spoken_queue.remove(speech)
				else:
					raise NotImplementedError(
						"You haven't yet written code for the listener to "\
						"respond to that speech."
					)



	def handle_pygame_events(self, pygame_event):
		if pygame_event.type == gc.KEYDOWN:
			if pygame_event.key in gc.USE:
				self.conversation_partner.dt.send(
					self.current_responses_dict[self.hovered_response]
				)
				self.refresh_dialogue()
			if pygame_event.key in gc.UP:
				self.hovered_index = \
					(self.hovered_index - 1) % self.number_of_responses
				self.hovered_response = \
					self.current_responses_list[self.hovered_index]
			if pygame_event.key in gc.DOWN:
				self.hovered_index = \
					(self.hovered_index + 1) % self.number_of_responses
				self.hovered_response = \
					self.current_responses_list[self.hovered_index]

	def update(self):
		self.listener()

	def draw(self, DISPLAY_SURF):
		th.make_text(
			DISPLAY_SURF, 
			gc.BGCOLOR, 
			400, 400, 
			800,
			self.current_dialogue
		)
		line = 0
		for response in self.current_responses_list:
			if response == self.hovered_response:
				draw_bdl = th.TextBundle(
					"> " + response.text,
					response.font,
					gc.GREEN
				)
			else:
				draw_bdl = th.TextBundle(
					"   " + response.text,
					response.font,
					gc.TEXT_COLOR
				)
			th.make_text(
				DISPLAY_SURF, 
				gc.BGCOLOR, 
				400, 500+line*response.font.get_height(), 
				800,
				draw_bdl
			)
			line += 1


