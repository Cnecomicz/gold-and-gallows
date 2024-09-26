from statemachine import StateMachine, State

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
        equipment_submenu.to(home)
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

    def on_enter_equipment_submenu(self, event, state):
        print("You entered equipment submenu TODO DELETE")
        self.cursor_index = 0
        if self.player.inventory != []:
            self.number_of_options = len(self.player.inventory)
        else:
            self.number_of_options = 1
            # OR we could do:
            # self.send("out_of_submenu")
            # This would keep you from entering the submenu at all if
            # you had no items.

    # ------------------------------------------------------------------

    def __init__(
            self, 
            player,
            list_of_active_x_manager
        ):
        self.player = player
        self.list_of_active_x_manager = list_of_active_x_manager
        self.cursor_index = 0
        self.number_of_options = 0 
        super().__init__()
        self.list_of_events_to_submenus_strings = \
            [f"to_{state.id}" for state in self.list_of_submenus]
        

    def reset(self):
        self.cursor_index = 0
        self.number_of_options = 0
        self.to_home()
