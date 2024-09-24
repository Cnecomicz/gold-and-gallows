from flexmock import flexmock
import pytest

import gng.functions.dice_roller as dr
import gng.global_constants as gc
import gng.dialogue_trees.guy1_dialogue_tree

from tests.create_test_methods import (
    create_test_player,
    create_test_potato,
    create_test_sword,
    create_test_shield,
    create_test_lava
)

from gng.entities_and_components import (
    NoSlotDefined,
    NoSuchHD,
    NotEquippable,
    UnreachableDialogue,
    Entity,
    convert_HD_to_default_damage,
    create_item,
    create_player,
    create_npc,
    give_item_component,
    give_world_map_component,
    give_dialogue_component,
    give_damage_dealing_component,
)


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
    # Succeed on your roll to hit the enemy:
    flexmock(dr).should_receive("thread_the_needle").and_return(True)
    player.equip(fake_sword)
    player.attacks(potato)

def test_HD_are_converted_to_damage_dice():
    assert convert_HD_to_default_damage(3) == (1, 8)

def test_player_gets_attacked_by_potato():
    player = create_test_player()
    starting_HP = player.HP
    potato = create_test_potato()
    assert hasattr(potato, "default_weapon")
    # Fail on your roll to be damaged by the enemy:
    flexmock(dr).should_receive("thread_the_needle").with_args(3,10).and_return(False)
    player.gets_attacked_by(potato)
    resulting_HP = player.HP
    assert starting_HP > resulting_HP





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
    fake_gsmm = flexmock()
    with pytest.raises(UnreachableDialogue):
        give_dialogue_component(ghost, gng.dialogue_trees.guy1_dialogue_tree.Guy1DialogueTree(fake_gsmm))

def test_NoSuchHD():
    with pytest.raises(NoSuchHD):
        convert_HD_to_default_damage(19) # HD are <= 17
    with pytest.raises(NoSuchHD):
        convert_HD_to_default_damage("Z") # HD are int
    with pytest.raises(NoSuchHD):
        convert_HD_to_default_damage(4.5) # HD are not avg_health
