from flexmock import flexmock
import pytest

import gng.entities_and_components as ec

from gng.turns_manager import (TurnsManager)

from .create_test_methods import (
    create_test_player,
    create_test_potato
)

def test_when_combat_begins_initiative_is_rolled_and_success_means_player_starts():
	player = create_test_player()
	potato = create_test_potato()
	flexmock(player).should_receive("roll_initiative").and_return(True).once()
	turns_manager = TurnsManager([player], [])
	assert turns_manager.turn_order_list[0] == player


def test_if_player_succeeds_on_initiative_roll_then_they_go_first():
	pass

def test_when_your_turn_begins_you_can_move_or_act():
	pass

def test_once_you_have_acted_you_cannot_act_again():
	pass


# def test_you_can_move_then_act_then_finish_moving():
# 	player = create_test_player()
# 	potato = create_test_potato()
# 	turns_manager = TurnsManager(player, potato)
# 	# Player passes initiative and goes first
# 	flexmock(dr).should_receive("roll_below").and_return(True)

