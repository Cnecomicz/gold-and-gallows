import global_constants as gc

def convert_world_to_camera_coordinates(camera_target, entity):
	"""Input: gameworld coordinates. Output: on-screen coordinates."""
	return (
		entity.x - camera_target.x + gc.WINDOW_WIDTH//2, 
		entity.y - camera_target.y + gc.WINDOW_HEIGHT//2
	)

def draw_in_camera_coordinates(DISPLAY_SURF, camera_target, entity, color):
	(camera_x, camera_y) = convert_world_to_camera_coordinates(
		camera_target, entity
	)
	camera_rect = gc.pygame.Rect(
		camera_x, camera_y, 
		entity.width, entity.height
	)
	gc.pygame.draw.rect(
		DISPLAY_SURF, color, camera_rect
	)
