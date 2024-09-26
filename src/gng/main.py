import sys
from statemachine import StateMachine, State
import pygame
# ----------------------------------------------------------------------
import gng.entity_instances as ei
import gng.global_constants as gc
# ----------------------------------------------------------------------
import gng.managers.character_creator_manager as ccm
import gng.managers.character_sheet_manager as csm
import gng.managers.clock_manager as cm
import gng.managers.dialogue_manager as dm
import gng.managers.debugging_manager as dbm
import gng.managers.gameplay_state_machine_manager as gsmm
import gng.managers.keylogger_manager as km
import gng.managers.manual_controls as mc
# ----------------------------------------------------------------------
import gng.event_handlers.pygame_event_handler as peh
import gng.event_handlers.manual_controls_event_handler as mceh
import gng.event_handlers.character_creator_event_handler as cceh
import gng.event_handlers.character_sheet_event_handler as cseh
import gng.event_handlers.dialogue_event_handler as deh
import gng.event_handlers.debugging_event_handler as dbeh
import gng.event_handlers.keylogger_event_handler as keh
# ----------------------------------------------------------------------
import gng.updaters.camera_targeting_updater as ctu
import gng.updaters.character_creator_updater as ccu
import gng.updaters.clock_updater as cu
import gng.updaters.debugging_updater as du
import gng.updaters.manual_controls_updater as mcu
# ----------------------------------------------------------------------
import gng.artists.character_creator_artist as cca
import gng.artists.character_sheet_artist as csa
import gng.artists.debugging_artist as da
import gng.artists.dialogue_artist as dia
import gng.artists.game_world_artist as gwa
import gng.artists.keylogger_artist as ka
# ----------------------------------------------------------------------
import gng.dialogue_trees.guy1_dialogue_tree as g1dt

class Game():
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
            self.player,
            self.list_of_entities,
            self.list_of_npcs,
            self.list_of_items_on_ground,
            self.list_of_collision_rects,
        )
        self.character_creator_manager = ccm.CharacterCreatorManager(
            self.player
        )
        self.character_sheet_manager = csm.CharacterSheetManager(
            self.player,
            None, # self.list_of_active_handlers
            None, # self.list_of_active_updaters
            None # self.list_of_active_artists
        )
        self.clock_manager = cm.ClockManager()
        self.debugging_manager = dbm.DebuggingManager()
        self.player_name_keylogger_manager = km.KeyloggerManager(
            self.player, 
            "name"
        )
        # Event handlers: ----------------------------------------------
        self.system_event_handler = peh.PygameEventHandler()
        self.system_event_handler.register_event_handler(
            pygame.QUIT, self.quit_game
        )
        self.manual_controls_event_handler = mceh.ManualControlsEventHandler(
            self.manual_controls, 
            self.list_of_npcs, 
            self.list_of_items_on_ground,
            self.dialogue_manager,
            None # self.gameplay_state_machine_manager
        )
        self.character_creator_event_handler = cceh.CharacterCreatorEventHandler(
            self.character_creator_manager
        )
        self.character_sheet_event_handler = cseh.CharacterSheetEventHandler(
            self.character_sheet_manager,
            None # self.gameplay_state_machine_manager
        )
        self.dialogue_event_handler = deh.DialogueEventHandler(
            self.dialogue_manager,
            self.clock_manager
        )
        self.debugging_event_handler = dbeh.DebuggingEventHandler(
            self.debugging_manager
        )
        self.player_name_keylogger_event_handler = keh.KeyloggerEventHandler(
            self.player_name_keylogger_manager
        )
        self.list_of_active_handlers = []
        # Updaters -----------------------------------------------------
        self.character_creator_updater = ccu.CharacterCreatorUpdater(
            self.character_creator_manager,
            None # self.gameplay_state_machine_manager
        )
        self.manual_controls_updater = mcu.ManualControlsUpdater(
            self.manual_controls
        )
        self.clock_updater = cu.ClockUpdater(
            self.clock_manager
        )
        self.camera_targeting_updater = ctu.CameraTargetingUpdater(
            self.camera_target, 
            self.player
        )
        self.debugging_updater = du.DebuggingUpdater(
            self.debugging_manager,
            self.FPS_CLOCK, 
            None, # self.gameplay_state_machine_manager
            self.player,
            self.character_sheet_manager
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
            self.character_creator_manager,
            self.player
        )
        self.debugging_artist = da.DebuggingArtist(
            self.debugging_manager,
            self.clock_manager
        )
        self.dialogue_artist = dia.DialogueArtist(
            self.dialogue_manager
        )
        self.character_sheet_artist = csa.CharacterSheetArtist(
            self.character_sheet_manager,
            self.player
        )
        self.player_name_keylogger_artist = ka.KeyloggerArtist(
            self.player_name_keylogger_manager
        )
        self.list_of_active_artists = []
        # Giving nested FSMs access to the list_of_active_*s------------
        self.character_sheet_manager.list_of_active_handlers = \
            self.list_of_active_handlers
        self.character_sheet_manager.list_of_active_updaters = \
            self.list_of_active_updaters
        self.character_sheet_manager.list_of_active_artists = \
            self.list_of_active_artists
        # Gameplay state machine manager -------------------------------
        self.gameplay_state_machine_manager = gsmm.GameplayStateMachineManager(
            self.list_of_active_handlers,
            self.list_of_active_updaters,
            self.list_of_active_artists,
            self.manual_controls,
            self.dialogue_manager,
            self.character_sheet_manager,
            self.system_event_handler,
            self.manual_controls_event_handler,
            self.character_creator_event_handler,
            self.character_sheet_event_handler,
            self.dialogue_event_handler,
            self.debugging_event_handler,
            self.character_creator_updater,
            self.manual_controls_updater,
            self.clock_updater,
            self.camera_targeting_updater,
            self.debugging_updater,
            self.game_world_artist,
            self.character_creator_artist,
            self.debugging_artist,
            self.dialogue_artist,
            self.character_sheet_artist
        )
        # Hodge-podge of things that need to go after creating GSMM ----
        self.manual_controls_event_handler.gameplay_state_machine_manager = \
            self.gameplay_state_machine_manager
        self.character_sheet_event_handler.gameplay_state_machine_manager = \
            self.gameplay_state_machine_manager
        self.character_creator_updater.gameplay_state_machine_manager = \
            self.gameplay_state_machine_manager
        self.debugging_updater.gameplay_state_machine_manager = \
            self.gameplay_state_machine_manager
        self.guy1.dt = g1dt.Guy1DialogueTree(
            self.gameplay_state_machine_manager
        )

    def quit_game(self, pygame_event):
        pygame.quit()
        sys.exit()

    def handle_pygame_events(self):
        for pygame_event in pygame.event.get():
            for handler in \
            self.gameplay_state_machine_manager.list_of_active_handlers:
                handler.handle_pygame_event(pygame_event)

    def update(self):
        for updater in \
        self.gameplay_state_machine_manager.list_of_active_updaters:
            updater.update()

    def draw(self):
        self.DISPLAY_SURF.fill(gc.BGCOLOR)
        for artist in \
        self.gameplay_state_machine_manager.list_of_active_artists: 
            artist.draw(self.DISPLAY_SURF)
        pygame.display.update()

    def run(self):
        while True:
            self.handle_pygame_events()
            self.update()
            self.draw()
            self.FPS_CLOCK.tick(gc.FPS)


def main():
    game = Game()
    game.run()
