import pygame

import gng.global_constants as gc
import gng.text_handling as th

import gng.managers.character_statistics as cs

class CharacterSheetArtist:
    def __init__(self, character_sheet_manager, player):
        self.character_sheet_manager = character_sheet_manager
        self.player = player



    def draw_controls(self, DISPLAY_SURF):
        text = ""

        def get_keys(val):
            return pygame.key.name(val).upper()

        match self.character_sheet_manager.current_state:
            case (
                self.character_sheet_manager.co_abilities
                | self.character_sheet_manager.co_class_and_level
                | self.character_sheet_manager.co_equipment
                | self.character_sheet_manager.co_portrait
                | self.character_sheet_manager.co_spells
                | self.character_sheet_manager.co_stats_HP_AC_and_AV
            ):
                text = f"Select: {[get_keys(val) for val in gc.USE]}. " f"Back: TODO"
            case self.character_sheet_manager.is_abilities:
                pass
            case self.character_sheet_manager.is_class_and_level:
                pass
            case self.character_sheet_manager.is_equipment:
                if self.character_sheet_manager.player.inventory != []:
                    current_item = self.player.inventory[self.character_sheet_manager.cursor_index]
                else:
                    current_item = None
                if getattr(current_item, "equippable", False):
                    slot = current_item.slot
                    if current_item in getattr(self.player, slot):
                        text = (
                            f"Unequip: {[get_keys(val) for val in gc.USE]}. "
                            f"Back: TODO"
                        )
                    else:
                        text = (
                            f"Equip: {[get_keys(val) for val in gc.USE]}. "
                            f"Back: TODO"
                        )
                elif getattr(current_item, "edible", False):
                    text = f"Eat: {[get_keys(val) for val in gc.USE]}. " f"Back: TODO"
                elif getattr(current_item, "potable", False):
                    text = f"Drink: {[get_keys(val) for val in gc.USE]}. " f"Back: TODO"
                else:
                    text = f"Drop: {[get_keys(val) for val in gc.USE]}. " f"Back: TODO"
            case self.character_sheet_manager.is_portrait:
                pass
            case self.character_sheet_manager.is_spells:
                pass
            case self.character_sheet_manager.is_stats_HP_AC_and_AV:
                pass
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            500,
            gc.WINDOW_HEIGHT - 2 * gc.BASIC_FONT.get_height(),
            500,
            th.bdlr(text),
        )

    def draw_co_abilities(self, DISPLAY_SURF):
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            self.character_sheet_manager.column_one_x,
            self.character_sheet_manager.row_two_y,
            self.character_sheet_manager.width,
            th.bdlr("ABILITIES:"),
        )

    def draw_co_class_and_level(self, DISPLAY_SURF):
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            self.character_sheet_manager.column_two_x,
            self.character_sheet_manager.row_two_y + 100,
            self.character_sheet_manager.width,
            th.bdlr(f"{self.player.character_class} {self.player.level}"),
        )

    def draw_co_equipment(self, DISPLAY_SURF):
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            self.character_sheet_manager.column_one_x,
            self.character_sheet_manager.row_one_y,
            self.character_sheet_manager.width,
            th.bdlr("EQUIPMENT:"),
        )
        enum = 1
        # Without .copy() you end up .pop()ing the actual inventory!
        write_items_list = self.player.inventory.copy()
        for i in range(self.player.STR):
            if write_items_list != []:
                text_bundle = th.bdlr(f"{enum}. {write_items_list[0].name}")
            else:
                text_bundle = th.bdlr(f"{enum}.")
            th.make_text(
                DISPLAY_SURF,
                gc.BGCOLOR,
                self.character_sheet_manager.column_one_x,
                self.character_sheet_manager.row_one_y + (enum) * gc.BASIC_FONT.get_height(),
                self.character_sheet_manager.width,
                text_bundle,
            )
            if write_items_list != []:
                write_items_list.pop(0)
            enum += 1

    def draw_co_portrait(self, DISPLAY_SURF):
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            self.character_sheet_manager.column_two_x,
            self.character_sheet_manager.row_two_y,
            self.character_sheet_manager.width,
            th.bdlr(
                f"PORTRAIT: \n "
                f"Held: {self.player.held_slot} "
                f"Head: {self.player.head_slot} "
                f"Necklace: {self.player.necklace_slot} "
                f"Armor: {self.player.armor_slot} "
                f"Boot: {self.player.boot_slot} "
                f"Glove: {self.player.glove_slot} "
                f"Ring: {self.player.ring_slot} "
                f"Back: {self.player.back_slot} "
            ),
        )

    def draw_co_spells(self, DISPLAY_SURF):
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            self.character_sheet_manager.column_two_x,
            self.character_sheet_manager.row_one_y,
            self.character_sheet_manager.width,
            th.bdlr("SPELLS:"),
        )

    def draw_co_stats_HP_AC_and_AV(self, DISPLAY_SURF):
        av = cs.calculate_AV(self.player.character_class, self.player.level)
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            self.character_sheet_manager.column_two_x,
            self.character_sheet_manager.row_two_y + 100 + gc.BASIC_FONT.get_height(),
            self.character_sheet_manager.width,
            th.bdlr(
                f"HP: {self.player.current_HP}/{self.player.max_HP} "
                f"AC: TODO "
                f"AV: {av} \n "
                f"CHA: {self.player.CHA} CON: {self.player.CON} "
                f"DEX: {self.player.DEX} \n INT: {self.player.INT} "
                f"STR: {self.player.STR} WIS: {self.player.WIS} "
            ),
        )

    def draw_cursor(self, DISPLAY_SURF):
        match self.character_sheet_manager.current_state:
            case self.character_sheet_manager.co_stats_HP_AC_and_AV:
                pygame.draw.rect(
                    DISPLAY_SURF,
                    gc.TEXT_COLOR,
                    pygame.Rect(
                        self.character_sheet_manager.column_two_x,
                        self.character_sheet_manager.row_two_y + 100 + gc.BASIC_FONT.get_height(),
                        self.character_sheet_manager.width,
                        3 * gc.BASIC_FONT.get_height(),
                    ),
                    5,
                )
            case self.character_sheet_manager.co_class_and_level:
                pygame.draw.rect(
                    DISPLAY_SURF,
                    gc.TEXT_COLOR,
                    pygame.Rect(
                        self.character_sheet_manager.column_two_x,
                        self.character_sheet_manager.row_two_y + 100,
                        self.character_sheet_manager.width,
                        gc.BASIC_FONT.get_height(),
                    ),
                    5,
                )
            case self.character_sheet_manager.co_equipment:
                pygame.draw.rect(
                    DISPLAY_SURF,
                    gc.TEXT_COLOR,
                    pygame.Rect(
                        self.character_sheet_manager.column_one_x,
                        self.character_sheet_manager.row_one_y,
                        self.character_sheet_manager.width,
                        self.character_sheet_manager.row_one_height,
                    ),
                    5,
                )
            case self.character_sheet_manager.co_portrait:
                pygame.draw.rect(
                    DISPLAY_SURF,
                    gc.TEXT_COLOR,
                    pygame.Rect(
                        self.character_sheet_manager.column_two_x, 
                        self.character_sheet_manager.row_two_y, 
                        self.character_sheet_manager.width, 
                        100
                    ),
                    5,
                )
            case self.character_sheet_manager.co_spells:
                pygame.draw.rect(
                    DISPLAY_SURF,
                    gc.TEXT_COLOR,
                    pygame.Rect(
                        self.character_sheet_manager.column_two_x,
                        self.character_sheet_manager.row_one_y,
                        self.character_sheet_manager.width,
                        self.character_sheet_manager.row_one_height,
                    ),
                    5,
                )
            case self.character_sheet_manager.co_abilities:
                pygame.draw.rect(
                    DISPLAY_SURF,
                    gc.TEXT_COLOR,
                    pygame.Rect(
                        self.character_sheet_manager.column_one_x, 
                        self.character_sheet_manager.row_two_y, 
                        self.character_sheet_manager.width, 
                        200
                    ),
                    5,
                )

    def draw(self, DISPLAY_SURF):
        text = f"{self.character_sheet_manager.current_state.name = } \n {self.character_sheet_manager.cursor_index = } \n "
        # for state in self.character_sheet_manager.list_of_submenus:
        #     text += f"{state.name} \n "
        th.make_text(
            DISPLAY_SURF,
            gc.BGCOLOR,
            10, # Fiddle with these constants (left / top / width) later
            10,
            800,
            th.bdlr(text),
        )