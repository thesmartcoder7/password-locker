
class User:

    user_accounts = []

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.accounts = []

    def add_user(self):
        User.user_accounts.append(self)


class Credentials:

    accounts = []

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def add_account(self):
        Credentials.accounts.append(self)
