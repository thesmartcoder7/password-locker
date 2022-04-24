import unittest
from user_details import User, Credentials


class TestUser(unittest.TestCase):
    """
    this is a test class that defines test cases for the User class behaviours
    """

    def setUp(self):
        """
        this runs before each of the test cases
        :return: this method does not return anything
        """
        self.test_user = User("samuel", "martins", "sammy", "smart-code")

    def test_init(self):
        """
        this method tests if the initialization of the user has been successful
        :return: this method does not return anything
        """
        self.assertEqual(self.test_user.first_name, "samuel")
        self.assertEqual(self.test_user.last_name, "martins")
        self.assertEqual(self.test_user.username, "sammy")
        self.assertEqual(self.test_user.password, "smart-code")

    def test_add_user(self):
        """
        this method tests if the functionality for user creation is successful
        :return: this method does not return anything
        """
        self.test_user.add_user()
        self.assertEqual(len(User.user_accounts), 1)

    def test_show_accounts(self):
        """
        this method tests the functionality of displaying all the accounts and credentials the user has
        :return: this method does not return any value at all
        """
        self.assertEqual(self.test_user.accounts, [])

    def test_user_login(self):
        """
        this method test if the user trying to log into the application exists in the application
        :return:
        """
        self.assertEqual(User.user_login(self.test_user.username, self.test_user.password)[0], True)
        self.assertEqual(
            User.user_login(self.test_user.username, self.test_user.password)[1].username,
            self.test_user.username
        )

    def test_delete_account(self):
        self.test_user.accounts.append(Credentials("twitter", "twitterboy", "twitterboyrocks!"))
        self.test_user.delete_account(self.test_user.accounts[0])
        self.assertEqual(len(self.test_user.accounts), 0)


class TestCredentials(unittest.TestCase):
    """
    this is a test class that defines test cases for the Credentials class behaviours
    """

    def setUp(self):
        """
        this runs before each of the test cases
        :return: this method does not return anything
        """
        self.test_account = Credentials("twitter", "twitterboy", "twitterboyrocks!")

    def test_init(self):
        """
        this method tests if the initialization of the account has been successful
        :return: this method does not return anything
        """
        self.assertEqual(self.test_account.name, "twitter")
        self.assertEqual(self.test_account.username, "twitterboy")
        self.assertEqual(self.test_account.password, "twitterboyrocks!")

    def test_add_account(self):
        """
        this method tests if the functionality for user creation is successful
        :return: this method does not return anything
        """
        self.test_account.add_account()
        self.assertEqual(len(Credentials.accounts), 1)


if __name__ == "__main__":
    unittest.main()
