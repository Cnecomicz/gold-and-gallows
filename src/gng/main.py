import sys
from statemachine import StateMachine, State
import pygame
# ----------------------------------------------------------------------
import gng.camera_functions as cf
import gng.character_statistics as cs
import gng.clock_manager as cm
import gng.dialogue_manager as dm
import gng.debugging_manager as dbm
import gng.entity_instances as ei
import gng.global_constants as gc
import gng.manual_controls as mc
import gng.text_handling as th
# ----------------------------------------------------------------------
import gng.event_handlers.pygame_event_handler as peh
import gng.event_handlers.manual_controls_event_handler as mceh
import gng.event_handlers.character_creator_event_handler as cceh
import gng.event_handlers.character_sheet_event_handler as cseh
import gng.event_handlers.dialogue_event_handler as deh
# ----------------------------------------------------------------------
import gng.updaters.camera_targeting_updater as ctu
import gng.updaters.character_creator_updater as ccu
import gng.updaters.clock_updater as cu
import gng.updaters.manual_controls_updater as mcu
# ----------------------------------------------------------------------
import gng.listeners.character_creator_listener as ccl
import gng.listeners.current_dialogue_tree_listener as cdtl
import gng.listeners.manual_controls_event_handler_listener as mcehl
# ----------------------------------------------------------------------
import gng.artists.character_creator_artist as cca
import gng.artists.debugging_artist as da
import gng.artists.game_world_artist as gwa

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
    # END OF TEMPORARY TRANSITIONS. ------------------------------------

    begin_dialogue = overworld.to(dialogue)
    end_dialogue = dialogue.to(overworld)
    end_character_creation = character_creation.to(overworld)

    def on_enter_character_creation(self, event, state):
        self.list_of_active_handlers.append(
            self.character_creator_event_handler
        )
        self.list_of_active_updaters.append(
            self.character_creator_updater
        )
        self.list_of_active_listeners.append(
            self.character_creator_listener
        )
        self.list_of_active_artists.append(
            self.character_creator_artist
        )

    def on_exit_character_creation(self, event, state):
        self.list_of_active_handlers.remove(
            self.character_creator_event_handler
        )
        self.list_of_active_updaters.remove(
            self.character_creator_updater
        )
        self.list_of_active_listeners.remove(
            self.character_creator_listener
        )
        self.list_of_active_artists.remove(
            self.character_creator_artist
        )

    def on_enter_overworld(self, event, state):
        self.list_of_active_handlers.append(
            self.manual_controls_event_handler
        )
        self.list_of_active_listeners.append(
            self.manual_controls_event_handler_listener
        )
        self.list_of_active_updaters.append(
            self.manual_controls_updater
        )
        self.list_of_active_updaters.append(
            self.clock_updater
        )
        self.list_of_active_updaters.append(
            self.camera_targeting_updater
        )
        self.list_of_active_artists.append(
            self.game_world_artist
        )

    def on_exit_overworld(self, event, state):
        self.list_of_active_handlers.remove(
            self.manual_controls_event_handler
        )
        self.list_of_active_listeners.remove(
            self.manual_controls_event_handler_listener
        )
        self.list_of_active_updaters.remove(
            self.manual_controls_updater 
        )
        self.list_of_active_updaters.remove(
            self.clock_updater
        )
        self.list_of_active_updaters.remove(
            self.camera_targeting_updater
        )
        self.list_of_active_artists.remove(
            self.game_world_artist
        )
        self.manual_controls.send("to_stationary")

    def on_enter_dialogue(self, event, state):
        self.list_of_active_handlers.append(
            self.dialogue_event_handler
        )
        # Create the CDTL here, since it's new for every new 
        # conversation partner.
        self.current_dialogue_tree_listener = cdtl.CurrentDialogueTreeListener(
            self.dialogue_manager.conversation_partner.dt.spoken_queue,
            self.end_dialogue
        )
        self.list_of_active_listeners.append(
            self.current_dialogue_tree_listener
        )
        self.list_of_active_artists.append(
            self.game_world_artist
        )

    def on_exit_dialogue(self, event, state):
        self.list_of_active_handlers.remove(
            self.dialogue_event_handler,
        )
        self.list_of_active_listeners.remove(
            self.current_dialogue_tree_listener
        )
        self.list_of_active_artists.remove(
            self.game_world_artist
        )
        self.dialogue_manager.leave_dialogue()

    def on_enter_character_sheet(self, event, state):
        self.list_of_active_handlers.append(
            self.character_sheet_event_handler
        )

    def on_exit_character_sheet(self, event, state):
        self.list_of_active_handlers.remove(
            self.character_sheet_event_handler
        )
        self.character_sheet_manager.send("reset")

    def on_enter_turns(self, event, state):
        self.list_of_active_artists.append(
            self.game_world_artist
        )

    def on_exit_turns(self, event, state):
        self.list_of_active_artists.remove(
            self.game_world_artist
        )

    # ------------------------------------------------------------------
    # ------ Above this line: FSM stuff. Below this line: other. -------
    # ------------------------------------------------------------------

    def __init__(self):
        # Pygame stuff: ------------------------------------------------
        self.FPS_CLOCK = pygame.time.Clock()
        self.DISPLAY_SURF = pygame.display.set_mode(
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
        self.dialogue_manager = dm.DialogueManager()
        self.manual_controls = mc.ManualControls(
            puppet=self.player,
            list_of_entities=self.list_of_entities,
            list_of_npcs=self.list_of_npcs,
            list_of_items_on_ground=self.list_of_items_on_ground,
            list_of_collision_rects=self.list_of_collision_rects,
        )
        self.character_creator = cs.CharacterCreator(player=self.player)
        self.character_sheet_manager = cs.CharacterSheetManager(
            player=self.player
        )
        self.clock_manager = cm.ClockManager()
        self.debugging_manager = dbm.DebuggingManager(
            {
                "FPS": self.FPS_CLOCK.get_fps(),
                # "Current state name": self.current_state.name,
                "Inventory": self.player.inventory,
                "Character sheet current state": self.character_sheet_manager.current_state,
                "Sword rect": self.sword.rect,
            }
        )
        # Event handlers: ----------------------------------------------
        self.system_event_handler = peh.PygameEventHandler()
        self.system_event_handler.register_event_handler(
            pygame.QUIT, self.quit_game
        )
        self.system_event_handler.register_keydown_event_handler(
            pygame.K_BACKQUOTE, lambda pygame_event: setattr(
                self.debugging_manager, "debugging_flag", not self.debugging_manager.debugging_flag
            )
        )
        # TODO: Remove everything below this comment and above the next. 
        # The number keys are for in-game debugging. The Escape key 
        # should eventually be replaced with pause functionality. ------
        self.system_event_handler.register_keydown_event_handler(
            pygame.K_1, lambda pygame_event: self.send("to_overworld")
        )
        self.system_event_handler.register_keydown_event_handler(
            pygame.K_3, lambda pygame_event: self.send("to_turns")
        )
        self.system_event_handler.register_keydown_event_handler(
            pygame.K_5, lambda pygame_event: self.send("to_character_sheet")
        )
        self.system_event_handler.register_keydown_event_handler(
            pygame.K_ESCAPE, self.quit_game
        )
        # TODO: Remove everything above this comment and below the 
        # previous. ----------------------------------------------------
        self.manual_controls_event_handler = mceh.ManualControlsEventHandler(
            self.manual_controls, 
            self.list_of_npcs, 
            self.list_of_items_on_ground,
            self.dialogue_manager
        )
        self.character_creator_event_handler = cceh.CharacterCreatorEventHandler(
            self.character_creator
        )
        self.character_sheet_event_handler = cseh.CharacterSheetEventHandler(
            self.character_sheet_manager
        )
        self.dialogue_event_handler = deh.DialogueEventHandler(
            self.dialogue_manager
        )
        self.list_of_active_handlers = [self.system_event_handler,]
        # Listeners ----------------------------------------------------
        self.character_creator_listener = ccl.CharacterCreatorListener(
            self.character_creator.spoken_queue,
            self.end_character_creation
        )
        self.manual_controls_event_handler_listener = mcehl.ManualControlsEventHandlerListener(
            self.manual_controls_event_handler.spoken_queue,
            self.begin_dialogue
        )
        self.list_of_active_listeners = []
        # Updaters -----------------------------------------------------
        self.character_creator_updater = ccu.CharacterCreatorUpdater(
            self.character_creator
        )
        self.manual_controls_updater = mcu.ManualControlsUpdater(
            self.manual_controls
        )
        self.clock_updater = cu.ClockUpdater(
            self.clock_manager
        )
        self.camera_targeting_updater = ctu.CameraTargetingUpdater(
            self.camera_target, self.player
        )
        self.list_of_active_updaters = []
        # Artists ------------------------------------------------------
        self.game_world_artist = gwa.GameWorldArtist(
            self.list_of_entities, 
            self.list_of_collision_rects, 
            self.manual_controls,
            self.camera_target,
            self.player
        )
        self.character_creator_artist = cca.CharacterCreatorArtist(
            self.character_creator,
            self.player
        )
        self.debugging_artist = da.DebuggingArtist(
            self.debugging_manager, 
            self.clock_manager
        )
        self.list_of_active_artists = [self.debugging_artist,]
        super().__init__()

    def quit_game(self, pygame_event):
        pygame.quit()
        sys.exit()

    def handle_pygame_events(self):
        for pygame_event in pygame.event.get():
            for handler in self.list_of_active_handlers:
                handler.handle_pygame_event(pygame_event)

    def update(self):
        for updater in self.list_of_active_updaters:
            updater.update()

    def listen(self):
        for listener in self.list_of_active_listeners:
            listener.listen()

    def draw(self):
        self.DISPLAY_SURF.fill(gc.BGCOLOR)
        for artist in reversed(self.list_of_active_artists): # TODO: 
            # this is reversing because we're handling debugging
            # differently. Reconsider this!
            artist.draw(self.DISPLAY_SURF)
        match self.current_state:
            case self.dialogue:
                self.dialogue_manager.draw(DISPLAY_SURF=self.DISPLAY_SURF)
            case self.character_sheet:
                self.character_sheet_manager.draw(DISPLAY_SURF=self.DISPLAY_SURF)
        # if self.debugging_flag:
        #     th.make_text(
        #         self.DISPLAY_SURF,
        #         gc.BGCOLOR,
        #         10,
        #         10,
        #         gc.WINDOW_WIDTH - 20,
        #         th.bdlr(text="Debug menu: (toggle with `) \n"),
        #         th.bdlr(
        #             text=self.clock_manager.get_datetime_string() + " \n",
        #             color=gc.GREEN,
        #         ),
        #         th.bdlr(
        #             # Add more values here when you want to track them.
        #             text=f"FPS = {self.FPS_CLOCK.get_fps()} \n "
        #             f"{self.current_state.name = } \n "
        #             f"{self.player.inventory = } \n "
        #             f"{self.character_sheet_manager.current_state = } \n "
        #             f"{self.sword.rect = } \n ",
        #             color=gc.BLUE,
        #         ),
        #     )
        pygame.display.update()

    def run(self):
        while True:
            self.handle_pygame_events()
            self.update()
            self.listen()
            self.draw()
            self.FPS_CLOCK.tick(gc.FPS)


def main():
    game = Game()
    game.run()
