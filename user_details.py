
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

    def show_accounts(self):
        """
        this is responsible for fetching all the use accounts and displaying them for the user to see
        :param self: the user parameter in this context refers to an individual object
        :return: this function does not return anything, it just does its work
        """
        for account in self.accounts:
            print(f"\n - - - {account.name.title()} Credentials - - - ")
            print(f"username: {account.username}")
            print(f"password: {account.password}")


class Credentials:

    accounts = []

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def add_account(self):
        Credentials.accounts.append(self)
