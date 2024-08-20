from flexmock import flexmock
import pytest

import gng.dice_roller as dr
import gng.global_constants as gc
import gng.DialogueTrees.guy1_dialogue_tree

from gng.entities_and_components import (
    NoSlotDefined,
    NotEquippable,
    UnreachableDialogue,
    Entity,
    create_item,
    create_player,
    create_npc,
    give_item_component,
    give_world_map_component,
    give_dialogue_component,
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
        name="potato", x=10, y=10, width=30, height=30, HD=42, dialogue_tree=None
    )


def create_test_sword():
    sword = create_item(
        "sword", equippable=True, slot="held_slot", damage_die=4, AC_value=0
    )
    give_damage_dealing_component(sword, 4)
    return sword


def create_test_shield():
    return create_item(
        "shield", equippable=True, slot="held_slot", damage_die=0, AC_value=1
    )


def create_test_lava():
    return create_item("lava", equippable=False)


def test_creating_sword_player_potato():
    sword = create_test_sword()
    player = create_test_player()
    potato = create_test_potato()


def test_sword_can_be_equipped():
    sword = create_test_sword()
    player = create_test_player()
    player.equip(sword)
    assert sword in player.held_slot


def test_sword_deals_damage():
    sword = create_test_sword()
    potato = create_test_potato()
    starting_HP = potato.HP
    sword.damages(potato)
    resulting_HP = potato.HP
    assert resulting_HP < starting_HP


def test_flexmock_sword_deals_max_damage():
    sword = create_test_sword()
    potato = create_test_potato()
    starting_HP = potato.HP
    flexmock(dr).should_receive("roll_x_d_n").and_return(4).once()
    sword.damages(potato)
    resulting_HP = potato.HP
    assert resulting_HP == starting_HP - 4


def test_player_attacks_potato():
    player = create_test_player()
    fake_sword = flexmock(create_test_sword())
    potato = create_test_potato()
    fake_sword.should_receive("damages").with_args(potato).once()
    flexmock(dr).should_receive("thread_the_needle").and_return(True)
    player.equip(fake_sword)
    player.attacks(potato)


# Error handling -------------------------------------------------------


def test_entities_without_equip_method_cannot_equip_an_item():
    sword = create_test_sword()
    shield = create_test_shield()
    with pytest.raises(AttributeError):
        sword.equip(shield)


def test_you_cannot_equip_nonequippable_items():
    player = create_test_player()
    lava = create_test_lava()
    with pytest.raises(NotEquippable):
        player.equip(lava)


def test_you_cannot_create_equippable_items_without_assigning_a_slot():
    bad_item = Entity()
    with pytest.raises(NoSlotDefined):
        give_item_component(bad_item, equippable=True, slot="")


def test_you_should_not_give_dialogue_trees_to_noninteractable_entities():
    ghost = Entity()
    give_world_map_component(ghost, 0, 0, 0, 0, gc.WHITE, interactable=False)
    with pytest.raises(UnreachableDialogue):
        give_dialogue_component(ghost, gng.DialogueTrees.guy1_dialogue_tree.guy1dt)
