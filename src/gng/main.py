import sys
from statemachine import StateMachine, State
import pygame
# ----------------------------------------------------------------------
import gng.camera_functions as cf
import gng.entity_instances as ei
import gng.global_constants as gc
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
import gng.artists.character_creator_artist as cca
import gng.artists.debugging_artist as da
import gng.artists.dialogue_artist as dia
import gng.artists.game_world_artist as gwa
# ----------------------------------------------------------------------
import gng.managers.character_statistics as cs
import gng.managers.clock_manager as cm
import gng.managers.dialogue_manager as dm
import gng.managers.debugging_manager as dbm
import gng.managers.gameplay_state_machine_manager as gsmm
import gng.managers.manual_controls as mc
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
        # TODO: Remove everything below this comment and above the next. 
        # The Escape key should eventually be replaced with pause 
        # functionality. -----------------------------------------------
        self.system_event_handler.register_keydown_event_handler(
            pygame.K_ESCAPE, self.quit_game
        )
        # TODO: Remove everything above this comment and below the 
        # previous. ----------------------------------------------------
        self.manual_controls_event_handler = mceh.ManualControlsEventHandler(
            self.manual_controls, 
            self.list_of_npcs, 
            self.list_of_items_on_ground,
            self.dialogue_manager,
            None
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
        # Updaters -----------------------------------------------------
        self.character_creator_updater = ccu.CharacterCreatorUpdater(
            self.character_creator,
            None
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
        self.dialogue_artist = dia.DialogueArtist(
            self.dialogue_manager
        )
        # --------------------------------------------------------------
        self.gameplay_state_machine_manager = gsmm.GameplayStateMachineManager(
            self.manual_controls,
            self.dialogue_manager,
            self.system_event_handler,
            self.manual_controls_event_handler,
            self.character_creator_event_handler,
            self.character_sheet_event_handler,
            self.dialogue_event_handler,
            self.character_creator_updater,
            self.manual_controls_updater,
            self.clock_updater,
            self.camera_targeting_updater,
            self.game_world_artist,
            self.character_creator_artist,
            self.debugging_artist,
            self.dialogue_artist
        )
        self.manual_controls_event_handler.gameplay_state_machine_manager = self.gameplay_state_machine_manager
        self.character_creator_updater.gameplay_state_machine_manager = self.gameplay_state_machine_manager
        self.guy1.dt = g1dt.Guy1DialogueTree(
            self.gameplay_state_machine_manager
        )

    def quit_game(self, pygame_event):
        pygame.quit()
        sys.exit()

    def handle_pygame_events(self):
        for pygame_event in pygame.event.get():
            for handler in self.gameplay_state_machine_manager.list_of_active_handlers:
                handler.handle_pygame_event(pygame_event)

    def update(self):
        for updater in self.gameplay_state_machine_manager.list_of_active_updaters:
            updater.update()

    def draw(self):
        self.DISPLAY_SURF.fill(gc.BGCOLOR)
        for artist in reversed(self.gameplay_state_machine_manager.list_of_active_artists): 
            # TODO: this is reversed because we're handling debugging
            # differently. Reconsider this!
            artist.draw(self.DISPLAY_SURF)
        # match self.current_state:
        #     case self.dialogue:
        #         self.dialogue_manager.draw(DISPLAY_SURF=self.DISPLAY_SURF)
        #     case self.character_sheet:
        #         self.character_sheet_manager.draw(DISPLAY_SURF=self.DISPLAY_SURF)
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
            self.draw()
            self.FPS_CLOCK.tick(gc.FPS)


def main():
    game = Game()
    game.run()
