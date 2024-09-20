import pygame
from statemachine import StateMachine, State

class GameplayStateMachineManager(StateMachine):
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
    pause = overworld.to(character_sheet) | character_sheet.to(overworld)

    def on_enter_character_creation(self, event, state):
        self.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler,
            self.character_creator_event_handler
        ]
        self.list_of_active_updaters = [
            self.debugging_updater,
            self.character_creator_updater
        ]
        self.list_of_active_artists = [
            self.debugging_artist,
            self.character_creator_artist
        ]

    def on_exit_character_creation(self, event, state):
        pass

    def on_enter_overworld(self, event, state):
        self.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler,
            self.manual_controls_event_handler
        ]
        self.list_of_active_updaters = [
            self.debugging_updater,
            self.manual_controls_updater,
            self.clock_updater,
            self.camera_targeting_updater
        ]
        self.list_of_active_artists = [
            self.debugging_artist,
            self.game_world_artist
        ]

    def on_exit_overworld(self, event, state):
        self.manual_controls.send("to_stationary")

    def on_enter_dialogue(self, event, state):
        self.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler,
            self.dialogue_event_handler
        ]
        self.list_of_active_updaters = [
            self.debugging_updater
        ]
        self.list_of_active_artists = [
            self.debugging_artist,
            self.game_world_artist,
            self.dialogue_artist
        ]

    def on_exit_dialogue(self, event, state):
        self.dialogue_manager.leave_dialogue()

    def on_enter_character_sheet(self, event, state):
        self.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler,
            self.character_sheet_event_handler
        ]
        self.list_of_active_updaters = [
            self.debugging_updater
        ]
        self.list_of_active_artists = [
            self.debugging_artist,
            self.character_sheet_artist
        ]

    def on_exit_character_sheet(self, event, state):
        self.character_sheet_manager.send("reset")

    def on_enter_turns(self, event, state):
        self.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler
        ]
        self.list_of_active_updaters = [
            self.debugging_updater
        ]
        self.list_of_active_artists = [
            self.debugging_artist,
            self.game_world_artist
        ]

    def on_exit_turns(self, event, state):
        pass

    # ------------------------------------------------------------------

    def __init__(
        self,
        list_of_active_handlers,
        list_of_active_updaters,
        list_of_active_artists,
        manual_controls,
        dialogue_manager,
        character_sheet_manager,
        system_event_handler,
        manual_controls_event_handler,
        character_creator_event_handler,
        character_sheet_event_handler,
        dialogue_event_handler,
        debugging_event_handler,
        character_creator_updater,
        manual_controls_updater,
        clock_updater,
        camera_targeting_updater,
        debugging_updater,
        game_world_artist,
        character_creator_artist,
        debugging_artist,
        dialogue_artist,
        character_sheet_artist,
    ):
        self.list_of_active_handlers = list_of_active_handlers
        self.list_of_active_updaters = list_of_active_updaters
        self.list_of_active_artists = list_of_active_artists
        self.manual_controls = manual_controls
        self.dialogue_manager = dialogue_manager
        self.character_sheet_manager = character_sheet_manager
        self.system_event_handler = system_event_handler
        self.manual_controls_event_handler = manual_controls_event_handler
        self.character_creator_event_handler = character_creator_event_handler
        self.character_sheet_event_handler = character_sheet_event_handler
        self.dialogue_event_handler = dialogue_event_handler
        self.debugging_event_handler = debugging_event_handler
        self.character_creator_updater = character_creator_updater
        self.manual_controls_updater = manual_controls_updater
        self.clock_updater = clock_updater
        self.camera_targeting_updater = camera_targeting_updater
        self.debugging_updater = debugging_updater
        self.game_world_artist = game_world_artist
        self.character_creator_artist = character_creator_artist
        self.debugging_artist = debugging_artist
        self.dialogue_artist = dialogue_artist
        self.character_sheet_artist = character_sheet_artist
        super().__init__()