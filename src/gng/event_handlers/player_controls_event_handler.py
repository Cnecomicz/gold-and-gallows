import pygame

import gng.event_handlers.pygame_event_handler as peh

class PlayerControlsEventHandler(peh.PygameEventHandler):
    def __init__(
        self, 
        player_controls, 
        list_of_npcs, 
        list_of_items_on_ground,
        dialogue_manager,
    ):
        self.player_controls = player_controls
        self.list_of_npcs = list_of_npcs
        self.list_of_items_on_ground = list_of_items_on_ground
        self.dialogue_manager = dialogue_manager
        self.spoken_queue = []
        super().__init__()
        self.register_keydown_event_handler(
            pygame.K_UP, self.handle_keydown_up
        )
        self.register_keydown_event_handler(
            pygame.K_w, self.handle_keydown_up
        )
        self.register_keydown_event_handler(
            pygame.K_DOWN, self.handle_keydown_down
        )
        self.register_keydown_event_handler(
            pygame.K_s, self.handle_keydown_down
        )
        self.register_keydown_event_handler(
            pygame.K_LEFT, self.handle_keydown_left
        )
        self.register_keydown_event_handler(
            pygame.K_a, self.handle_keydown_left
        )
        self.register_keydown_event_handler(
            pygame.K_RIGHT, self.handle_keydown_right
        )
        self.register_keydown_event_handler(
            pygame.K_d, self.handle_keydown_right
        )
        self.register_keyup_event_handler(
            pygame.K_UP, self.handle_keyup_up
        )
        self.register_keyup_event_handler(
            pygame.K_w, self.handle_keyup_up
        )
        self.register_keyup_event_handler(
            pygame.K_DOWN, self.handle_keyup_down
        )
        self.register_keyup_event_handler(
            pygame.K_s, self.handle_keyup_down
        )
        self.register_keyup_event_handler(
            pygame.K_LEFT, self.handle_keyup_left
        )
        self.register_keyup_event_handler(
            pygame.K_a, self.handle_keyup_left
        )
        self.register_keyup_event_handler(
            pygame.K_RIGHT, self.handle_keyup_right
        )
        self.register_keyup_event_handler(
            pygame.K_d, self.handle_keyup_right
        )
        self.register_keydown_event_handler(
            pygame.K_e, self.handle_keydown_use
        )
        self.register_keydown_event_handler(
            pygame.K_z, self.handle_keydown_use
        )

    def handle_keydown_up(self, pygame_event):
        self.player_controls.send("press_up")

    def handle_keydown_down(self, pygame_event):
        self.player_controls.send("press_down")

    def handle_keydown_left(self, pygame_event):
        self.player_controls.send("press_left")

    def handle_keydown_right(self, pygame_event):
        self.player_controls.send("press_right")

    def handle_keyup_up(self, pygame_event):
        self.player_controls.send("release_up")
        check = pygame.key.get_pressed()
        if check[pygame.K_s] or check[pygame.K_DOWN]:
            self.player_controls.send("press_down")

    def handle_keyup_down(self, pygame_event):
        self.player_controls.send("release_down")
        check = pygame.key.get_pressed()
        if check[pygame.K_w] or check[pygame.K_UP]:
            self.player_controls.send("press_up")

    def handle_keyup_left(self, pygame_event):
        self.player_controls.send("release_left")
        check = pygame.key.get_pressed()
        if check[pygame.K_d] or check[pygame.K_RIGHT]:
            self.player_controls.send("press_right")

    def handle_keyup_right(self, pygame_event):
        self.player_controls.send("release_right")
        check = pygame.key.get_pressed()
        if check[pygame.K_a] or check[pygame.K_LEFT]:
            self.player_controls.send("press_left")

    def handle_keydown_use(self, pygame_event):
        entity = self.player_controls.get_entity_facing()
        if entity in self.list_of_npcs:
            self.dialogue_manager.enter_dialogue_with(entity)
            self.spoken_queue.append("Go to dialogue state")
        elif entity in self.list_of_items_on_ground:
            self.player_controls.pick_up(entity)




