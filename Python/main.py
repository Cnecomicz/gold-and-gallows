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

	def on_exit_overworld(self, event, state):
		self.player_movement.send("to_stationary")

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
		self.player_movement = pf.ManualMovement(
			puppet=self.player,
			list_of_collision_rects=self.list_of_collision_rects,
			DISPLAY_SURF=self.DISPLAY_SURF
		)
		self.dialogue_manager = dm.DialogueManager()
		super().__init__()

	def quit_game(self):
		gc.pygame.quit()
		sys.exit()

	def handle_pygame_events(self):
		for event in gc.pygame.event.get():
			if event.type == gc.QUIT:
				self.quit_game()
			if event.type == gc.KEYDOWN:
				if event.key == gc.K_ESCAPE:
					self.quit_game()
				if event.key == gc.K_1:
					self.send("to_overworld")
				if event.key == gc.K_2:
					self.send("to_dialogue")
				if event.key == gc.K_3:
					self.send("to_turns")
				if event.key == gc.K_BACKQUOTE:
					self.debugging_flag = not self.debugging_flag
			match self.current_state:
				case self.overworld:
					self.player_movement.handle_pygame_events(event)
				case self.dialogue:
					self.dialogue_manager.handle_pygame_events(event)
				case self.turns:
					pass



	def update(self):
		self.player_movement.update()
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
		# we implement sprites.
		arrow = "•"
		match self.player_movement.current_direction_facing:
			case self.player_movement.stationary: 
				arrow = "•"
			case self.player_movement.up:
				arrow = "^"
			case self.player_movement.down:
				arrow = "v"
			case self.player_movement.left:
				arrow = "<"
			case self.player_movement.right:
				arrow = ">"
			case self.player_movement.upleft:
				arrow = "'\\"
			case self.player_movement.upright:
				arrow = "/'"
			case self.player_movement.downleft:
				arrow = "./"
			case self.player_movement.downright:
				arrow = "\\."
		coord_x, coord_y = cf.convert_world_to_camera_coordinates(
			self.camera, self.player
		)
		th.make_text(
			self.DISPLAY_SURF, 
			self.player.color, 
			coord_y, coord_x, 
			self.player.width*2,
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
					text="Debug menu: \n"
				),
				th.bdlr(
					# Add more values here when you want to track them.
					text=
					f"{self.current_state.name = } \n "\
					f"{self.player_movement.current_state.name = } \n "\
					f"{self.dialogue_manager.number_of_responses = } \n "\
					f"{self.dialogue_manager.hovered_index = } \n ",
					color=gc.BLUE
				)
			)

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