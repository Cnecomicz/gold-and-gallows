class KeyloggerManager:
    def __init__(self, instance, attribute):
        self.user_string = ""
        self.instance = instance
        self.attribute = attribute
        # self.instance is an instance that has the attribute 
        # self.attribute of type string to which you intend to assign 
        # self.user_string.
        

    def set_user_string(self):
        setattr(self.instance, self.attribute, self.user_string)