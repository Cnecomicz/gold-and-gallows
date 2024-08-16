import gng.entities_and_components as ec
import gng.global_constants        as gc
from gng.DialogueTrees.guy1_dialogue_tree import *


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

# Here I'll keep track of some of the components we use. 
# ----- dt: ------------------------------------------------------------
# Dialogue tree. Every file in DialogueTrees/ has first a single class 
# which outlines the finite state machine for the given entity's 
# dialogue tree, and second a single instantiation of that class with 
# syntax "{name}dt". These files are imported via "from 
# DialogueTrees.filename.py import *" and then assigned to their
# respective entity's dt. 
# ----- equippable: ----------------------------------------------------
# A boolean. Checks if an item can be equipped. If so, there must be 
# another component called "slot".
# ----- interactable: --------------------------------------------------
# A boolean. Checks if you can initiate dialogue / pick up / etc with 
# the entity. 
# ----- slot: ----------------------------------------------------------
# Indicates which equipment slot an equippable item will fit into.
# Options are: held_slot, head_slot, necklace_slot, armor_slot, 
# boot_slot, glove_slot, ring_slot, and back_slot.
# ----- visible_on_world_map: ------------------------------------------
# A boolean. As of now implicitly needs a rect and a color. 



camera_target = ec.Entity(
	x=0, y=0, speed=1, zoom_level=1,
)

player = ec.Entity(
	x=0, y=0, 
	width=30, height=30,  
	color=gc.BLUE,
	speed=4,
	visible_on_world_map=True,
	level=1,
	inventory=[],
	held_slot=[], # Max size: number_of_arms
	glove_slot=[], # Max size: number_of_arms
	number_of_arms=2,
	head_slot=[], # Max size: number_of_heads
	necklace_slot=[], # Max size: number_of_heads
	number_of_heads=1,
	boot_slot=[], # Max size: number_of_legs
	number_of_legs=2,
	ring_slot=[], # Max size: number_of_fingers
	number_of_fingers_on_a_hand=5,
	armor_slot=[], # Max size: number_of_torsos
	back_slot=[], # Max size: number_of_torsos
	number_of_torsos=1,
)
player.rect=gc.pygame.Rect(player.x, player.y, player.width, player.height)
player.number_of_fingers=\
	player.number_of_arms*player.number_of_fingers_on_a_hand,

guy1 = ec.Entity(
	name="Guy1",
	x=50, y=30,
	width=30, height=30,
	color=gc.GREEN,
	dt=guy1dt,
	visible_on_world_map=True, interactable=True, 
)
guy1.rect=gc.pygame.Rect(guy1.x, guy1.y, guy1.width, guy1.height)

sword = ec.Entity(
	name="Sword",
	x=150, y=100,
	width=30, height=30,
	color=gc.RED,
	visible_on_world_map=True, interactable=True,
	equippable=True,
	slot="held_slot",
)
sword.rect=gc.pygame.Rect(sword.x, sword.y, sword.width, sword.height)
