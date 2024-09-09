class DebuggingManager:
    def __init__(self):
        self.debugging_text = "" 
        self.debugging_flag = False

    def flip_debugging_flag(self):
        self.debugging_flag = not self.debugging_flag