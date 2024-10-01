from statemachine import StateMachine, State

import gng.global_constants as gc


class PlayerTurn(StateMachine):
    awaiting_input = State(initial=True)
    handling_movement = State()
    handling_action = State()
    end_turn = State(final=True)

    move = awaiting_input.to(handling_movement, cond="can_move")
    act = awaiting_input.to(handling_action, cond="can_act")
    stop_move = handling_movement.to(awaiting_input)
    stop_act = handling_action.to(awaiting_input)
    done = (
        awaiting_input.to(end_turn)
        | handling_movement.to(end_turn)
        | handling_action.to(end_turn)
    )

    # def on_stop_move(self, event, state):
    #     if self.movement_spent >= self.player.movement_allotment:
    #         self.can_move = False

    def on_exit_handling_action(self, event, state):
        self.can_act = False

    # ------------------------------------------------------------------

    def __init__(self, player):
        self.player = player
        self.movement_spent = 0
        self.can_move = True
        self.can_act = True
        super().__init__()

    def check_if_movement_remains(self):
        if self.movement_spent >= self.player.movement_allotment:
            self.can_move = False
            self.send("stop_move")

    def handle_pygame_events(self, pygame_event):
        if pygame_event.type == gc.KEYDOWN:
            match self.current_state:
                case self.awaiting_input:
                    pass
                case self.handling_movement:
                    if pygame_event.key in (gc.UP + gc.DOWN + gc.LEFT + gc.RIGHT):
                        # TODO: player movement
                        self.check_if_movement_remains()
                case self.handling_action:
                    pass
                case self.end_turn:
                    pass

    def update(self):
        pass

    def draw(self):
        pass

    # def tracking_movement(self):
    #     distance = delta(player_last_frame, player_this_frame)
    #     self.movement_spent += distance

    #     # player.movement_allotment is like 300 or something
