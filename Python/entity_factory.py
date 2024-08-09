import entity           as e
import global_constants as gc
from DialogueTrees.guy1_dialogue_tree import *


list_of_collision_rects = [
	gc.pygame.Rect(100,100,10,10),
	gc.pygame.Rect(100,110,10,10),
	gc.pygame.Rect(100,120,10,10),
	gc.pygame.Rect(100,130,10,10),
	gc.pygame.Rect(100,140,10,10),
	gc.pygame.Rect(100,150,10,10),
	gc.pygame.Rect(300,200,20,80),
	gc.pygame.Rect(400,400,200,100),
	gc.pygame.Rect(-10,-10,10,500),
	gc.pygame.Rect(-10,-10,500,10),
	# gc.pygame.Rect(-10,400,500,10),
	gc.pygame.Rect(490,-10,10,500),
	gc.pygame.Rect(-50,200,200,10),
]

# Here I'll keep track of some of the components we use. ---------------
# visible_on_world_map: A boolean. As of now implicitly needs a rect and
# a color. -------------------------------------------------------------
# interactable: A boolean. Checks if you can initiate dialogue with the
# entity. --------------------------------------------------------------
# dt: Dialogue tree. Every file in DialogueTrees/ has first 
# a single class which outlines the finite state machine for the given 
# entity's dialogue tree, and second a single instantiation of that
# class with syntax "{name}dt". These files are imported via "from
# DialogueTrees.filename.py import *" and then assigned to their
# respective entity's dt. ----------------------------------------------

camera = e.Entity(
	x=0, y=0, speed=1, zoom_level=1,
)

player = e.Entity(
	x=0, y=0, 
	width=30, height=30,  
	color=gc.BLUE,
	speed=4,
	visible_on_world_map=True,
	level=1,
	inventory=[],
	main_hand_slot=None,
	off_hand_slot=None,
	head_slot=None,
	necklace_slot=None,
	armor_slot=None,
	boot_slot=None,
	glove_slot=None,
	ring_slot=None,
	back_slot=None,
)
player.rect=gc.pygame.Rect(player.x, player.y, player.width, player.height)

guy1 = e.Entity(
	name="Guy1",
	x=50, y=30,
	width=30, height=30,
	color=gc.GREEN,
	visible_on_world_map=True,
	interactable=True,
	dt=guy1dt,
)
guy1.rect=gc.pygame.Rect(guy1.x, guy1.y, guy1.width, guy1.height)

sword = e.Entity(
	name="Sword",
	x=150, y=100,
	width=30, height=30,
	color=gc.RED,
	visible_on_world_map=True,
	interactable=True,
)
sword.rect=gc.pygame.Rect(sword.x, sword.y, sword.width, sword.height)
