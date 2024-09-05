import gng.camera_functions as cf
import gng.global_constants as gc
import gng.text_handling as th

class GameWorldArtist:
    def __init__(
        self, 
        DISPLAY_SURF,
        list_of_entities, 
        list_of_collision_rects, 
        manual_controls,
        camera_target,
        player
    ):
        self.DISPLAY_SURF = DISPLAY_SURF
        self.list_of_entities = list_of_entities
        self.list_of_collision_rects = list_of_collision_rects
        self.manual_controls = manual_controls
        self.camera_target = camera_target
        self.player = player

    def draw(self):
        for entity in self.list_of_entities:
            if getattr(entity, "visible_on_world_map", False):
                cf.draw_in_camera_coordinates(
                    DISPLAY_SURF=self.DISPLAY_SURF,
                    camera_target=self.camera_target,
                    entity=entity,
                    color=entity.color,
                )
        for block in self.list_of_collision_rects:
            cf.draw_in_camera_coordinates(
                DISPLAY_SURF=self.DISPLAY_SURF,
                camera_target=self.camera_target,
                entity=block,
                color=gc.WHITE,
            )
        # Until we start drawing sprites, let's just draw an "arrow" to
        # indicate the direction you are facing. Everything between this
        # comment and the next one is temporary and will be deleted when
        # we implement sprites. ----------------------------------------
        arrow = "•"
        match self.manual_controls.current_direction_facing:
            case self.manual_controls.up:
                arrow = "^"
            case self.manual_controls.down:
                arrow = "v"
            case self.manual_controls.left:
                arrow = "<"
            case self.manual_controls.right:
                arrow = ">"
            case self.manual_controls.upleft:
                arrow = "'\\"
            case self.manual_controls.upright:
                arrow = "/'"
            case self.manual_controls.downleft:
                arrow = "./"
            case self.manual_controls.downright:
                arrow = "\\."
        coord_x, coord_y = cf.convert_world_to_camera_coordinates(
            self.camera_target, self.player
        )
        th.make_text(
            self.DISPLAY_SURF,
            self.player.color,
            coord_x,
            coord_y,
            self.player.width,
            th.bdlr(arrow),
        )