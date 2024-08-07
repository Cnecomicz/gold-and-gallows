from statemachine import StateMachine, State

import dice_roller      as dr
import global_constants as gc
import player_functions as pf
import text_handling    as th

class CharacterCreator(StateMachine):
	choosing_power_level = State(initial=True)
	choosing_class       = State()
	choosing_name        = State(final=True)

	chose_extreme    = choosing_power_level.to(choosing_class)
	chose_standard   = choosing_power_level.to(choosing_class)
	chose_classic    = choosing_power_level.to(choosing_class)
	chose_cleric     = choosing_class.to(choosing_name)
	chose_druid      = choosing_class.to(choosing_name)
	chose_dwarf      = choosing_class.to(choosing_name)
	chose_elf        = choosing_class.to(choosing_name)
	chose_fighter    = choosing_class.to(choosing_name)
	chose_halfling   = choosing_class.to(choosing_name)
	chose_magic_user = choosing_class.to(choosing_name)
	chose_paladin    = choosing_class.to(choosing_name)
	chose_ranger     = choosing_class.to(choosing_name)
	chose_warlock    = choosing_class.to(choosing_name)

	def on_chose_extreme(self, event, state):
		self.player.CHA = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
		self.player.CON = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
		self.player.DEX = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
		self.player.INT = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
		self.player.STR = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
		self.player.WIS = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
 
	def on_chose_standard(self, event, state):
		self.player.CHA = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
		self.player.CON = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
		self.player.DEX = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
		self.player.INT = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
		self.player.STR = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
		self.player.WIS = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)

	def on_chose_classic(self, event, state):
		self.player.CHA = dr.roll_x_d_n(3, 6)
		self.player.CON = dr.roll_x_d_n(3, 6)
		self.player.DEX = dr.roll_x_d_n(3, 6)
		self.player.INT = dr.roll_x_d_n(3, 6)
		self.player.STR = dr.roll_x_d_n(3, 6)
		self.player.WIS = dr.roll_x_d_n(3, 6)

	def on_chose_cleric(self, event, state):
		self.player.character_class     = "Cleric"
		self.player.class_die_size      = 8
		self.player.weapon_max_die_size = 6
		self.player.armor_max_size      = "Medium"
		self.player.shield_max_size     = "Large"
		self.roll_starting_HP()
		self.set_initial_AV()

	def on_chose_druid(self, event, state):
		self.player.character_class     = "Druid"
		self.player.class_die_size      = 6
		self.player.weapon_max_die_size = 4
		self.player.armor_max_size      = "Light"
		self.player.shield_max_size     = ""
		self.roll_starting_HP()
		self.set_initial_AV()

	def on_chose_dwarf(self, event, state):
		self.player.character_class     = "Dwarf"
		self.player.class_die_size      = 8
		self.player.weapon_max_die_size = 8
		self.player.armor_max_size      = "Heavy"
		self.player.shield_max_size     = "Large"
		self.roll_starting_HP()
		self.set_initial_AV()

	def on_chose_elf(self, event, state):
		self.player.character_class     = "Elf"
		self.player.class_die_size      = 6
		self.player.weapon_max_die_size = 8
		self.player.armor_max_size      = "Medium"
		self.player.shield_max_size     = "Small"
		self.roll_starting_HP()
		self.set_initial_AV()

	def on_chose_fighter(self, event, state):
		self.player.character_class     = "Fighter"
		self.player.class_die_size      = 10
		self.player.weapon_max_die_size = 8
		self.player.armor_max_size      = "Heavy"
		self.player.shield_max_size     = "Large"
		self.roll_starting_HP()
		self.set_initial_AV()

	def on_chose_halfling(self, event, state):
		self.player.character_class     = "Halfling"
		self.player.class_die_size      = 6
		self.player.weapon_max_die_size = 6
		self.player.armor_max_size      = "Light"
		self.player.shield_max_size     = "Small"
		self.roll_starting_HP()
		self.set_initial_AV()

	def on_chose_magic_user(self, event, state):
		self.player.character_class     = "Magic-User"
		self.player.class_die_size      = 4
		self.player.weapon_max_die_size = 4
		self.player.armor_max_size      = "Light"
		self.player.shield_max_size     = ""
		self.roll_starting_HP()
		self.set_initial_AV()

	def on_chose_paladin(self, event, state):
		self.player.character_class     = "Paladin"
		self.player.class_die_size      = 10
		self.player.weapon_max_die_size = 8
		self.player.armor_max_size      = "Heavy"
		self.player.shield_max_size     = "Large"
		self.roll_starting_HP()
		self.set_initial_AV()

	def on_chose_ranger(self, event, state):
		self.player.character_class     = "Ranger"
		self.player.class_die_size      = 8
		self.player.weapon_max_die_size = 6
		self.player.armor_max_size      = "Medium"
		self.player.shield_max_size     = "Small"
		self.roll_starting_HP()
		self.set_initial_AV()

	def on_chose_warlock(self, event, state):
		self.player.character_class     = "Warlock"
		self.player.class_die_size      = 4
		self.player.weapon_max_die_size = 4
		self.player.armor_max_size      = "Light"
		self.player.shield_max_size     = ""
		self.roll_starting_HP()
		self.set_initial_AV()



	def on_enter_choosing_power_level(self, event, state):
		self.number_of_options = 3
		self.cursor_index      = 1

	def on_enter_choosing_class(self, event, state):
		self.number_of_options = 10
		self.cursor_index      = 0

	# ------------------------------------------------------------------

	def __init__(self, player):
		self.player            = player
		self.cursor_index      = 0
		self.number_of_options = 0
		self.spoken_queue      = []
		super().__init__()

	def roll_starting_HP(self):
		self.player.HP = 4 + dr.roll_x_d_n(1, self.player.class_die_size)

	def set_initial_AV(self):
		self.player.AV = pf.calculate_AV(self.player.character_class, 1)

	def choose_power_level(self):
		match self.cursor_index:
			case 0:
				self.send("chose_extreme")
			case 1:
				self.send("chose_standard")
			case 2:
				self.send("chose_classic")

	def choose_class(self):
		match self.cursor_index:
			case 0:
				self.send("chose_cleric")
			case 1:
				self.send("chose_druid")
			case 2:
				self.send("chose_dwarf")
			case 3:
				self.send("chose_elf")
			case 4:
				self.send("chose_fighter")
			case 5:
				self.send("chose_halfling")
			case 6:
				self.send("chose_magic_user")
			case 7:
				self.send("chose_paladin")
			case 8:
				self.send("chose_ranger")
			case 9:
				self.send("chose_warlock")

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
		match self.current_state:
			case self.choosing_power_level:
				pass
			case self.choosing_class:
				pass
			case self.choosing_name:
				if hasattr(self.player, "name"):
					self.spoken_queue.append("Finished character creation")

	def draw(self, DISPLAY_SURF):
		match self.current_state:
			case self.choosing_power_level:
				th.make_text(
					DISPLAY_SURF, 
					gc.BGCOLOR, 
					100, 100, 
					800,
					th.bdlr("Choose your capability.")
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
				match self.cursor_index:
					case 0:
						text = "CLERIC: Lorem ipsum. \n "\
							"Druid. \n "\
							"Dwarf. \n "\
							"Elf. \n "\
							"Fighter. \n "\
							"Halfling. \n "\
							"Magic-User. \n "\
							"Paladin. \n "\
							"Ranger. \n "\
							"Warlock. \n "
					case 1:
						text = "DRUID: Lorem ipsum. \n "\
							"Dwarf. \n "\
							"Elf. \n "\
							"Fighter. \n "\
							"Halfling. \n "\
							"Magic-User. \n "\
							"Paladin. \n "\
							"Ranger. \n "\
							"Warlock. \n "\
							"Cleric. \n "
					case 2:
						text = "DWARF: Lorem ipsum. \n "\
							"Elf. \n "\
							"Fighter. \n "\
							"Halfling. \n "\
							"Magic-User. \n "\
							"Paladin. \n "\
							"Ranger. \n "\
							"Warlock. \n "\
							"Cleric. \n "\
							"Druid. \n "
					case 3:
						text = "ELF: Lorem ipsum. \n "\
							"Fighter. \n "\
							"Halfling. \n "\
							"Magic-User. \n "\
							"Paladin. \n "\
							"Ranger. \n "\
							"Warlock. \n "\
							"Cleric. \n "\
							"Druid. \n "\
							"Dwarf. \n "
					case 4:
						text = "FIGHTER: Lorem ipsum. \n "\
							"Halfling. \n "\
							"Magic-User. \n "\
							"Paladin. \n "\
							"Ranger. \n "\
							"Warlock. \n "\
							"Cleric. \n "\
							"Druid. \n "\
							"Dwarf. \n "\
							"Elf. \n "
					case 5:
						text = "HALFLING: Lorem ipsum. \n "\
							"Magic-User. \n "\
							"Paladin. \n "\
							"Ranger. \n "\
							"Warlock. \n "\
							"Cleric. \n "\
							"Druid. \n "\
							"Dwarf. \n "\
							"Elf. \n "\
							"Fighter. \n "
					case 6:
						text = "MAGIC-USER: Lorem ipsum. \n "\
							"Paladin. \n "\
							"Ranger. \n "\
							"Warlock. \n "\
							"Cleric. \n "\
							"Druid. \n "\
							"Dwarf. \n "\
							"Elf. \n "\
							"Fighter. \n "\
							"Halfling. \n "
					case 7:
						text = "PALADIN: Lorem ipsum. \n "\
							"Ranger. \n "\
							"Warlock. \n "\
							"Cleric. \n "\
							"Druid. \n "\
							"Dwarf. \n "\
							"Elf. \n "\
							"Fighter. \n "\
							"Halfling. \n "\
							"Magic-User. \n "
					case 8:
						text = "RANGER: Lorem ipsum. \n "\
							"Warlock. \n "\
							"Cleric. \n "\
							"Druid. \n "\
							"Dwarf. \n "\
							"Elf. \n "\
							"Fighter. \n "\
							"Halfling. \n "\
							"Magic-User. \n "\
							"Paladin. \n "
					case 9:
						text = "WARLOCK: Lorem ipsum. \n "\
							"Cleric. \n "\
							"Druid. \n "\
							"Dwarf. \n "\
							"Elf. \n "\
							"Fighter. \n "\
							"Halfling. \n "\
							"Magic-User. \n "\
							"Paladin. \n "\
							"Ranger. \n "
				th.make_hovered_option(
					DISPLAY_SURF,
					gc.BGCOLOR,
					100, 300,
					800,
					th.bdlr(text)
				)
			case self.choosing_name:
				th.make_text(
					DISPLAY_SURF,
					gc.BGCOLOR,
					100, 100,
					800,
					th.bdlr(
						f"You are a {self.player.character_class}. \n "\
						"Please type your name."
					)
				)
				if not hasattr(self.player, "name"):
					self.player.name = th.keylogger(
						DISPLAY_SURF,
						gc.BGCOLOR,
						100, 200,
						800,
						gc.BASIC_FONT,
						gc.TEXT_COLOR
					)
				else:
					th.make_hovered_option(
						DISPLAY_SURF,
						gc.BGCOLOR,
						100, 200,
						800,
						th.bdlr(self.player.name)
					)


