

class DebuggingManager:
    def __init__(
        self, 
        FPS_CLOCK,
        gameplay_state_machine_manager,
        player,
    ):
        # The inputs of the DebuggingManager will change as our needs to
        # track various values change. Go to debugging_updater.py
        self.FPS_CLOCK = FPS_CLOCK
        self.gameplay_state_machine_manager = gameplay_state_machine_manager
        self.player = player
        self.debugging_text = "" 
        self.debugging_flag = False

    def flip_debugging_flag(self):
        self.debugging_flag = not self.debugging_flag