import pygame

import gng.global_constants as gc

class ManualControlsUpdater:
    def __init__(self, manual_controls):
        self.manual_controls = manual_controls
        self.current_frame_obstruction_up = None
        self.current_frame_obstruction_down = None
        self.current_frame_obstruction_left = None
        self.current_frame_obstruction_right = None
        self.previous_frame_obstruction_up = None
        self.previous_frame_obstruction_down = None
        self.previous_frame_obstruction_left = None
        self.previous_frame_obstruction_right = None

    def update(self):
        # The current_frame_obstructions prevent you from moving into
        # walls. The previous_frame_obstructions check if you have
        # recently moved clear of a wall. If so, then you can resume
        # moving diagonally if you are still holding that direction.
        # SIDE EFFECT: If you're running into a wall, continue to hold
        # that direction, and then press the opposite direction, then
        # you'll move clear and immediately move back, because the
        # previous_frame_obstruction check goes through. This doesn't
        # mesh with the rest of the game, where "most recently pressed
        # direction" wins, but it's minor enough I'm not addressing at
        # this time.
        check = pygame.key.get_pressed()
        self.current_frame_obstruction_up = self.manual_controls.next_wall(self.manual_controls.up)
        self.current_frame_obstruction_down = self.manual_controls.next_wall(self.manual_controls.down)
        self.current_frame_obstruction_left = self.manual_controls.next_wall(self.manual_controls.left)
        self.current_frame_obstruction_right = self.manual_controls.next_wall(self.manual_controls.right)
        if self.current_frame_obstruction_up is not None:
            self.manual_controls.send("obstruction_up")
        elif self.previous_frame_obstruction_up is not None:
            for key in gc.UP:
                if check[key]:
                    self.manual_controls.send("press_up")
        if self.current_frame_obstruction_down is not None:
            self.manual_controls.send("obstruction_down")
        elif self.previous_frame_obstruction_down is not None:
            for key in gc.DOWN:
                if check[key]:
                    self.manual_controls.send("press_down")
        if self.current_frame_obstruction_left is not None:
            self.manual_controls.send("obstruction_left")
        elif self.previous_frame_obstruction_left is not None:
            for key in gc.LEFT:
                if check[key]:
                    self.manual_controls.send("press_left")
        if self.current_frame_obstruction_right is not None:
            self.manual_controls.send("obstruction_right")
        elif self.previous_frame_obstruction_right is not None:
            for key in gc.RIGHT: 
                if check[key]:
                    self.manual_controls.send("press_right")
        self.previous_frame_obstruction_up = self.current_frame_obstruction_up
        self.previous_frame_obstruction_down = self.current_frame_obstruction_down
        self.previous_frame_obstruction_left = self.current_frame_obstruction_left
        self.previous_frame_obstruction_right = self.current_frame_obstruction_right

        # Given all of the above collision checking, your current state
        # should be the total of the directions you are pressing and the
        # non-obstructed directions. Thus we can move simply by using
        # the current_state.
        (self.manual_controls.puppet.x, self.manual_controls.puppet.y) = self.manual_controls.next_coordinates(self.manual_controls.current_state)
        # Call this function after all the collision checking.
        self.manual_controls.get_direction_facing()
        # Make sure to update the rect, not just the x and y
        # coordinates.
        if hasattr(self.manual_controls.puppet, "rect"):
            self.manual_controls.puppet.rect = pygame.Rect(
                self.manual_controls.puppet.x, self.manual_controls.puppet.y, self.manual_controls.puppet.width, self.manual_controls.puppet.height
            )
