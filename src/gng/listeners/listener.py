class DuplicateSpeechError(Exception):
    pass

class NoSuchSpeech(Exception):
    pass

class Listener:
    def __init__(self, spoken_queue):
        self.spoken_queue = spoken_queue
        self.dict_of_actions = {}

    def register_speech(self, speech, method):
        if speech in self.dict_of_actions:
            raise DuplicateSpeechError(
                f"Tried to give a second method for speech({speech})"
            )
        self.dict_of_actions[speech] = method

    def listen(self):
        for speech in self.spoken_queue:
            if (method := self.dict_of_actions.get(speech)) is not None:
                method()
                self.spoken_queue.remove(speech)
            else:
                raise NoSuchSpeech(
                    "You haven't yet written code for the listener to " \
                    "respond to that speech. (Check if you made a typo!)"
                )