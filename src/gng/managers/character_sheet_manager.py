from statemachine import StateMachine, State

import gng.event_handlers.character_sheet_event_handlers as cseh
import gng.artists.character_sheet_artists as csa


class CharacterSheetManager(StateMachine):
    home = State(initial=True)

    list_of_submenus = [
        equipment_submenu := State(),
        spells_submenu := State(),
        abilities_submenu := State(),
        portrait_submenu := State(),
        class_and_level_submenu := State(),
        stats_HP_AC_and_AV_submenu := State(),
        log_submenu := State(),
        quit_submenu := State(),
    ]

    list_of_events_to_submenus = [
        to_equipment_submenu := home.to(equipment_submenu),
        to_spells_submenu := home.to(spells_submenu),
        to_abilities_submenu := home.to(abilities_submenu),
        to_portrait_submenu := home.to(portrait_submenu),
        to_class_and_level_submenu := home.to(class_and_level_submenu),
        to_stats_HP_AC_and_AV_submenu := home.to(stats_HP_AC_and_AV_submenu),
        to_log_submenu := home.to(log_submenu),
        to_quit_submenu := home.to(quit_submenu),
    ]

    to_home = (
        home.to(home)
        | equipment_submenu.to(home)
        | spells_submenu.to(home)
        | abilities_submenu.to(home)
        | portrait_submenu.to(home)
        | class_and_level_submenu.to(home)
        | stats_HP_AC_and_AV_submenu.to(home)
        | log_submenu.to(home)
        | quit_submenu.to(home)
    )

    def on_enter_home(self, event, state):
        self.number_of_options = len(self.list_of_submenus)
        self.list_of_active_x_manager.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler,
            self.character_sheet_event_handler,
        ]
        self.list_of_active_x_manager.list_of_active_updaters = [self.debugging_updater]
        self.list_of_active_x_manager.list_of_active_artists = [
            self.debugging_artist,
            self.character_sheet_artist,
        ]

    def on_enter_equipment_submenu(self, event, state):
        self.cursor_index = 0
        self.number_of_options = len(self.player.inventory) + 1  # +1 for "Back"

        self.list_of_active_x_manager.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler,
            cseh.CharacterSheetEventHandlerEquipment(self),
        ]
        self.list_of_active_x_manager.list_of_active_updaters = [self.debugging_updater]
        self.list_of_active_x_manager.list_of_active_artists = [
            self.debugging_artist,
            csa.CharacterSheetArtistEquipment(self, self.player),
        ]

    def on_enter_spells_submenu(self, event, state):
        self.cursor_index = 0
        self.number_of_options = len(self.player.spells) + 1  # +1 for "Back"

        self.list_of_active_x_manager.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler,
            cseh.CharacterSheetEventHandlerSpells(self),
        ]
        self.list_of_active_x_manager.list_of_active_updaters = [self.debugging_updater]
        self.list_of_active_x_manager.list_of_active_artists = [
            self.debugging_artist,
            csa.CharacterSheetArtistEquipment(self, self.player),
        ]

    def on_enter_abilities_submenu(self, event, state):
        pass

    def on_enter_portrait_submenu(self, event, state):
        pass

    def on_enter_class_and_level_submenu(self, event, state):
        pass

    def on_enter_stats_HP_AC_and_AV_submenu(self, event, state):
        pass

    def on_enter_log_submenu(self, event, state):
        pass

    def on_enter_quit_submenu(self, event, state):
        self.cursor_index = 0
        self.number_of_options = 2  # "Yes" or "No"

        self.list_of_active_x_manager.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler,
            cseh.CharacterSheetEventHandlerQuit(self),
        ]
        self.list_of_active_x_manager.list_of_active_updaters = [self.debugging_updater]
        self.list_of_active_x_manager.list_of_active_artists = [
            self.debugging_artist,
            csa.CharacterSheetArtistQuit(self),
        ]

    def on_exit_home(self, event, state):
        pass

    def on_exit_equipment_submenu(self, event, state):
        self.put_cursor_back(state)

    def on_exit_spells_submenu(self, event, state):
        self.put_cursor_back(state)

    def on_exit_abilities_submenu(self, event, state):
        self.put_cursor_back(state)

    def on_exit_portrait_submenu(self, event, state):
        self.put_cursor_back(state)

    def on_exit_class_and_level_submenu(self, event, state):
        self.put_cursor_back(state)

    def on_exit_stats_HP_AC_and_AV_submenu(self, event, state):
        self.put_cursor_back(state)

    def on_exit_log_submenu(self, event, state):
        self.put_cursor_back(state)

    def on_exit_quit_submenu(self, event, state):
        self.put_cursor_back(state)

    # ------------------------------------------------------------------

    def __init__(
        self,
        player,
        list_of_active_x_manager,
        system_event_handler,
        debugging_event_handler,
        character_sheet_event_handler,
        debugging_updater,
        debugging_artist,
        character_sheet_artist,
    ):
        self.player = player
        self.list_of_active_x_manager = list_of_active_x_manager
        self.system_event_handler = system_event_handler
        self.debugging_event_handler = debugging_event_handler
        self.character_sheet_event_handler = character_sheet_event_handler
        self.debugging_updater = debugging_updater
        self.debugging_artist = debugging_artist
        self.character_sheet_artist = character_sheet_artist
        self.cursor_index = 0
        self.number_of_options = 0
        super().__init__()
        self.list_of_events_to_submenus_strings = [
            f"to_{state.id}" for state in self.list_of_submenus
        ]

    def reset(self):
        self.cursor_index = 0
        self.number_of_options = 0
        self.to_home()

    def put_cursor_back(self, state):
        self.cursor_index = self.list_of_submenus.index(state)
