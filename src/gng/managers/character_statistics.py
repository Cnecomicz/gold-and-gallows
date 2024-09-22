import math

from statemachine import StateMachine, State

import gng.dice_roller as dr
import gng.global_constants as gc
import gng.text_handling as th


class CharacterCreator(StateMachine):
    choosing_power_level = State(initial=True)
    choosing_class = State()
    choosing_name = State(final=True)

    chose_extreme = choosing_power_level.to(choosing_class)
    chose_standard = choosing_power_level.to(choosing_class)
    chose_classic = choosing_power_level.to(choosing_class)
    chose_cleric = choosing_class.to(choosing_name)
    chose_druid = choosing_class.to(choosing_name)
    chose_dwarf = choosing_class.to(choosing_name)
    chose_elf = choosing_class.to(choosing_name)
    chose_fighter = choosing_class.to(choosing_name)
    chose_halfling = choosing_class.to(choosing_name)
    chose_magic_user = choosing_class.to(choosing_name)
    chose_paladin = choosing_class.to(choosing_name)
    chose_ranger = choosing_class.to(choosing_name)
    chose_warlock = choosing_class.to(choosing_name)

    def on_chose_extreme(self, event, state):
        self.player.CHA = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
        self.player.CON = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
        self.player.DEX = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
        self.player.INT = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
        self.player.STR = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)
        self.player.WIS = dr.roll_x_d_n_and_keep_highest_k(3, 20, 1)

    def on_chose_standard(self, event, state):
        self.player.CHA = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
        self.player.CON = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
        self.player.DEX = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
        self.player.INT = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
        self.player.STR = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)
        self.player.WIS = dr.roll_x_d_n_and_keep_highest_k(3, 10, 2)

    def on_chose_classic(self, event, state):
        self.player.CHA = dr.roll_x_d_n(3, 6)
        self.player.CON = dr.roll_x_d_n(3, 6)
        self.player.DEX = dr.roll_x_d_n(3, 6)
        self.player.INT = dr.roll_x_d_n(3, 6)
        self.player.STR = dr.roll_x_d_n(3, 6)
        self.player.WIS = dr.roll_x_d_n(3, 6)

    def on_chose_cleric(self, event, state):
        self.player.character_class = "Cleric"
        self.player.class_die_size = 8
        self.player.weapon_max_die_size = 6
        self.player.armor_max_size = "Medium"
        self.player.shield_max_size = "Large"
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_chose_druid(self, event, state):
        self.player.character_class = "Druid"
        self.player.class_die_size = 6
        self.player.weapon_max_die_size = 4
        self.player.armor_max_size = "Light"
        self.player.shield_max_size = ""
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_chose_dwarf(self, event, state):
        self.player.character_class = "Dwarf"
        self.player.class_die_size = 8
        self.player.weapon_max_die_size = 8
        self.player.armor_max_size = "Heavy"
        self.player.shield_max_size = "Large"
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_chose_elf(self, event, state):
        self.player.character_class = "Elf"
        self.player.class_die_size = 6
        self.player.weapon_max_die_size = 8
        self.player.armor_max_size = "Medium"
        self.player.shield_max_size = "Small"
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_chose_fighter(self, event, state):
        self.player.character_class = "Fighter"
        self.player.class_die_size = 10
        self.player.weapon_max_die_size = 8
        self.player.armor_max_size = "Heavy"
        self.player.shield_max_size = "Large"
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_chose_halfling(self, event, state):
        self.player.character_class = "Halfling"
        self.player.class_die_size = 6
        self.player.weapon_max_die_size = 6
        self.player.armor_max_size = "Light"
        self.player.shield_max_size = "Small"
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_chose_magic_user(self, event, state):
        self.player.character_class = "Magic-User"
        self.player.class_die_size = 4
        self.player.weapon_max_die_size = 4
        self.player.armor_max_size = "Light"
        self.player.shield_max_size = ""
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_chose_paladin(self, event, state):
        self.player.character_class = "Paladin"
        self.player.class_die_size = 10
        self.player.weapon_max_die_size = 8
        self.player.armor_max_size = "Heavy"
        self.player.shield_max_size = "Large"
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_chose_ranger(self, event, state):
        self.player.character_class = "Ranger"
        self.player.class_die_size = 8
        self.player.weapon_max_die_size = 6
        self.player.armor_max_size = "Medium"
        self.player.shield_max_size = "Small"
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_chose_warlock(self, event, state):
        self.player.character_class = "Warlock"
        self.player.class_die_size = 4
        self.player.weapon_max_die_size = 4
        self.player.armor_max_size = "Light"
        self.player.shield_max_size = ""
        self.roll_starting_HP()
        self.set_initial_AV()

    def on_enter_choosing_power_level(self, event, state):
        self.number_of_options = 3
        self.cursor_index = 1

    def on_enter_choosing_class(self, event, state):
        self.number_of_options = 10
        self.cursor_index = 0

    def on_enter_choosing_name(self, event, state):
        pass

    # ------------------------------------------------------------------

    def __init__(self, player):
        self.player = player
        self.cursor_index = 0
        self.number_of_options = 0
        super().__init__()

    def roll_starting_HP(self):
        self.player.max_HP = 4 + dr.roll_x_d_n(1, self.player.class_die_size)
        self.player.current_HP = self.player.max_HP

    def set_initial_AV(self):
        self.player.AV = calculate_AV(self.player.character_class, 1)

    def choose_power_level(self):
        match self.cursor_index:
            case 0:
                self.send("chose_extreme")
            case 1:
                self.send("chose_standard")
            case 2:
                self.send("chose_classic")

    def choose_class(self):
        match self.cursor_index:
            case 0:
                self.send("chose_cleric")
            case 1:
                self.send("chose_druid")
            case 2:
                self.send("chose_dwarf")
            case 3:
                self.send("chose_elf")
            case 4:
                self.send("chose_fighter")
            case 5:
                self.send("chose_halfling")
            case 6:
                self.send("chose_magic_user")
            case 7:
                self.send("chose_paladin")
            case 8:
                self.send("chose_ranger")
            case 9:
                self.send("chose_warlock")


# ======================================================================


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
            list_of_active_handlers,
            list_of_active_updaters,
            list_of_active_artists
        ):
        self.player = player
        self.list_of_active_handlers = list_of_active_handlers
        self.list_of_active_updaters = list_of_active_updaters
        self.list_of_active_artists = list_of_active_artists
        self.cursor_index = 0
        self.number_of_options = 0 
        super().__init__()
        self.list_of_events_to_submenus_strings = \
            [f"to_{state.id}" for state in self.list_of_submenus]
        

    def reset(self):
        self.cursor_index = 0
        self.number_of_options = 0
        self.to_home()





# ======================================================================


def calculate_AV(character_class, level):
    match character_class:
        case "Cleric":
            return round(2 / 5 * (level - 1) + 10 + (4 / 5))
        case "Druid":
            return round(2 / 5 * (level - 1) + 7 + (4 / 5))
        case "Dwarf" | "Paladin" | "Ranger":
            return math.floor(1 / 2 * (level - 1) + 11)
        case "Elf":
            return round(2 / 3 * (level - 1) + 10 + (2 / 3))
        case "Fighter":
            return math.ceil(2 / 3 * (level - 1) + 10 + (2 / 3))
        case "Halfling":
            return math.floor(1 / 4 * (level - 1) + 12)
        case "Magic-User" | "Warlock":
            return math.ceil(1 / 3 * (level - 1) + 7 + (1 / 3))
