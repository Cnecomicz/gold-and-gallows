import math

from statemachine import StateMachine, State

import global_constants as gc

class ManualMovement(StateMachine):
	stationary = State(initial=True)
	up         = State()
	down       = State()
	left       = State()
	right      = State()
	upleft     = State()
	upright    = State()
	downleft   = State()
	downright  = State()

	press_up = (
		stationary.to(up) |
		up.to(up) |
		down.to(up) |
		left.to(upleft) |
		right.to(upright) |
		upleft.to(upleft) |
		upright.to(upright) |
		downleft.to(upleft) |
		downright.to(upright)
	)
	press_down = (
		stationary.to(down) |
		up.to(down) |
		down.to(down) |
		left.to(downleft) |
		right.to(downright) |
		upleft.to(downleft) |
		upright.to(downright) |
		downleft.to(downleft) |
		downright.to(downright)
	)
	press_left = (
		stationary.to(left) |
		up.to(upleft) |
		down.to(downleft) |
		left.to(left) |
		right.to(left) |
		upleft.to(upleft) |
		upright.to(upleft) |
		downleft.to(downleft) |
		downright.to(downleft)
	)
	press_right = (
		stationary.to(right) |
		up.to(upright) |
		down.to(downright) |
		left.to(right) |
		right.to(right) |
		upleft.to(upright) |
		upright.to(upright) |
		downleft.to(downright) |
		downright.to(downright)
	)
	release_up = (
		stationary.to(stationary) |
		up.to(stationary) |
		down.to(down) |
		left.to(left) |
		right.to(right) |
		upleft.to(left) |
		upright.to(right) |
		downleft.to(downleft) |
		downright.to(downright)
	)
	release_down = (
		stationary.to(stationary) |
		up.to(up) |
		down.to(stationary) |
		left.to(left) |
		right.to(right) |
		upleft.to(upleft) |
		upright.to(upright) |
		downleft.to(left) |
		downright.to(right)
	)
	release_left = (
		stationary.to(stationary) |
		up.to(up) |
		down.to(down) |
		left.to(stationary) |
		right.to(right) |
		upleft.to(up) |
		upright.to(upright) |
		downleft.to(down) |
		downright.to(downright)
	)
	release_right = (
		stationary.to(stationary) |
		up.to(up) |
		down.to(down) |
		left.to(left) |
		right.to(stationary) |
		upleft.to(upleft) |
		upright.to(up) |
		downleft.to(downleft) |
		downright.to(down)
	)

	# ------------------------------------------------------------------
	# ------------------------------------------------------------------
	# ------------------------------------------------------------------

	def __init__(self, puppet):
		self.puppet = puppet
		super().__init__()

	def handle_pygame_events(self, pygame_event):
		if pygame_event.type == gc.KEYDOWN:
			if pygame_event.key in gc.UP:
				self.send("press_up")
			if pygame_event.key in gc.DOWN:
				self.send("press_down")
			if pygame_event.key in gc.LEFT:
				self.send("press_left")
			if pygame_event.key in gc.RIGHT:
				self.send("press_right")
		if pygame_event.type == gc.KEYUP:
			check = gc.pygame.key.get_pressed()
			if pygame_event.key in gc.UP:
				self.send("release_up")
				for key in gc.DOWN:
					if check[key]: self.send("press_down")
			if pygame_event.key in gc.DOWN:
				self.send("release_down")
				for key in gc.UP: 
					if check[key]: self.send("press_up")
			if pygame_event.key in gc.LEFT:
				self.send("release_left")
				for key in gc.RIGHT:
					if check[key]: self.send("press_right")
			if pygame_event.key in gc.RIGHT:
				self.send("release_right")
				for key in gc.LEFT:
					if check[key]: self.send("press_left")

	def run(self):
		match self.current_state:
			case self.stationary:
				self.puppet.x = math.floor(self.puppet.x)
				self.puppet.y = math.floor(self.puppet.y)
			case self.up:
				self.puppet.x = math.floor(self.puppet.x)
				self.puppet.y -= self.puppet.speed
			case self.down:
				self.puppet.x = math.floor(self.puppet.x)
				self.puppet.y += self.puppet.speed
			case self.left:
				self.puppet.x -= self.puppet.speed
				self.puppet.y = math.floor(self.puppet.y)
			case self.right:
				self.puppet.x += self.puppet.speed
				self.puppet.y = math.floor(self.puppet.y)
			case self.upleft:
				self.puppet.x -= self.puppet.speed/math.sqrt(2)
				self.puppet.y -= self.puppet.speed/math.sqrt(2)
			case self.upright:
				self.puppet.x += self.puppet.speed/math.sqrt(2)
				self.puppet.y -= self.puppet.speed/math.sqrt(2)
			case self.downleft:
				self.puppet.x -= self.puppet.speed/math.sqrt(2)
				self.puppet.y += self.puppet.speed/math.sqrt(2)
			case self.downright:
				self.puppet.x += self.puppet.speed/math.sqrt(2)
				self.puppet.y += self.puppet.speed/math.sqrt(2)
		self.puppet.rect=gc.pygame.Rect(
			self.puppet.x, self.puppet.y, self.puppet.width, self.puppet.height
		)


