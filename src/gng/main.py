import sys
from statemachine import StateMachine, State

import gng.camera_functions as cf
import gng.character_statistics as cs
import gng.dialogue_manager as dm
import gng.entity_instances as ei
import gng.global_constants as gc
import gng.player_functions as pf
import gng.text_handling as th

import gng.event_handlers.pygame_event_handler as peh
import gng.event_handlers.player_controls_event_handler as pceh




class Game(StateMachine):
    main_menu = State()
    overworld = State()
    dialogue = State()
    turns = State()
    character_creation = State(initial=True)
    character_sheet = State()

    # TEMPORARY TRANSITIONS FOR DEBUGGING ONLY. DELETE ONCE INTENTIONAL
    # TRANSITIONS HAVE BEEN ADDED. -------------------------------------
    to_overworld = (
        overworld.to(overworld)
        | dialogue.to(overworld)
        | turns.to(overworld)
        | main_menu.to(overworld)
        | character_creation.to(overworld)
        | character_sheet.to(overworld)
    )
    to_dialogue = (
        overworld.to(dialogue)
        | dialogue.to(dialogue)
        | turns.to(dialogue)
        | main_menu.to(dialogue)
        | character_creation.to(dialogue)
        | character_sheet.to(dialogue)
    )
    to_turns = (
        overworld.to(turns)
        | dialogue.to(turns)
        | turns.to(turns)
        | main_menu.to(turns)
        | character_creation.to(turns)
        | character_sheet.to(turns)
    )
    to_main_menu = (
        overworld.to(main_menu)
        | dialogue.to(main_menu)
        | turns.to(main_menu)
        | main_menu.to(main_menu)
        | character_creation.to(main_menu)
        | character_sheet.to(main_menu)
    )
    to_character_creation = (
        overworld.to(character_creation)
        | dialogue.to(character_creation)
        | turns.to(character_creation)
        | main_menu.to(character_creation)
        | character_creation.to(character_creation)
        | character_sheet.to(character_creation)
    )
    to_character_sheet = (
        overworld.to(character_sheet)
        | dialogue.to(character_sheet)
        | turns.to(character_sheet)
        | main_menu.to(character_sheet)
        | character_creation.to(character_sheet)
        | character_sheet.to(character_sheet)
    )

    # ------------------------------------------------------------------

    begin_dialogue = overworld.to(dialogue)
    end_dialogue = dialogue.to(overworld)
    end_character_creation = character_creation.to(overworld)

    def on_exit_overworld(self, event, state):
        self.player_controls.send("to_stationary")

    def on_exit_dialogue(self, event, state):
        self.dialogue_manager.leave_dialogue()

    def on_exit_character_sheet(self, event, state):
        self.character_sheet_manager.send("reset")

    # ------------------------------------------------------------------
    # ------ Above this line: FSM stuff. Below this line: other. -------
    # ------------------------------------------------------------------

    def __init__(self):
        # Pygame stuff: ------------------------------------------------
        self.FPS_CLOCK = gc.pygame.time.Clock()
        self.DISPLAY_SURF = gc.pygame.display.set_mode(
            (gc.WINDOW_WIDTH, gc.WINDOW_HEIGHT)
        )
        # Entities and gameworld objects: ------------------------------
        self.camera_target = ei.camera_target
        self.player = ei.player
        self.guy1 = ei.guy1
        self.sword = ei.sword
        self.list_of_entities = [
            self.camera_target,
            self.player,
            self.guy1,
            self.sword,
        ]
        self.list_of_npcs = [
            self.guy1,
        ]
        self.list_of_items_on_ground = [
            self.sword,
        ]

        self.list_of_collision_rects = ei.list_of_collision_rects
        # Systems managers: --------------------------------------------
        self.debugging_flag = False
        self.quitting_event_handler = peh.PygameEventHandler()
        self.dialogue_manager = dm.DialogueManager()
        self.player_controls = pf.ManualControls(
            puppet=self.player,
            list_of_entities=self.list_of_entities,
            list_of_npcs=self.list_of_npcs,
            list_of_items_on_ground=self.list_of_items_on_ground,
            list_of_collision_rects=self.list_of_collision_rects,
        )
        self.character_creator = cs.CharacterCreator(player=self.player)
        self.character_sheet_manager = cs.CharacterSheetManager(player=self.player)
        self.player_controls_event_handler = pceh.PlayerControlsEventHandler(
            self.player_controls, 
            self.list_of_npcs, 
            self.list_of_items_on_ground,
            self.dialogue_manager
        )
        super().__init__()

    def character_creator_listener(self):
        for speech in self.character_creator.spoken_queue:
            if speech == "Finished character creation":
                self.send("end_character_creation")
                self.character_creator.spoken_queue.remove(speech)
            else:
                raise NotImplementedError(
                    "You haven't yet written code for the listener to "
                    "respond to that speech."
                )

    def dialogue_listener(self):
        for speech in self.dialogue_manager.spoken_queue:
            if speech == "Ending dialogue":
                self.send("end_dialogue")
                self.dialogue_manager.spoken_queue.remove(speech)
            else:
                raise NotImplementedError(
                    "You haven't yet written code for the listener to "
                    "respond to that speech."
                )

    def event_handler_listener(self):
        for speech in self.player_controls_event_handler.spoken_queue:
            if speech == "Go to dialogue state":
                self.send("begin_dialogue")
                self.player_controls_event_handler.spoken_queue.remove(speech)

    def quit_game(self):
        gc.pygame.quit()
        sys.exit()

    def handle_pygame_events(self):
        self.player_controls_event_handler.handle_pygame_events()

        # for pygame_event in gc.pygame.event.get():
        #     if pygame_event.type == gc.QUIT:
        #         self.quit_game()
        #     if pygame_event.type == gc.KEYDOWN and pygame_event.key == gc.K_BACKQUOTE:
        #         self.debugging_flag = not self.debugging_flag
        #     match self.current_state:
        #         case self.overworld:
        #             self.player_controls.handle_pygame_events(pygame_event)
        #             if pygame_event.type == gc.KEYDOWN and pygame_event.key in gc.USE:
        #                 entity = self.player_controls.get_entity_facing()
        #                 if entity in self.list_of_npcs:
        #                     self.dialogue_manager.enter_dialogue_with(entity)
        #                     self.send("begin_dialogue")
        #                 elif entity in self.list_of_items_on_ground:
        #                     self.player_controls.pick_up(entity)
        #         case self.dialogue:
        #             self.dialogue_manager.handle_pygame_events(pygame_event)
        #         case self.turns:
        #             pass
        #         case self.main_menu:
        #             pass
        #         case self.character_sheet:
        #             self.character_sheet_manager.handle_pygame_events(pygame_event)
        #         case self.character_creation:
        #             self.character_creator.handle_pygame_events(pygame_event)
        #     # To be deleted later: -------------------------------------
        #     if pygame_event.type == gc.KEYDOWN:
        #         if pygame_event.key == gc.K_ESCAPE:
        #             self.quit_game()
        #         if pygame_event.key == gc.K_1:
        #             self.send("to_overworld")
        #         if pygame_event.key == gc.K_2:
        #             self.send("to_dialogue")
        #         if pygame_event.key == gc.K_3:
        #             self.send("to_turns")
        #         if pygame_event.key == gc.K_4:
        #             self.send("to_character_creation")
        #         if pygame_event.key == gc.K_5:
        #             self.send("to_character_sheet")
        #     # ----------------------------------------------------------

    def update(self):
        self.player_controls.update()
        match self.current_state:
            case self.overworld:
                self.camera_target.x = self.player.x
                self.camera_target.y = self.player.y
                self.event_handler_listener()
            case self.dialogue:
                self.dialogue_manager.update()
                self.dialogue_listener()
            case self.turns:
                pass
            case self.main_menu:
                pass
            case self.character_sheet:
                pass
            case self.character_creation:
                self.character_creator.update()
                self.character_creator_listener()

    def draw_in_game_world(self):
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
        match self.player_controls.current_direction_facing:
            case self.player_controls.up:
                arrow = "^"
            case self.player_controls.down:
                arrow = "v"
            case self.player_controls.left:
                arrow = "<"
            case self.player_controls.right:
                arrow = ">"
            case self.player_controls.upleft:
                arrow = "'\\"
            case self.player_controls.upright:
                arrow = "/'"
            case self.player_controls.downleft:
                arrow = "./"
            case self.player_controls.downright:
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
        # --------------------------------------------------------------

    def draw(self):
        self.DISPLAY_SURF.fill(gc.BGCOLOR)
        match self.current_state:
            case self.overworld:
                self.draw_in_game_world()
            case self.dialogue:
                self.draw_in_game_world()
                self.dialogue_manager.draw(DISPLAY_SURF=self.DISPLAY_SURF)
            case self.turns:
                self.draw_in_game_world()
            case self.main_menu:
                pass
            case self.character_sheet:
                self.character_sheet_manager.draw(DISPLAY_SURF=self.DISPLAY_SURF)
            case self.character_creation:
                self.character_creator.draw(DISPLAY_SURF=self.DISPLAY_SURF)
        if self.debugging_flag:
            th.make_text(
                self.DISPLAY_SURF,
                gc.BGCOLOR,
                10,
                10,
                gc.WINDOW_WIDTH - 20,
                th.bdlr(text="Debug menu: (toggle with `) \n"),
                th.bdlr(
                    # Add more values here when you want to track them.
                    text=f"FPS = {self.FPS_CLOCK.get_fps()} \n "
                    f"{self.current_state.name = } \n "
                    f"{self.player.inventory = } \n "
                    f"{self.character_sheet_manager.current_state = } \n "
                    f"{self.sword.rect = } \n ",
                    color=gc.BLUE,
                ),
            )
        gc.pygame.display.update()

    def run(self):
        while True:
            self.handle_pygame_events()
            self.update()
            self.draw()
            self.FPS_CLOCK.tick(gc.FPS)


def main():
    game = Game()
    game.run()
