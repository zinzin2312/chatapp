import uuid


class User:
    def __init__(self):
        self.ID = str(uuid.uuid4())
        self.name = "Anonymous"

    def change_name(self, name):
        self.name = name


