import sys

import entity_factory   as ef
import global_constants as gc
import state_machines   as sm

class Game:
	def __init__(self):
		self.FPS_CLOCK = \
			gc.pygame.time.Clock()
		self.DISPLAY_SURF = \
			gc.pygame.display.set_mode((gc.WINDOW_WIDTH,gc.WINDOW_HEIGHT))
		self.gameplay_state_machine = \
			sm.GameplayStateMachine()
		self.camera = \
			ef.camera

	def quit_game(self):
		gc.pygame.quit()
		sys.exit()

	def handle_events(self):
		for event in gc.pygame.event.get():
			if event.type == gc.QUIT:
				self.quit_game()
			if event.type == gc.KEYDOWN:
				if event.key == gc.K_ESCAPE:
					self.quit_game()

	def update(self):
		pass

	def draw(self):
		self.DISPLAY_SURF.fill(gc.BGCOLOR)
		# other draw
		gc.pygame.display.update()

	def run(self):
		while True:
			self.handle_events()
			self.update()
			self.draw()
			self.FPS_CLOCK.tick(gc.FPS)

def main():
	game = Game()
	game.run()

if __name__ == "__main__":
	main()