
import math

from statemachine import StateMachine, State

import gng.dice_roller      as dr
import gng.global_constants as gc
import gng.text_handling    as th

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
		self.player.max_HP = 4 + dr.roll_x_d_n(1, self.player.class_die_size)
		self.player.current_HP = self.player.max_HP

	def set_initial_AV(self):
		self.player.AV = calculate_AV(self.player.character_class, 1)

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

# ======================================================================

class CharacterSheetManager(StateMachine):
	# "co_" stands for "cursor_over_"
	co_stats_HP_AC_and_AV = State()
	co_class_and_level    = State()
	co_equipment          = State(initial=True)
	co_portrait           = State()
	co_spells             = State()
	co_abilities          = State()

	# "is_" stands for "in_submenu_"
	is_stats_HP_AC_and_AV = State()
	is_class_and_level    = State()
	is_equipment          = State()
	is_portrait           = State()
	is_spells             = State()
	is_abilities          = State()

	# LAYOUT: (not to scale)
	# Arrows indicate transitions when in "co_" states.
	#  ___________   ________________
	# | Equipment |→| Spells         |
	# |___________|←|________________|
	#  ____↑_↓____   ______↑_↓_______
	# | Abilities |→| Portrait       |
	# |           |←|________________|
	# |           |  ______↑_↓_______
	# |           | | Class & level  |
	# |           |←|________________|
	# |           |  ______↑_↓_______
	# |           | | Stats/HP/AC/AV |
	# |___________|←|________________|

	cursor_up = (
		co_stats_HP_AC_and_AV.to(co_class_and_level) |
		co_class_and_level.to(co_portrait) |
		co_equipment.to(co_equipment) |
		co_portrait.to(co_spells) |
		co_spells.to(co_spells) |
		co_abilities.to(co_equipment)
	)
	cursor_down = (
		co_stats_HP_AC_and_AV.to(co_stats_HP_AC_and_AV) |
		co_class_and_level.to(co_stats_HP_AC_and_AV) |
		co_equipment.to(co_abilities) |
		co_portrait.to(co_class_and_level) |
		co_spells.to(co_portrait) |
		co_abilities.to(co_abilities)
	)
	cursor_left = (
		co_stats_HP_AC_and_AV.to(co_abilities) |
		co_class_and_level.to(co_abilities) |
		co_equipment.to(co_equipment) |
		co_portrait.to(co_abilities) |
		co_spells.to(co_equipment) |
		co_abilities.to(co_abilities)
	)
	cursor_right = (
		co_stats_HP_AC_and_AV.to(co_stats_HP_AC_and_AV) |
		co_class_and_level.to(co_class_and_level) |
		co_equipment.to(co_spells) |
		co_portrait.to(co_portrait) |
		co_spells.to(co_spells) |
		co_abilities.to(co_portrait)
	)
	into_submenu = (
		co_stats_HP_AC_and_AV.to(is_stats_HP_AC_and_AV) |
		co_class_and_level.to(is_class_and_level) |
		co_equipment.to(is_equipment) |
		co_portrait.to(is_portrait) |
		co_spells.to(is_spells) |
		co_abilities.to(is_abilities)
	)
	out_of_submenu = (
		is_stats_HP_AC_and_AV.to(co_stats_HP_AC_and_AV) |
		is_class_and_level.to(co_class_and_level) |
		is_equipment.to(co_equipment) |
		is_portrait.to(co_portrait) |
		is_spells.to(co_spells) |
		is_abilities.to(co_abilities)
	)
	reset = (
		co_stats_HP_AC_and_AV.to(co_equipment) |
		co_class_and_level.to(co_equipment) |
		co_equipment.to(co_equipment) |
		co_portrait.to(co_equipment) |
		co_spells.to(co_equipment) |
		co_abilities.to(co_equipment) |
		is_stats_HP_AC_and_AV.to(co_equipment) |
		is_class_and_level.to(co_equipment) |
		is_equipment.to(co_equipment) |
		is_portrait.to(co_equipment) |
		is_spells.to(co_equipment) |
		is_abilities.to(co_equipment)
	)

	def on_enter_is_equipment(self, event, state):
		self.cursor_index = 0
		if self.player.inventory != []:
			self.number_of_options = len(self.player.inventory)
		else:
			self.number_of_options = 1
			# OR we could do:
			# self.send("out_of_submenu") 
			# This would keep you from entering the submenu at all if 
			# you had no items.

	# ------------------------------------------------------------------

	def __init__(self, player):
		self.player            = player
		self.column_one_x      = 10
		self.column_two_x      = 550
		self.row_one_y         = 10
		self.row_two_y         = 450
		self.row_one_height    = 21*gc.BASIC_FONT.get_height()
		self.width             = 500
		self.cursor_index      = 0
		self.number_of_options = 0
		super().__init__()

	def cycle_up_and_down(self, pygame_event):
		if pygame_event.key in gc.UP:
			self.cursor_index = \
				(self.cursor_index - 1) % self.number_of_options
		if pygame_event.key in gc.DOWN:
			self.cursor_index = \
				(self.cursor_index + 1) % self.number_of_options

	def draw_controls(self, DISPLAY_SURF):
		text = ""
		def get_keys(val):
			return gc.pygame.key.name(val).upper()
		match self.current_state:
			case (
				self.co_abilities | self.co_class_and_level | 
				self.co_equipment | self.co_portrait | self.co_spells |
				self.co_stats_HP_AC_and_AV
			):
				text = \
					f"Select: {[get_keys(val) for val in gc.USE]}. "\
					f"Back: TODO"
			case self.is_abilities:
				pass
			case self.is_class_and_level:
				pass
			case self.is_equipment:
				if self.player.inventory != []:
					current_item = self.player.inventory[self.cursor_index]
				else:
					current_item = None
				if getattr(current_item, "equippable", False):
					slot = current_item.slot
					if current_item in getattr(self.player, slot):
						text = \
							f"Unequip: {[get_keys(val) for val in gc.USE]}. "\
							f"Back: TODO"
					else:
						text = \
							f"Equip: {[get_keys(val) for val in gc.USE]}. "\
							f"Back: TODO"
				elif getattr(current_item, "edible", False):
					text = \
						f"Eat: {[get_keys(val) for val in gc.USE]}. "\
						f"Back: TODO"
				elif getattr(current_item, "potable", False):
					text = \
						f"Drink: {[get_keys(val) for val in gc.USE]}. "\
						f"Back: TODO"
				else:
					text = \
						f"Drop: {[get_keys(val) for val in gc.USE]}. "\
						f"Back: TODO"
			case self.is_portrait:
				pass
			case self.is_spells:
				pass
			case self.is_stats_HP_AC_and_AV:
				pass
		th.make_text(
			DISPLAY_SURF,
			gc.BGCOLOR,
			500, gc.WINDOW_HEIGHT-2*gc.BASIC_FONT.get_height(),
			500,
			th.bdlr(text)
		)


	def draw_co_abilities(self, DISPLAY_SURF):
		th.make_text(
			DISPLAY_SURF,
			gc.BGCOLOR,
			self.column_one_x, self.row_two_y,
			self.width,
			th.bdlr("ABILITIES:")
		) 

	def draw_co_class_and_level(self, DISPLAY_SURF):
		th.make_text(
			DISPLAY_SURF,
			gc.BGCOLOR,
			self.column_two_x, self.row_two_y+100,
			self.width,
			th.bdlr(f"{self.player.character_class} {self.player.level}")
		) 

	def draw_co_equipment(self, DISPLAY_SURF):
		th.make_text(
			DISPLAY_SURF,
			gc.BGCOLOR,
			self.column_one_x, self.row_one_y,
			self.width,
			th.bdlr("EQUIPMENT:")
		) 
		enum = 1
		# Without .copy() you end up .pop()ing the actual inventory! 
		write_items_list = self.player.inventory.copy()
		for i in range(self.player.STR):
			if write_items_list != []:
				text_bundle = th.bdlr(f"{enum}. {write_items_list[0].name}")
			else:
				text_bundle = th.bdlr(f"{enum}.")
			th.make_text(
				DISPLAY_SURF,
				gc.BGCOLOR,
				self.column_one_x, 
				self.row_one_y+(enum)*gc.BASIC_FONT.get_height(),
				self.width,
				text_bundle
			)
			if write_items_list != []:
				write_items_list.pop(0)
			enum += 1

	def draw_co_portrait(self, DISPLAY_SURF):
		th.make_text(
			DISPLAY_SURF,
			gc.BGCOLOR,
			self.column_two_x, self.row_two_y,
			self.width,
			th.bdlr(
				f"PORTRAIT: \n "\
				f"Held: {self.player.held_slot} "\
				f"Head: {self.player.head_slot} "\
				f"Necklace: {self.player.necklace_slot} "\
				f"Armor: {self.player.armor_slot} "\
				f"Boot: {self.player.boot_slot} "\
				f"Glove: {self.player.glove_slot} "\
				f"Ring: {self.player.ring_slot} "\
				f"Back: {self.player.back_slot} "\
			)
		) 

	def draw_co_spells(self, DISPLAY_SURF):
		th.make_text(
			DISPLAY_SURF,
			gc.BGCOLOR,
			self.column_two_x, self.row_one_y,
			self.width,
			th.bdlr("SPELLS:")
		) 

	def draw_co_stats_HP_AC_and_AV(self, DISPLAY_SURF):
		av = calculate_AV(self.player.character_class, self.player.level)
		th.make_text(
			DISPLAY_SURF,
			gc.BGCOLOR,
			self.column_two_x, self.row_two_y+100+gc.BASIC_FONT.get_height(),
			self.width,
			th.bdlr(
				f"HP: {self.player.current_HP}/{self.player.max_HP} "\
				f"AC: TODO "\
				f"AV: {av} \n "\
				f"CHA: {self.player.CHA} CON: {self.player.CON} "\
				f"DEX: {self.player.DEX} \n INT: {self.player.INT} "\
				f"STR: {self.player.STR} WIS: {self.player.WIS} "\
			)
		) 

	def draw_cursor(self, DISPLAY_SURF):
		match self.current_state:
			case self.co_stats_HP_AC_and_AV:
				gc.pygame.draw.rect(
					DISPLAY_SURF, 
					gc.TEXT_COLOR,
					gc.pygame.Rect(
						self.column_two_x, 
						self.row_two_y+100+gc.BASIC_FONT.get_height(),
						self.width, 3*gc.BASIC_FONT.get_height()
					),
					5
				)
			case self.co_class_and_level: 
				gc.pygame.draw.rect(
					DISPLAY_SURF, 
					gc.TEXT_COLOR,
					gc.pygame.Rect(
						self.column_two_x, self.row_two_y+100,
						self.width, gc.BASIC_FONT.get_height()
					),
					5
				)
			case self.co_equipment:
				gc.pygame.draw.rect(
					DISPLAY_SURF, 
					gc.TEXT_COLOR,
					gc.pygame.Rect(
						self.column_one_x, self.row_one_y,
						self.width, self.row_one_height,
					),
					5
				)
			case self.co_portrait:
				gc.pygame.draw.rect(
					DISPLAY_SURF, 
					gc.TEXT_COLOR,
					gc.pygame.Rect(
						self.column_two_x, self.row_two_y,
						self.width, 100
					),
					5
				)
			case self.co_spells:
				gc.pygame.draw.rect(
					DISPLAY_SURF, 
					gc.TEXT_COLOR,
					gc.pygame.Rect(
						self.column_two_x, self.row_one_y,
						self.width, self.row_one_height,
					),
					5
				)
			case self.co_abilities:
				gc.pygame.draw.rect(
					DISPLAY_SURF, 
					gc.TEXT_COLOR,
					gc.pygame.Rect(
						self.column_one_x, self.row_two_y,
						self.width, 200
					),
					5
				)

	def handle_pygame_events(self, pygame_event):
		if pygame_event.type == gc.KEYDOWN:
			match self.current_state:
				case (
					self.co_abilities | self.co_class_and_level | 
					self.co_equipment | self.co_portrait | self.co_spells |
					self.co_stats_HP_AC_and_AV
				):
					if pygame_event.key in gc.UP:
						self.send("cursor_up")
					if pygame_event.key in gc.DOWN:
						self.send("cursor_down")
					if pygame_event.key in gc.LEFT:
						self.send("cursor_left")
					if pygame_event.key in gc.RIGHT:
						self.send("cursor_right")
					if pygame_event.key in gc.USE:
						self.send("into_submenu")
				case self.is_abilities:
					pass
				case self.is_class_and_level:
					pass
				case self.is_equipment: 
					self.cycle_up_and_down(pygame_event)
				case self.is_portrait:
					pass
				case self.is_spells:
					pass
				case self.is_stats_HP_AC_and_AV:
					pass

	def update(self):
		pass

	def draw(self, DISPLAY_SURF):
		self.draw_controls(DISPLAY_SURF)
		match self.current_state:
			case (
				self.co_abilities | self.co_class_and_level | 
				self.co_equipment | self.co_portrait | self.co_spells |
				self.co_stats_HP_AC_and_AV
			):
				self.draw_co_equipment(DISPLAY_SURF)
				self.draw_co_spells(DISPLAY_SURF)
				self.draw_co_abilities(DISPLAY_SURF)
				self.draw_co_portrait(DISPLAY_SURF)
				self.draw_co_class_and_level(DISPLAY_SURF)
				self.draw_co_stats_HP_AC_and_AV(DISPLAY_SURF)
				self.draw_cursor(DISPLAY_SURF)
			case self.is_abilities:
				pass
			case self.is_class_and_level:
				pass
			case self.is_equipment: 
				pass
				# FILL IN
			case self.is_portrait:
				pass
			case self.is_spells:
				pass
			case self.is_stats_HP_AC_and_AV:
				pass

		

# ======================================================================

def calculate_AV(character_class, level):
	match character_class:
		case "Cleric":
			return round(2/5*(level-1) + 10+(4/5))
		case "Druid":
			return round(2/5*(level-1) + 7+(4/5))
		case "Dwarf" | "Paladin" | "Ranger":
			return math.floor(1/2*(level-1) + 11)
		case "Elf":
			return round(2/3*(level-1) + 10+(2/3))
		case "Fighter":
			return math.ceil(2/3*(level-1) + 10+(2/3))
		case "Halfling":
			return math.floor(1/4*(level-1) + 12)
		case "Magic-User" | "Warlock":
			return math.ceil(1/3*(level-1) + 7+(1/3))


