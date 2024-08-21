from statemachine import StateMachine, State

import gng.global_constants as gc

class TurnsManager(StateMachine):
    roll_initiative = State(initial=True)
    player_turn = State()
    npc_turn = State()
    not_in_combat = State()

    # TODO: FIXME
    cycle = (roll_initiative.to(player_turn) 
        | player_turn.to(npc_turn) 
        | npc_turn.to(not_in_combat) 
        | not_in_combat.to(roll_initiative))

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

    def on_enter_not_in_combat(self, event, state):
        self.party_list = []
        self.other_npcs_list = []
        self.turn_order_list = []



    # ------------------------------------------------------------------
    def __init__(self, party_list, other_npcs_list):
        self.party_list = party_list
        self.other_npcs_list = other_npcs_list
        self.turn_order_list = []
        super().__init__()

    def handle_pygame_events(self, pygame_event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

