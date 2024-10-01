from statemachine import StateMachine, State


class NPCTurn(StateMachine):
    todo = State(initial=True)

    to_todo = todo.to(todo)

    def __init__(self, npc):
        self.npc = npc
        super().__init__()
