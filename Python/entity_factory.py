import entity           as e
import global_constants as gc

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

camera = e.Entity(
	x=0, y=0, speed=1, zoom_level=1,
)

player = e.Entity(
	x=0, y=0, 
	width=30, height=30,  
	color=gc.BLUE,
	speed=4,
	can_move=True,
	moving=False,
	visible_on_world_map=True,
)
player.rect=gc.pygame.Rect(player.x, player.y, player.width, player.height)