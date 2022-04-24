from user_details import User, Account
import random

user_accounts = []
characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']


def generate_password():
    """
    this function is responsible for generating a 21 character random, secure password
    :return: it returns the randomly generated password to the function that calls it
    """
    r_letters = [random.choice(characters) for _ in range(7)]
    r_numbers = [random.choice(numbers) for _ in range(7)]
    r_symbols = [random.choice(symbols) for _ in range(7)]
    gen_password = r_letters + r_numbers + r_symbols
    random.shuffle(gen_password)
    generated_password = "".join(gen_password)
    return generated_password


def create_user_account():
    """
    this function is  responsible for taking in user details and using them to create a user account
    :return: It does not return any value. It just executes.
    """
    print("\n - - - signup - - - ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    user_name = input("Enter your desired username: ")
    user_password = input("Enter your desired password: ")

    user_name = User(first_name, last_name, user_name, user_password)

    if user_name not in user_accounts:
        user_accounts.append(user_name)
        print("\n - - - Account successfully created! - - - ")
    else:
        print("That username is already taken!")
        create_user_account()


def login():
    """
    This function is responsible for taking in use login details and validating them for a proper login.
    :return:
    """
    print("\n - - - login - - - ")
    login_name = input("Enter your username: ")
    login_password = input("Enter your password: ")
    successful_user = "sam"
    logged_in = False
    for user in user_accounts:
        if login_name == user.username and login_password == user.password:
            successful_user = user
            logged_in = True
            print(f"\n - - - Welcome to your account, {user.first_name.title()} - - - ")
        else:
            print(f"\n - - - Your details are invalid - - - ")
            login()

    while logged_in:
        option = input("\nWhat would you like to do? \na: add account\nb: show accounts\n"
                       "c: update account\nd: delete account\n e: logout ")

        if option.lower() == "a":
            account_login_password = "12345"
            account_name = input("Enter the name of the account you'd like to add: ")
            account_login_name = input("Enter the username for the account: ")
            password_choice = input("Enter 'g' to generate a random secure password or 'w' to write your own: ")
            if password_choice.lower() == "g":
                account_login_password = generate_password()
            elif password_choice.lower() == "s":
                account_login_password = input("Enter your desired password for the account: ")
            add_account(successful_user, account_name, account_login_name, account_login_password)


def add_account(user, name, username, password):
    user.accounts.append(Account(name, username, password))


def show_accounts(user):
    for account in user.accounts:
        print(account.name, account.username, account.password)




print("Welcome to the password vault!")

while True:
    print("\nWhat would you like to do? ")
    choice = input("a: open an account\nb: login to your account\n\n"
                   "Type 'a' for the first option and 'b' for the second: ")
    if choice.lower() == "a":
        create_user_account()
    else:
        login()
