import pygame

import gng.global_constants as gc
import gng.event_handlers.pygame_event_handler as peh

class ManualControlsEventHandler(peh.PygameEventHandler):
    def __init__(
        self, 
        manual_controls, 
        list_of_npcs, 
        list_of_items_on_ground,
        dialogue_manager,
        gameplay_state_machine_manager
    ):
        self.manual_controls = manual_controls
        self.list_of_npcs = list_of_npcs
        self.list_of_items_on_ground = list_of_items_on_ground
        self.dialogue_manager = dialogue_manager
        self.gameplay_state_machine_manager = gameplay_state_machine_manager
        self.spoken_queue = []
        super().__init__()
        for up_key in gc.UP:
            self.register_keydown_event_handler(
                up_key, self.handle_keydown_up
            )
            self.register_keyup_event_handler(
                up_key, self.handle_keyup_up
            )
        for down_key in gc.DOWN:
            self.register_keydown_event_handler(
                down_key, self.handle_keydown_down
            )
            self.register_keyup_event_handler(
                down_key, self.handle_keyup_down
            )
        for left_key in gc.LEFT:
            self.register_keydown_event_handler(
                left_key, self.handle_keydown_left
            )
            self.register_keyup_event_handler(
                left_key, self.handle_keyup_left
            )
        for right_key in gc.RIGHT:
            self.register_keydown_event_handler(
                right_key, self.handle_keydown_right
            )
            self.register_keyup_event_handler(
                right_key, self.handle_keyup_right
            )
        for use_key in gc.USE:
            self.register_keydown_event_handler(
                use_key, self.handle_keydown_use
            )

    def handle_keydown_up(self, pygame_event):
        self.manual_controls.send("press_up")

    def handle_keydown_down(self, pygame_event):
        self.manual_controls.send("press_down")

    def handle_keydown_left(self, pygame_event):
        self.manual_controls.send("press_left")

    def handle_keydown_right(self, pygame_event):
        self.manual_controls.send("press_right")

    def handle_keyup_up(self, pygame_event):
        self.manual_controls.send("release_up")
        check = pygame.key.get_pressed()
        if check[pygame.K_s] or check[pygame.K_DOWN]:
            self.manual_controls.send("press_down")

    def handle_keyup_down(self, pygame_event):
        self.manual_controls.send("release_down")
        check = pygame.key.get_pressed()
        if check[pygame.K_w] or check[pygame.K_UP]:
            self.manual_controls.send("press_up")

    def handle_keyup_left(self, pygame_event):
        self.manual_controls.send("release_left")
        check = pygame.key.get_pressed()
        if check[pygame.K_d] or check[pygame.K_RIGHT]:
            self.manual_controls.send("press_right")

    def handle_keyup_right(self, pygame_event):
        self.manual_controls.send("release_right")
        check = pygame.key.get_pressed()
        if check[pygame.K_a] or check[pygame.K_LEFT]:
            self.manual_controls.send("press_left")

    def handle_keydown_use(self, pygame_event):
        entity = self.manual_controls.get_entity_facing()
        if entity in self.list_of_npcs:
            self.dialogue_manager.enter_dialogue_with(entity)
            self.gameplay_state_machine_manager.send("begin_dialogue")
        elif entity in self.list_of_items_on_ground:
            self.manual_controls.pick_up(entity)




