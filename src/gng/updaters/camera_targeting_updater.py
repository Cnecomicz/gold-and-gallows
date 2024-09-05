class CameraTargetingUpdater:
    def __init__(self, camera_target, thing_to_target):
        self.camera_target = camera_target
        self.thing_to_target = thing_to_target

    def update(self):
        self.camera_target.x = self.thing_to_target.x
        self.camera_target.y = self.thing_to_target.y