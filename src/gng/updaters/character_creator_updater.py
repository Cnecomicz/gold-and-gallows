class CharacterCreatorUpdater:
    def __init__(self, character_creator):
        self.character_creator = character_creator

    def update(self):
        if self.character_creator.current_state == self.character_creator.choosing_name:
            if hasattr(self.character_creator.player, "name"):
                    self.character_creator.spoken_queue.append("Finished character creation")