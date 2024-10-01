class DebuggingUpdater:
    def __init__(
        self,
        debugging_manager,
        FPS_CLOCK,
        gameplay_state_machine_manager,
        player,
        character_sheet_manager,
    ):
        # The inputs of the DebuggingUpdater will change as our need to
        # track various values changes.
        self.debugging_manager = debugging_manager
        self.FPS_CLOCK = FPS_CLOCK
        self.gameplay_state_machine_manager = gameplay_state_machine_manager
        self.player = player
        self.character_sheet_manager = character_sheet_manager

    def update(self):
        self.debugging_manager.debugging_text = (
            f"{self.FPS_CLOCK.get_fps() = } \n "
            f"{self.gameplay_state_machine_manager.current_state.name = } \n "
            f"{self.player.inventory = } \n "
            f"{self.character_sheet_manager.current_state.name = } \n "
        )
