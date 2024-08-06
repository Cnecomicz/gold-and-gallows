import sys
from statemachine import StateMachine, State

import camera_functions as cf
import dialogue_manager as dm
import entity_factory   as ef
import global_constants as gc
import player_functions as pf
import text_handling    as th

class Game(StateMachine):
	overworld = State(initial=True)
	dialogue  = State()
	turns     = State() 

	to_overworld = (
		overworld.to(overworld) | 
		dialogue.to(overworld) | 
		turns.to(overworld)
	)
	to_dialogue = (
		overworld.to(dialogue) | 
		dialogue.to(dialogue) | 
		turns.to(dialogue)
	)
	to_turns = (
		overworld.to(turns) | 
		dialogue.to(turns) | 
		turns.to(turns)
	)
	begin_dialogue = overworld.to(dialogue)

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
		super().__init__()

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
			# ----------------------------------------------------------



	def update(self):
		self.player_controls.update()
		match self.current_state:
			case self.overworld:
				self.camera.x = self.player.x
				self.camera.y = self.player.y
			case self.dialogue:
				pass
			case self.turns:
				pass

	def draw(self):
		self.DISPLAY_SURF.fill(gc.BGCOLOR)

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
					f"{self.player_controls.current_state.name = } \n "\
					f"{self.dialogue_manager.number_of_responses = } \n "\
					f"{self.dialogue_manager.hovered_index = } \n "\
					f"{self.dialogue_manager.conversation_partner = } \n "\
					f"{self.dialogue_manager.current_responses_dict = } \n ",
					color=gc.BLUE
				)
			)
		match self.current_state:
			case self.overworld:
				pass
			case self.dialogue:
				self.dialogue_manager.draw(DISPLAY_SURF=self.DISPLAY_SURF)
			case self.turns:
				pass

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