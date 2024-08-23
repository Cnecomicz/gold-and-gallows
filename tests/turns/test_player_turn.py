from flexmock import flexmock
import pytest

from statemachine import StateMachine

from gng.turns.player_turn import (PlayerTurn)

from tests.create_test_methods import (
    create_test_player,
    create_test_potato,
)


def test_when_your_turn_begins_you_can_move_and_act():
    player = create_test_player()
    player_turn_fsm = PlayerTurn(player)
    assert player_turn_fsm.can_move and player_turn_fsm.can_act

def test_once_you_have_acted_you_cannot_act_again():
    player = create_test_player()
    player_turn_fsm = PlayerTurn(player)
    player_turn_fsm.send("act")
    player_turn_fsm.send("stop_act")
    with pytest.raises(StateMachine.TransitionNotAllowed):
        player_turn_fsm.send("act")


def test_if_you_have_moved_less_than_your_allotted_amount_you_can_move_again():
    player = create_test_player()
    player_turn_fsm = PlayerTurn(player)
    player_turn_fsm.send("move")
    player_turn_fsm.movement_spent = player.movement_allotment - 1
    player_turn_fsm.send("stop_move")
    player_turn_fsm.send("move")

def test_if_you_move_your_alloted_amount_you_cannot_move_again():
    player = create_test_player()
    player_turn_fsm = PlayerTurn(player)
    player_turn_fsm.send("move")
    player_turn_fsm.movement_spent = player.movement_allotment
    player_turn_fsm.update()
    with pytest.raises(StateMachine.TransitionNotAllowed):
        player_turn_fsm.send("move")



