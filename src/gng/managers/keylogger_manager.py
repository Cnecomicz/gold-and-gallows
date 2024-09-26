class KeyloggerManager:
    def __init__(
        self, instance, attribute, finite_state_machine, event_string
    ):
        self.user_string = ""
        self.instance = instance
        self.attribute = attribute
        # self.instance is an instance that has the attribute 
        # self.attribute of type string to which you intend to assign 
        # self.user_string.
        self.finite_state_machine = finite_state_machine
        self.event_string = event_string
        # When the assignment occurs, we also send the self.event_string
        # to the self.finite_state_machine.


    def set_user_string(self):
        setattr(self.instance, self.attribute, self.user_string)
        self.finite_state_machine.send(self.event_string)