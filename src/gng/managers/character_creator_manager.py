from statemachine import StateMachine, State

import gng.functions.character_functions as cf
import gng.functions.dice_roller as dr


class CharacterCreatorManager(StateMachine):
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
        self.player.CHA = dr.roll("3d20k1")
        self.player.CON = dr.roll("3d20k1")
        self.player.DEX = dr.roll("3d20k1")
        self.player.INT = dr.roll("3d20k1")
        self.player.STR = dr.roll("3d20k1")
        self.player.WIS = dr.roll("3d20k1")

    def on_chose_standard(self, event, state):
        self.player.CHA = dr.roll("3d10k2")
        self.player.CON = dr.roll("3d10k2")
        self.player.DEX = dr.roll("3d10k2")
        self.player.INT = dr.roll("3d10k2")
        self.player.STR = dr.roll("3d10k2")
        self.player.WIS = dr.roll("3d10k2")

    def on_chose_classic(self, event, state):
        self.player.CHA = dr.roll("3d6")
        self.player.CON = dr.roll("3d6")
        self.player.DEX = dr.roll("3d6")
        self.player.INT = dr.roll("3d6")
        self.player.STR = dr.roll("3d6")
        self.player.WIS = dr.roll("3d6")

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
        self.list_of_active_x_manager.list_of_active_handlers = [
            self.system_event_handler,
            self.debugging_event_handler,
            self.player_name_keylogger_event_handler,
        ]
        self.list_of_active_x_manager.list_of_active_updaters = [self.debugging_updater]
        self.list_of_active_x_manager.list_of_active_artists = [
            self.debugging_artist,
            self.character_creator_artist,
            self.player_name_keylogger_artist,
        ]

    # ------------------------------------------------------------------

    def __init__(
        self,
        player,
        list_of_active_x_manager,
        system_event_handler,
        debugging_event_handler,
        player_name_keylogger_event_handler,
        debugging_updater,
        debugging_artist,
        character_creator_artist,
        player_name_keylogger_artist,
    ):
        self.player = player
        self.list_of_active_x_manager = list_of_active_x_manager
        self.system_event_handler = system_event_handler
        self.debugging_event_handler = debugging_event_handler
        self.player_name_keylogger_event_handler = player_name_keylogger_event_handler
        self.debugging_updater = debugging_updater
        self.debugging_artist = debugging_artist
        self.character_creator_artist = character_creator_artist
        self.player_name_keylogger_artist = player_name_keylogger_artist
        self.cursor_index = 0
        self.number_of_options = 0
        super().__init__()

    def roll_starting_HP(self):
        self.player.max_HP = 4 + dr.roll(f"d{self.player.class_die_size}")
        self.player.current_HP = self.player.max_HP

    def set_initial_AV(self):
        self.player.AV = cf.calculate_AV(self.player.character_class, 1)

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
