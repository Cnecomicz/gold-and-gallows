import gng.listeners.listener as l

class CharacterCreatorListener(l.Listener):
    def __init__(self, spoken_queue, end_character_creation):
        self.spoken_queue = spoken_queue
        self.end_character_creation = end_character_creation
        super().__init__(self.spoken_queue)
        self.register_speech(
            "Finished character creation",
            self.end_character_creation
        )