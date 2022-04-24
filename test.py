import unittest
# import main
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
        self.assertEqual(self.test_user.first_name, "samuel")
        self.assertEqual(self.test_user.last_name, "martins")
        self.assertEqual(self.test_user.username, "sammy")
        self.assertEqual(self.test_user.password, "smart-code")


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
        self.assertEqual(self.test_account.name, "twitter")
        self.assertEqual(self.test_account.username, "twitterboy")
        self.assertEqual(self.test_account.password, "twitterboyrocks!")


if __name__ == "__main__":
    unittest.main()
