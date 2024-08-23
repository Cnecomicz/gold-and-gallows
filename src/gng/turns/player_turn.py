from statemachine import StateMachine, State

class PlayerTurn(StateMachine):
    awaiting_input = State(initial=True)
    handling_movement = State()
    handling_action = State()
    end_turn = State(final=True)

    move = awaiting_input.to(handling_movement)
    act = awaiting_input.to(handling_action)
    stop_move = handling_movement.to(awaiting_input)
    done = (awaiting_input.to(end_turn)
        | handling_movement.to(end_turn)
        | handling_action.to(end_turn))

    def on_exit_handling_action(self, event, state):
        self.can_act = False

    # ------------------------------------------------------------------

    def __init__(self, player):
        self.player = player
        self.movement_spent = 0
        self.can_move = True
        self.can_act = True
        super().__init__()