import gng.listeners.listener as l

class PlayerControlsEventHandlerListener(l.Listener):
    def __init__(self, spoken_queue, begin_dialogue):
        self.spoken_queue = spoken_queue
        self.begin_dialogue = begin_dialogue
        super().__init__(self.spoken_queue)
        self.register_speech(
            "Go to dialogue state",
            self.begin_dialogue
        )