

class DebuggingManager:
    def __init__(self, dict_of_things_to_track):
        self.dict_of_things_to_track = dict_of_things_to_track
        self.debugging_text = f""
        for name, thing in self.dict_of_things_to_track.items():
            self.debugging_text += f"{name} = {thing} \n "
        self.debugging_flag = False

    def flip_debugging_flag(self):
        self.debugging_flag = not self.debugging_flag