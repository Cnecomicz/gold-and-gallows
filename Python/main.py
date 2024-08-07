import sys
from statemachine import StateMachine, State

import character_creation as cc
import camera_functions   as cf
import dialogue_manager   as dm
import entity_factory     as ef
import global_constants   as gc
import player_functions   as pf
import text_handling      as th

class Game(StateMachine):
	main_menu          = State()
	overworld          = State(initial=True)
	dialogue           = State()
	turns              = State() 
	character_creation = State()
	paused             = State()

	# TEMPORARY TRANSITIONS FOR DEBUGGING ONLY. DELETE ONCE INTENTIONAL
	# TRANSITIONS HAVE BEEN ADDED. -------------------------------------
	to_overworld = (
		overworld.to(overworld) | 
		dialogue.to(overworld) | 
		turns.to(overworld) |
		main_menu.to(overworld) |
		character_creation.to(overworld) |
		paused.to(overworld)
	)
	to_dialogue = (
		overworld.to(dialogue) | 
		dialogue.to(dialogue) | 
		turns.to(dialogue) |
		main_menu.to(dialogue) |
		character_creation.to(dialogue) |
		paused.to(dialogue)
	)
	to_turns = (
		overworld.to(turns) | 
		dialogue.to(turns) | 
		turns.to(turns) |
		main_menu.to(turns) |
		character_creation.to(turns) |
		paused.to(turns)
	)
	to_main_menu = (
		overworld.to(main_menu) | 
		dialogue.to(main_menu) | 
		turns.to(main_menu) |
		main_menu.to(main_menu) |
		character_creation.to(main_menu) |
		paused.to(main_menu)
	)
	to_character_creation = (
		overworld.to(character_creation) | 
		dialogue.to(character_creation) | 
		turns.to(character_creation) |
		main_menu.to(character_creation) |
		character_creation.to(character_creation) |
		paused.to(character_creation)
	)
	to_paused = (
		overworld.to(paused) | 
		dialogue.to(paused) | 
		turns.to(paused) |
		main_menu.to(paused) |
		character_creation.to(paused) |
		paused.to(paused)
	)

	# ------------------------------------------------------------------

	begin_dialogue = overworld.to(dialogue)
	end_dialogue   = dialogue.to(overworld)

	def on_exit_overworld(self, event, state):
		self.player_controls.send("to_stationary")

	def on_exit_dialogue(self, event, state):
		self.dialogue_manager.leave_dialogue()

	# ------------------------------------------------------------------
	# ------ Above this line: FSM stuff. Below this line: other. -------
	# ------------------------------------------------------------------

	def __init__(self):
		# Pygame stuff: ------------------------------------------------
		self.FPS_CLOCK    = gc.pygame.time.Clock()
		self.DISPLAY_SURF = gc.pygame.display.set_mode(
			(gc.WINDOW_WIDTH, gc.WINDOW_HEIGHT)
		)
		# Entities and gameworld objects: ------------------------------
		self.camera                  = ef.camera
		self.player                  = ef.player
		self.guy1                    = ef.guy1
		self.list_of_entities        = [
			self.camera, self.player, self.guy1,
		]
		self.list_of_collision_rects = ef.list_of_collision_rects
		# Systems managers: --------------------------------------------
		self.debugging_flag  = False
		self.dialogue_manager = dm.DialogueManager()
		self.player_controls = pf.ManualControls(
			puppet=self.player,
			list_of_collision_rects=self.list_of_collision_rects,
			list_of_entities=self.list_of_entities
		)
		self.character_creator = cc.CharacterCreator(player=self.player)
		super().__init__()

	def dialogue_listener(self):
		for speech in self.dialogue_manager.spoken_queue:
			if speech == "Ending dialogue":
				self.send("end_dialogue")
				self.dialogue_manager.spoken_queue.remove(speech)
			else:
				raise NotImplementedError(
					"You haven't yet written code for the listener to "\
					"respond to that speech."
				)

	def quit_game(self):
		gc.pygame.quit()
		sys.exit()

	def handle_pygame_events(self):
		for event in gc.pygame.event.get():
			if event.type == gc.QUIT:
				self.quit_game()
			if event.type == gc.KEYDOWN and event.key == gc.K_BACKQUOTE:
				self.debugging_flag = not self.debugging_flag
			match self.current_state:
				case self.overworld:
					self.player_controls.handle_pygame_events(event)
					if event.type == gc.KEYDOWN and event.key in gc.USE:
						entity = self.player_controls.get_entity_facing()
						if entity is not None:
							self.dialogue_manager.enter_dialogue_with(
								entity
							)
							self.send("begin_dialogue")
				case self.dialogue:
					self.dialogue_manager.handle_pygame_events(event)
				case self.turns:
					pass
				case self.main_menu:
					pass
				case self.paused:
					pass
				case self.character_creation:
					self.character_creator.handle_pygame_events(event)
			# To be deleted later: -------------------------------------
			if event.type == gc.KEYDOWN:
				if event.key == gc.K_ESCAPE:
					self.quit_game()
				if event.key == gc.K_1:
					self.send("to_overworld")
				if event.key == gc.K_2:
					self.send("to_dialogue")
				if event.key == gc.K_3:
					self.send("to_turns")
				if event.key == gc.K_4:
					self.send("to_character_creation")
			# ----------------------------------------------------------



	def update(self):
		self.player_controls.update()
		match self.current_state:
			case self.overworld:
				self.camera.x = self.player.x
				self.camera.y = self.player.y
			case self.dialogue:
				self.dialogue_manager.update()
				self.dialogue_listener()
			case self.turns:
				pass
			case self.main_menu:
				pass
			case self.paused:
				pass
			case self.character_creation:
				pass

	def draw_in_game_world(self):
		for entity in self.list_of_entities:
			if getattr(entity, "visible_on_world_map", False):
				cf.draw_in_camera_coordinates(
					DISPLAY_SURF=self.DISPLAY_SURF,
					camera=self.camera,
					entity=entity,
					color=entity.color
				)
		for block in self.list_of_collision_rects:
			cf.draw_in_camera_coordinates(
				DISPLAY_SURF=self.DISPLAY_SURF,
				camera=self.camera,
				entity=block,
				color=gc.WHITE
			)
		# Until we start drawing sprites, let's just draw an "arrow" to
		# indicate the direction you are facing. Everything between this
		# comment and the next one is temporary and will be deleted when
		# we implement sprites. ----------------------------------------
		arrow = "•"
		match self.player_controls.current_direction_facing:
			case self.player_controls.up:
				arrow = "^"
			case self.player_controls.down:
				arrow = "v"
			case self.player_controls.left:
				arrow = "<"
			case self.player_controls.right:
				arrow = ">"
			case self.player_controls.upleft:
				arrow = "'\\"
			case self.player_controls.upright:
				arrow = "/'"
			case self.player_controls.downleft:
				arrow = "./"
			case self.player_controls.downright:
				arrow = "\\."
		coord_x, coord_y = cf.convert_world_to_camera_coordinates(
			self.camera, self.player
		)
		th.make_text(
			self.DISPLAY_SURF, 
			self.player.color, 
			coord_x, coord_y, 
			self.player.width,
			th.bdlr(arrow)
		)
		# --------------------------------------------------------------

	def draw(self):
		self.DISPLAY_SURF.fill(gc.BGCOLOR)

		if self.debugging_flag:
			th.make_text(
				self.DISPLAY_SURF, 
				gc.BGCOLOR, 
				10, 
				10, 
				gc.WINDOW_WIDTH-20,
				th.bdlr(
					text="Debug menu: (toggle with `) \n"
				),
				th.bdlr(
					# Add more values here when you want to track them.
					text=
					f"{self.current_state.name = } \n "\
					f"{self.character_creator.cursor_index = } \n "\
					f"{self.character_creator.current_state.name = } \n ",
					color=gc.BLUE
				)
			)
		match self.current_state:
			case self.overworld:
				self.draw_in_game_world()
			case self.dialogue:
				self.draw_in_game_world()
				self.dialogue_manager.draw(DISPLAY_SURF=self.DISPLAY_SURF)
			case self.turns:
				self.draw_in_game_world()
			case self.main_menu:
				pass
			case self.paused:
				pass
			case self.character_creation:
				self.character_creator.draw(DISPLAY_SURF=self.DISPLAY_SURF)

		gc.pygame.display.update()


	def run(self):
		while True:
			self.handle_pygame_events()
			self.update()
			self.draw()
			self.FPS_CLOCK.tick(gc.FPS)

def main():
	game = Game()
	game.run()

if __name__ == "__main__":
	main()