from gng.listeners.listener import Listener#, NoSuchSpeech



class Setup:
    def __init__(self):
        self.value = 0

    def set_value_to_one(self):
        self.value = 1

def test_registering_a_method_for_a_given_speech():
    setup = Setup()
    assert setup.value == 0
    listener = Listener(["phrase"])
    listener.register_speech("phrase", setup.set_value_to_one)
    listener.listen()
    assert setup.value == 1
