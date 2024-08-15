from statemachine import StateMachine, State

import GnG.global_constants as gc

from GnG.text_handling import *

class Guy1DialogueTree(StateMachine):
	node1 = State(initial=True)
	node2 = State()
	node3 = State()
	node4 = State()

	A = node1.to(node2)
	B = node1.to(node3)
	C = node1.to(node4)
	to1 = (node2.to(node1) | node3.to(node1) | node4.to(node1))

	def on_enter_node1(self, event, state):
		self.current_dialogue  = bdlr("Hello. Yes or no?")
		self.current_responses = {bdlr("Yes") : "A", bdlr("No") : "B"}
		if self.maybe_flag:
			self.current_responses[bdlr("Maybe")] = "C"

	def on_enter_node2(self, event, state):
		self.current_dialogue  = bdlr("You selected yes.")
		self.current_responses = {bdlr("Goodbye.") : "to1"}

	def on_enter_node3(self, event, state):
		self.current_dialogue  = bdlr("You selected no.")
		self.current_responses = {bdlr("Goodbye.") : "to1"}

	def on_enter_node4(self, event, state):
		self.current_dialogue  = bdlr("You selected maybe.")
		self.current_responses = {bdlr("Goodbye.") : "to1"}

	def on_exit_state(self, event, state):
		self.current_dialogue  = bdlr("")
		self.current_responses = {}

	def on_to1(self, event, state):
		self.spoken_queue.append("Ending dialogue")
		self.maybe_flag = not self.maybe_flag

	def __init__(self):
		self.current_dialogue  = bdlr("")
		self.current_responses = {} # Text : Transition
		self.maybe_flag        = False
		self.spoken_queue      = []
		super().__init__()

guy1dt = Guy1DialogueTree()