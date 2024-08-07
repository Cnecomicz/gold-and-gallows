from statemachine import StateMachine, State

import dice_roller      as dr
import global_constants as gc
import text_handling    as th

class CharacterCreator(StateMachine):
	choosing_power_level = State(initial=True)
	choosing_class       = State()
	choosing_name        = State()

	to_class_extreme  = choosing_power_level.to(choosing_class)
	to_class_standard = choosing_power_level.to(choosing_class)
	to_class_classic  = choosing_power_level.to(choosing_class)
	to_name           = choosing_class.to(choosing_name)

	def on_to_class_extreme(self, event, state):
		self.player.CHA = dr.roll_x_d_n_and_keep_highest_k(3,20,1)
		self.player.CON = dr.roll_x_d_n_and_keep_highest_k(3,20,1)
		self.player.DEX = dr.roll_x_d_n_and_keep_highest_k(3,20,1)
		self.player.INT = dr.roll_x_d_n_and_keep_highest_k(3,20,1)
		self.player.STR = dr.roll_x_d_n_and_keep_highest_k(3,20,1)
		self.player.WIS = dr.roll_x_d_n_and_keep_highest_k(3,20,1)

	def on_to_class_standard(self, event, state):
		self.player.CHA = dr.roll_x_d_n_and_keep_highest_k(3,10,2)
		self.player.CON = dr.roll_x_d_n_and_keep_highest_k(3,10,2)
		self.player.DEX = dr.roll_x_d_n_and_keep_highest_k(3,10,2)
		self.player.INT = dr.roll_x_d_n_and_keep_highest_k(3,10,2)
		self.player.STR = dr.roll_x_d_n_and_keep_highest_k(3,10,2)
		self.player.WIS = dr.roll_x_d_n_and_keep_highest_k(3,10,2)

	def on_to_class_classic(self, event, state):
		self.player.CHA = dr.roll_x_d_n(3,6)
		self.player.CON = dr.roll_x_d_n(3,6)
		self.player.DEX = dr.roll_x_d_n(3,6)
		self.player.INT = dr.roll_x_d_n(3,6)
		self.player.STR = dr.roll_x_d_n(3,6)
		self.player.WIS = dr.roll_x_d_n(3,6)

	def on_enter_choosing_power_level(self, event, state):
		self.number_of_options = 3
		self.cursor_index      = 1

	def on_enter_choosing_class(self, event, state):
		self.number_of_options = 10

	# ------------------------------------------------------------------

	def __init__(self, player):
		self.player            = player
		self.cursor_index      = 0
		self.number_of_options = 0
		super().__init__()

	def choose_power_level(self):
		match self.cursor_index:
			case 0:
				self.send("to_class_extreme")
			case 1:
				self.send("to_class_standard")
			case 2:
				self.send("to_class_classic")
			case _:
				raise NotImplementedError("Cursor index out of range.")

	def roll_stats(self):
		pass

	def choose_class(self):
		pass

	def choose_name(self):
		pass

	def cycle_up_and_down(self, pygame_event):
		if pygame_event.key in gc.UP:
			self.cursor_index = \
				(self.cursor_index - 1) % self.number_of_options
		if pygame_event.key in gc.DOWN:
			self.cursor_index = \
				(self.cursor_index + 1) % self.number_of_options
		
	def handle_pygame_events(self, pygame_event):
		if pygame_event.type == gc.KEYDOWN:
			match self.current_state:
				case self.choosing_power_level:
					self.cycle_up_and_down(pygame_event)
					if pygame_event.key in gc.USE:
						self.choose_power_level()
				case self.choosing_class:
					self.cycle_up_and_down(pygame_event)
					if pygame_event.key in gc.USE:
						self.choose_class()
				case self.choosing_name:
					pass

	def update(self):
		pass

	def draw(self, DISPLAY_SURF):
		match self.current_state:
			case self.choosing_power_level:
				th.make_text(
					DISPLAY_SURF, 
					gc.BGCOLOR, 
					100, 100, 
					800,
					th.bdlr("Choose your difficulty.")
				)
				if self.cursor_index == 0:
					th.make_hovered_option(
						DISPLAY_SURF,
						gc.BGCOLOR,
						100, 200,
						800,
						th.bdlr(
							"EXTREME. Your stats will average about 15.5. "\
							"The highest a stat can be is 20 and the lowest "\
							"is 1."
						)
					)
				else:
					th.make_text(
						DISPLAY_SURF,
						gc.BGCOLOR,
						100, 200,
						800,
						th.bdlr(
							"EXTREME. Your stats will average about 15.5. "\
							"The highest a stat can be is 20 and the lowest "\
							"is 1."
						)
					)
				if self.cursor_index == 1:
					th.make_hovered_option(
						DISPLAY_SURF,
						gc.BGCOLOR,
						100, 200+2*gc.BASIC_FONT.get_height(),
						800,
						th.bdlr(
							"STANDARD. Your stats will average about 13.5. "\
							"The highest a stat can be is 20 and the lowest "\
							"is 2."
						)
					)
				else:
					th.make_text(
						DISPLAY_SURF,
						gc.BGCOLOR,
						100, 200+2*gc.BASIC_FONT.get_height(),
						800,
						th.bdlr(
							"STANDARD. Your stats will average about 13.5. "\
							"The highest a stat can be is 20 and the lowest "\
							"is 2."
						)
					)
				if self.cursor_index == 2:
					th.make_hovered_option(
						DISPLAY_SURF,
						gc.BGCOLOR,
						100, 200+4*gc.BASIC_FONT.get_height(),
						800,
						th.bdlr(
							"CLASSIC. Your stats will average about 10.5. "\
							"The highest a stat can be is 18 and the lowest "\
							"is 3."
						)
					)
				else:
					th.make_text(
						DISPLAY_SURF,
						gc.BGCOLOR,
						100, 200+4*gc.BASIC_FONT.get_height(),
						800,
						th.bdlr(
							"CLASSIC. Your stats will average about 10.5. "\
							"The highest a stat can be is 18 and the lowest "\
							"is 3."
						)
					)
			case self.choosing_class:
				th.make_text(
					DISPLAY_SURF,
					gc.BGCOLOR,
					100, 100,
					800,
					th.bdlr(
						"Your stats are as follows: \n "\
						f"Charisma: {self.player.CHA} \n "\
						f"Constitution: {self.player.CON} \n "\
						f"Dexterity: {self.player.DEX} \n "\
						f"Intelligence: {self.player.INT} \n "\
						f"Strength: {self.player.STR} \n "\
						f"Wisdom: {self.player.WIS} \n "\
						"What class would you like to be?"
					)
				)
			case self.choosing_name:
				pass

