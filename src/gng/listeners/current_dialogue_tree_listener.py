import gng.listeners.listener as l

class CurrentDialogueTreeListener(l.Listener):
    def __init__(self, spoken_queue, end_dialogue):
        self.spoken_queue = spoken_queue
        self.end_dialogue = end_dialogue
        super().__init__(self.spoken_queue)
        self.register_speech(
            "Ending dialogue",
            self.end_dialogue
        )