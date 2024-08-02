import sys
from statemachine import StateMachine, State

import entity_factory   as ef
import global_constants as gc
import player_functions as pf

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
		self.FPS_CLOCK = gc.pygame.time.Clock()
		self.DISPLAY_SURF = gc.pygame.display.set_mode(
			(gc.WINDOW_WIDTH, gc.WINDOW_HEIGHT)
		)
		self.camera = ef.camera
		self.player = ef.player
		self.list_of_entities = [
			self.camera, self.player,
		]
		self.manualmovement = pf.ManualMovement(puppet=self.player)
		super().__init__()

	def quit_game(self):
		gc.pygame.quit()
		sys.exit()

	def handle_pygame_events(self):
		for event in gc.pygame.event.get():
			if event.type == gc.QUIT:
				self.quit_game()
			self.manualmovement.handle_pygame_events(event)
			if event.type == gc.KEYDOWN:
				if event.key == gc.K_ESCAPE:
					self.quit_game()
				if event.key == gc.K_1:
					self.send("to_overworld")
				if event.key == gc.K_2:
					self.send("to_dialogue")
				if event.key == gc.K_3:
					self.send("to_turns")



	def update(self):
		self.manualmovement.run()
		print(self.current_state)
		print(self.manualmovement.current_state)
		print(self.player.x, self.player.y)

	def draw(self):
		self.DISPLAY_SURF.fill(gc.BGCOLOR)

		# For observing camera motion:
		for x in range(100):
			gc.pygame.draw.line(
				self.DISPLAY_SURF, 
				gc.WHITE, 
				(10*x, 0), 
				(10*x, 500)
			)
		
		gc.pygame.draw.rect(self.DISPLAY_SURF, gc.BLUE, self.player.rect)
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