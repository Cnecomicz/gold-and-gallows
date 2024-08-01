from statemachine import StateMachine, State

class GameplayStateMachine(StateMachine):
	overworld = State(initial=True)
	dialogue  = State()
	turns     = State() 

	to_overworld = (turns.to(overworld) | dialogue.to(overworld))
	to_dialogue  = (turns.to(dialogue)  | overworld.to(dialogue))
	to_turns     = (dialogue.to(turns)  | overworld.to(turns)   )

