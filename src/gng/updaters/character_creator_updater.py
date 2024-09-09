class CharacterCreatorUpdater:
    def __init__(self, character_creator, gameplay_state_machine_manager):
        self.character_creator = character_creator
        self.gameplay_state_machine_manager = gameplay_state_machine_manager

    def update(self):
        if self.character_creator.current_state == self.character_creator.choosing_name:
            if hasattr(self.character_creator.player, "name"):
                    self.gameplay_state_machine_manager.send("end_character_creation")