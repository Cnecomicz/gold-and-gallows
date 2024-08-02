import entity           as e
import global_constants as gc

camera = e.Entity(
	x=0, y=0, target=None, speed=1, zoom_level=1,
)

player = e.Entity(
	x=0, y=0, 
	width=100, height=100,  
	speed=2,
	can_move=True,
	moving=False,
)
player.rect=gc.pygame.Rect(player.x, player.y, player.width, player.height)