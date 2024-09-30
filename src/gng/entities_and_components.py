from functools import partial

import gng.functions.dice_roller as dr
import gng.global_constants as gc


class NoSlotDefined(Exception):
    pass


class NotEquippable(Exception):
    pass


class UnreachableDialogue(Exception):
    pass


class NoSuchHD(Exception):
    pass


# ----------------------------------------------------------------------

# This code lets us define an indeterminate amount of components when we
# instantiate an object of Entity. You can also add new components to an
# Entity after creation by simply declaring them (e.g., Bob.x = 5 makes
# Bob have an attribute of x with value 5 _even if_ Bob previously did
# not have an attribute of x.


class Entity:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "<entity(id=%s, name='%s')>" % (hex(id(self)), self.name)


def create_item(name, equippable=False, slot="", number_of_dice=0, damage_die=0, AC_value=0):
    entity = Entity()
    give_name_component(entity, name)
    give_item_component(entity, equippable, slot, number_of_dice, damage_die, AC_value)
    return entity


def create_player(name, CHA, CON, DEX, INT, STR, WIS, max_HP, AC, AV):
    entity = Entity()
    give_name_component(entity, name)
    give_equipment_component(entity)
    give_world_map_component(
        entity,
        x=0,
        y=0,
        width=30,
        height=30,
        color=gc.BLUE,
        visible_on_world_map=True,
        interactable=False,
    )
    give_player_stats_component(entity, CHA, CON, DEX, INT, STR, WIS, max_HP, AC, AV)
    give_moveable_component(entity, speed=4, movement_allotment=300)
    give_level_component(entity, level=1)
    return entity


def create_npc(name, x, y, width, height, HD, dialogue_tree):
    entity = Entity()
    give_name_component(entity, name)
    give_moveable_component(entity, speed=4, movement_allotment=300)
    give_equipment_component(entity)
    give_world_map_component(entity, x, y, width, height, color=gc.GREEN)
    give_HD_component(entity, HD)
    give_dialogue_component(entity, dialogue_tree)
    return entity


# ----------------------------------------------------------------------

def convert_HD_to_default_damage(HD):
    """Input: an int representing monster HD. 
    Output: (int, int) corresponding to 
    gc.MONSTER_HP_AND_DAMAGE_LIST_OF_DICT"""
    for dictionary in gc.MONSTER_HP_AND_DAMAGE_LIST_OF_DICT:
        if dictionary["hit_die"] == HD:
            return dictionary["number_of_damage_dice"], \
            dictionary["type_of_damage_dice"]
    raise NoSuchHD(f"The inputted HD {HD} was not found in the JSON.")


    



def create_default_weapon(entity, number_of_dice=1, damage_die=1):
    default_weapon = Entity()
    give_damage_dealing_component(default_weapon, number_of_dice, damage_die)
    entity.default_weapon = default_weapon


def give_world_map_component(
    entity, x, y, width, height, color, visible_on_world_map=True, interactable=True
):
    entity.x = x
    entity.y = y
    entity.width = width
    entity.height = height
    entity.color = color
    entity.rect = gc.pygame.Rect(x, y, width, height)
    entity.visible_on_world_map = visible_on_world_map
    entity.interactable = interactable


def give_item_component(
    entity,
    equippable=False,
    slot="",
    number_of_dice=0,
    damage_die=0,
    AC_value=0,
):
    if equippable and slot == "":
        raise NoSlotDefined("An equippable item must have a slot.")
    entity.equippable = equippable
    entity.slot = slot
    entity.damage_die = damage_die
    entity.AC_value = AC_value


def give_name_component(entity, name):
    entity.name = name


def give_equipment_component(
    entity,
    inventory=None,
    held_slot=None,  # Max size: number_of_arms
    glove_slot=None,  # Max size: number_of_arms
    number_of_arms=2,
    head_slot=None,  # Max size: number_of_heads
    necklace_slot=None,  # Max size: number_of_heads
    number_of_heads=1,
    boot_slot=None,  # Max size: number_of_legs
    number_of_legs=2,
    ring_slot=None,  # Max size: number_of_fingers
    number_of_fingers_on_a_hand=5,
    armor_slot=None,  # Max size: number_of_torsos
    back_slot=None,  # Max size: number_of_torsos
    number_of_torsos=1,
):
    entity.inventory = inventory or []
    entity.held_slot = held_slot or []
    entity.glove_slot = glove_slot or []
    entity.number_of_arms = number_of_arms
    entity.head_slot = head_slot or []
    entity.necklace_slot = necklace_slot or []
    entity.number_of_heads = number_of_heads
    entity.boot_slot = boot_slot or []
    entity.number_of_legs = number_of_legs
    entity.ring_slot = ring_slot or []
    entity.number_of_fingers_on_a_hand = number_of_fingers_on_a_hand
    entity.armor_slot = armor_slot or []
    entity.back_slot = back_slot or []
    entity.number_of_torsos = number_of_torsos

    def equip(self, item):
        if item.equippable:
            slot_string = item.slot
            slot_list = getattr(self, slot_string)
            slot_list.append(item)
        else:
            raise NotEquippable("That item is not equippable.")

    entity.equip = partial(equip, entity)


def give_dialogue_component(entity, dialogue_tree):
    if not entity.interactable:
        raise UnreachableDialogue(
            "An entity with a dialogue tree that "
            "can't be interacted with will never display its dialogue."
        )
    entity.dt = dialogue_tree


def give_moveable_component(entity, speed, movement_allotment):
    entity.speed = speed
    entity.movement_allotment = movement_allotment


def give_player_stats_component(entity, CHA, CON, DEX, INT, STR, WIS, max_HP, AC, AV):
    entity.CHA = CHA
    entity.CON = CON
    entity.DEX = DEX
    entity.INT = INT
    entity.STR = STR
    entity.WIS = WIS
    entity.max_HP = max_HP
    entity.HP = entity.max_HP
    entity.AC = AC
    entity.AV = AV

    def attacks(self, enemy):
        weapon = entity.held_slot[0]  # TODO: how do I reconcile multiple or no weapons?
        if dr.thread_the_needle(enemy.HD, entity.AV):
            weapon.damages(enemy)

    entity.attacks = partial(attacks, entity)

    def gets_attacked_by(self, enemy):
        if not dr.thread_the_needle(enemy.HD, entity.AC):
            enemy.default_weapon.damages(self) # TODO: add logic for if the enemy uses a non default weapon

    entity.gets_attacked_by = partial(gets_attacked_by, entity)

    def roll_initiative(self):
        return dr.roll_below(self.DEX)

    entity.roll_initiative = partial(roll_initiative, entity)


def give_level_component(entity, level):
    entity.level = level


def give_HD_component(entity, HD):
    entity.HD = HD
    # By defining a HD (hit die), you can derive all other values. They
    # can be overridden on a case-by-case basis when desired.
    entity.max_HP = round(entity.HD * gc.AVERAGE_HP_PER_HD)
    entity.HP = entity.max_HP
    create_default_weapon(entity)




def give_damage_dealing_component(entity, number_of_dice, damage_die):
    entity.damage_die = damage_die
    entity.number_of_dice = number_of_dice

    def damages(self, entity):
        damage_roll = dr.roll(f"{self.number_of_dice}d{self.damage_die}")
        entity.HP -= damage_roll

    entity.damages = partial(damages, entity)
