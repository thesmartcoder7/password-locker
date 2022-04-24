
class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.accounts = []


class Credentials:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
