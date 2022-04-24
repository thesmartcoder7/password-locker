
class User:
    """
    this is a class that allows the program to generate objects of type User
    """

    user_accounts = []

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.accounts = []

    def add_user(self):
        """
        this function basically adds a new user in to the user accounts array
        :return: it returns nothing as it just executes
        """
        User.user_accounts.append(self)

    def show_accounts(self):
        """
        this is responsible for fetching all the use accounts and displaying them for the user to see
        :param self: the user parameter in this context refers to an individual object
        :return: this function does not return anything, it just does its work
        """

        if len(self.accounts) == 0:
            print("\n - - - You have not added any accounts yet - - - ")
        else:
            for account in self.accounts:
                print(f"\n - - - {account.name.title()} Credentials - - - ")
                print(f"username: {account.username}")
                print(f"password: {account.password}")

    def delete_account(self, account):
        for item in self.accounts:
            if account.name == item.name:
                self.accounts.remove(account)

    @staticmethod
    def user_login(name, password):
        """
        This function is responsible for taking in use login details and validating them for a proper login.
        :return: it returns an array with two items. A boolean and a value. The boolean is what determines if the
                 user gets to try again or get into their account details
        """
        for user in User.user_accounts:
            if name == user.username and password == user.password:
                return [True, user]
            else:
                return [False, "sam"]


class Credentials:

    """
    this is a class that allows the program to generate objects of type Credentials
    """

    accounts = []

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def add_account(self):
        Credentials.accounts.append(self)
