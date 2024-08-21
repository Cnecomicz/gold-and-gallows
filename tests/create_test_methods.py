from gng.entities_and_components import (
    create_item,
    create_player,
    create_npc,
    give_damage_dealing_component,
)

def create_test_player():
    return create_player(
        name="player",
        CHA=20,
        CON=20,
        DEX=20,
        INT=20,
        STR=20,
        WIS=20,
        max_HP=10,
        AC=10,
        AV=10,
    )


def create_test_potato():
    return create_npc(
        name="potato", 
        x=10, y=10, 
        width=30, height=30, 
        HD=3, 
        dialogue_tree=None
    )


def create_test_sword():
    sword = create_item(
        "sword", 
        equippable=True, slot="held_slot", 
        number_of_dice=1, damage_die=4, AC_value=0
    )
    give_damage_dealing_component(sword, number_of_dice=1, damage_die=4)
    return sword


def create_test_shield():
    return create_item(
        "shield", 
        equippable=True, slot="held_slot", 
        number_of_dice=0, damage_die=0, AC_value=1
    )


def create_test_lava():
    return create_item("lava", equippable=False)