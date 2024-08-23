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
	flexmock(player).should_receive("roll_initiative").once()
	turns_manager = TurnsManager(player, [], [potato])


def test_if_player_succeeds_on_initiative_roll_then_they_go_first():
	player = create_test_player()
	potato = create_test_potato()
	flexmock(player).should_receive("roll_initiative").and_return(True).once()
	turns_manager = TurnsManager(player, [], [potato])
	turns_manager.send("begin") # TODO: this should happen automatically
	assert turns_manager.current_actor == player

def test_once_the_turn_is_over_the_next_actor_goes():
	player = create_test_player()
	potato = create_test_potato()
	flexmock(player).should_receive("roll_initiative").and_return(True).once()
	turns_manager = TurnsManager(player, [], [potato])
	turns_manager.send("begin") # TODO: this should happen automatically
	turns_manager.send("next_turn") # TODO: this should happen automatically
	assert turns_manager.current_actor == potato




