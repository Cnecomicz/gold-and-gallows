from flexmock import flexmock
import pytest

from gng.turns.turns_manager import (TurnsManager)

from tests.create_test_methods import (
    create_test_player,
    create_test_potato,
)

def test_when_combat_begins_initiative_is_rolled():
	player = create_test_player()
	potato = create_test_potato()
	turns_manager = TurnsManager(player, [], [potato])


def test_if_player_succeeds_on_initiative_roll_then_they_go_first():
	player = create_test_player()
	potato = create_test_potato()
	flexmock(player).should_receive("roll_initiative").and_return(True).once()
	turns_manager = TurnsManager(player, [], [potato])
	assert turns_manager.turn_order_list[0] == player




# def test_you_can_move_then_act_then_finish_moving():
# 	player = create_test_player()
# 	potato = create_test_potato()
# 	turns_manager = TurnsManager(player, potato)
# 	# Player passes initiative and goes first
# 	flexmock(dr).should_receive("roll_below").and_return(True)

