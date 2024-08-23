from statemachine import StateMachine, State

import gng.turns.player_turn as pt
import gng.turns.npc_turn    as nt

class TurnsManager(StateMachine):
    roll_initiative = State(initial=True)
    turn = State()
    not_in_combat = State(final=True)

    begin = roll_initiative.to(turn)
    next_turn = turn.to(turn)
    end = turn.to(not_in_combat)

    def on_enter_roll_initiative(self, event, state):
        # Start by putting all NPCs in the turn order.
        self.turn_order_list = self.other_npcs_list.copy()
        for character in self.party_list:
            if character.roll_initiative():
                # If you pass your initiative roll, you go before NPCs.
                self.turn_order_list.insert(0, character)
            else:
                # Else, you go after NPCs.
                self.turn_order_list.append(character)

    def on_enter_turn(self, event, state):
        current_actor = self.turn_order_list[self.current_turn_index]
        if current_actor == self.player:
            player_turn_fsm = pt.PlayerTurn(current_actor)
        else:
            npc_turn_fsm = nt.NPCTurn(current_actor)

    def on_exit_turn(self, event, state):
        self.current_turn_index = \
            (self.current_turn_index + 1) % self.number_of_actors


    def on_enter_not_in_combat(self, event, state):
        self.party_list = []
        self.other_npcs_list = []
        self.turn_order_list = []



    # ------------------------------------------------------------------
    def __init__(self, player, other_party_list, other_npcs_list):
        self.player = player
        self.party_list = [player] + other_party_list
        self.other_npcs_list = other_npcs_list
        self.turn_order_list = []
        self.current_turn_index = 0
        self.number_of_actors = \
            len(self.party_list) + len(self.other_npcs_list)
        super().__init__()

    def handle_pygame_events(self, pygame_event):
        pass

    def update(self):
        pass

    def draw(self):
        pass




