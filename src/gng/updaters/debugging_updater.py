class DebuggingUpdater:
    def __init__(self, debugging_manager):
        self.debugging_manager = debugging_manager

    def update(self):
        self.debugging_manager.debugging_text = \
            f"{self.debugging_manager.FPS_CLOCK.get_fps() = } \n " \
            f"{self.debugging_manager.gameplay_state_machine_manager.current_state = } \n " \
            f"{self.debugging_manager.player.inventory = } \n " 