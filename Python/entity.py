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
