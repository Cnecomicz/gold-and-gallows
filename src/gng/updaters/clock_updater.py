class ClockUpdater:
    def __init__(self, clock_manager):
        self.clock_manager = clock_manager

    def update(self):
        self.clock_manager.ticks_passed += 1