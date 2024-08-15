import GnG.global_constants as gc

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

def give_component(entity, *args):
	for arg in args:
		entity.arg = arg
	list_of_blah.append(entity)

def give_world_map_component(
	entity, x, y, width, height, color,
	visible_on_world_map=True, interactable=True
):
	entity.x = x
	entity.y = y
	entity.width = width
	entity.height = height
	entity.color = color
	entity.rect = \
		gc.pygame.Rect(entity.x, entity.y, entity.width, entity.height)
	entity.visible_on_world_map = visible_on_world_map
	entity.interactable = interactable



