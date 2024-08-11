import global_constants as gc

# This code lets us define an indeterminate amount of components when we 
# instantiate an object of Entity. You can also add new components to an 
# Entity after creation by simply declaring them (e.g., Bob.x = 5 makes 
# Bob have an attribute of x with value 5 _even if_ Bob previously did 
# not have an attribute of x.

class Entity:
	def __init__(self, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

# ----------------------------------------------------------------------

class NPC:
	def __init__(
		self, name, x, y, width, height, color, dt, 
		visible_on_world_map=True, interactable=True, 
	):
		self.name                 = name
		self.x                    = x
		self.y                    = y
		self.width                = width
		self.height               = height
		self.color                = color
		self.dt                   = dt
		self.visible_on_world_map = visible_on_world_map
		self.interactable         = interactable

		self.rect                 = \
			gc.pygame.Rect(self.x, self.y, self.width, self.height)

class Item:
	def __init__(
		self, name, x, y, width, height, color, equippable,
		visible_on_world_map=True, interactable=True, slot=None,
	):
		self.name                 = name
		self.x                    = x
		self.y                    = y
		self.width                = width
		self.height               = height
		self.color                = color
		self.equippable           = equippable
		self.visible_on_world_map = visible_on_world_map
		self.interactable         = interactable
		self.slot                 = slot
		if self.equippable and (self.slot == None):
			raise NotImplementedError("An equippable item needs a slot.")

		self.rect                 = \
			gc.pygame.Rect(self.x, self.y, self.width, self.height)

