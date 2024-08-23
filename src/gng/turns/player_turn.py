from statemachine import StateMachine, State

class CannotActHere(Exception):
    pass

class PlayerTurn(StateMachine):
    can_move_and_act = State(initial=True)
    can_move = State()
    can_act = State()
    end_turn = State(final=True)

    to_can_move = (can_move_and_act.to(can_move) 
        | can_move.to(can_move))
    to_can_act = can_move_and_act.to(can_act)
    to_can_move_and_act = (can_move_and_act.to(can_move_and_act)
        | can_move.to(can_move_and_act))
    to_end_turn = (can_move_and_act.to(end_turn)
        | can_move.to(end_turn)
        | can_act.to(end_turn))

    def no_more_movement(self):
        pass

    def act(self):
        match self.current_state:
            case self.can_move_and_act:
                self.send("to_can_move")
            case self.can_act:
                self.send("end_turn")
            case self.end_turn | self.can_move:
                raise CannotActHere(
                    "You are in a state that doesn't allow acting."
                )



    # ------------------------------------------------------------------

    def __init__(self, player):
        self.player = player
        self.movement_spent = 0
        super().__init__()