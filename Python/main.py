import sys
from statemachine import StateMachine, State

import camera_functions   as cf
import collision_handling as ch
import entity_factory     as ef
import global_constants   as gc
import player_functions   as pf

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

	def on_enter_overworld(self, event, state):
		pass
		# pseudocode:
		# set self.camera.target to the player
		# then inside of game.update, every tick if
		# (x, y) != (target), move the camera to the target

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
		self.list_of_entities        = [
			self.camera, self.player,
		]
		self.list_of_collision_rects = ef.list_of_collision_rects
		# Systems managers: --------------------------------------------
		self.player_movement  = pf.ManualMovement(
			puppet=self.player,
			list_of_collision_rects=self.list_of_collision_rects
		)
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
			match self.current_state:
				case self.overworld:
					self.player_movement.handle_pygame_events(event)
				case self.dialogue:
					self.player_movement.send("to_stationary")
				case self.turns:
					self.player_movement.send("to_stationary")



	def update(self):
		self.player_movement.run()
		print(f"{self.current_state.name = }")
		print(f"{self.player_movement.current_state.name = }")
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