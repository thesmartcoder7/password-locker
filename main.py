from user_details import User, Credentials
import random

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
    this function is responsible for generating a 15 character random, secure password
    :return: it returns the randomly generated password to the function that calls it
    """
    r_letters = [random.choice(characters) for _ in range(5)]
    r_numbers = [random.choice(numbers) for _ in range(5)]
    r_symbols = [random.choice(symbols) for _ in range(5)]
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

    if user_name not in User.user_accounts:
        User.add_user(user_name)
        print("\n - - - Account successfully created! - - - ")
    else:
        print("That username is already taken!")
        create_user_account()


def login():
    """
    This function is responsible for taking in use login details and validating them for a proper login.
    :return: It does not return any value. It just executes.
    """
    print("\n - - - login - - - ")
    login_name = input("Enter your username: ")
    login_password = input("Enter your password: ")
    successful_user = User.user_login(login_name, login_password)[1]
    logged_in = User.user_login(login_name, login_password)[0]
    if logged_in:
        print(f"\n - - - Welcome to your account, {successful_user.first_name.title()} - - - ")
    else:
        print(f"\n - - - Your details are invalid - - - ")
        login()

    while logged_in:
        option = input("\nWhat would you like to do? \na: add account\nb: show accounts\n"
                       "c: edit account\nd: delete account\ne: logout\n:")
        if option.lower() == "a":
            account_login_password = "12345"
            account_name = input("Enter the name of the account you'd like to add: ")
            account_login_name = input("Enter the username for the account: ")
            password_choice = input("Enter 'g' to generate a random secure password or 'w' to write your own: ")
            if password_choice.lower() == "g":
                account_login_password = generate_password()
                print("\n - - - Account added successfully! - - - \n")
            elif password_choice.lower() == "w":
                account_login_password = input("Enter your desired password for the account: ")
                print("\n - - - Account added successfully! - - - \n")
            add_account(successful_user, account_name, account_login_name, account_login_password)
        elif option.lower() == "b":
            successful_user.show_accounts()
        elif option.lower() == "c":
            edit_account(successful_user)
        elif option.lower() == "d":
            delete_account(successful_user)
        elif option.lower() == "e":
            logged_in = False
            print("\n - - - You have been logged out! - - - \n")


def add_account(user, name, username, password):
    """
    this method is responsible for creating new instances of accounts and adding them into the user accounts
    :param user: this is taken in to represent the main User object
    :param name: this is an attribute of the account class that represents the name of the specific account
                 to be added
    :param username: this is the username parameter that is to be stored as the account's username
    :param password: this is the username parameter that is to be stored as the account's password
    :return: this function does not return anything, it just does its work.
    """
    user.accounts.append(Credentials(name, username, password))


def edit_account(user):
    """
    this is responsible for editing the individual accounts
    :param user: the user parameter in this context represents the User object instance
    :return: this function does not return anything, it just does its work
    """
    to_edit = input("Which account's credentials would you like to edit? ")
    for account in user.accounts:
        if account.name.lower() == to_edit.lower():
            account.username = input(f"Your old username is {account.username}. What is your new username? ")
            password_choice = input("Enter 'g' to generate a random secure password or 'w' to write your own: ")
            if password_choice.lower() == "g":
                account.password = generate_password()
                print("\n - - - Your account has been successfully updated! - - - \n")
            elif password_choice.lower() == "w":
                account.password = input("Enter your desired password for the account: ")
                print("\n - - - Your account has been successfully updated! - - - \n")


def delete_account(user):
    """
    this function is responsible for removing the credentials for the selected user
    :param user: in this context, the user represents the object instance of the User class
    :return: this function does not return anything, it just does its work
    """
    to_delete = input("Which account's credentials would you like to delete? ")
    for account in user.accounts:
        if account.name.lower() == to_delete.lower():
            user.delete_account(account)
            print("\n - - - Your account's credentials have been successfully deleted! - - - \n")


def main():
    print("Welcome to the password vault!")

    while True:
        print("\nWhat would you like to do? ")
        choice = input("a: open an account\nb: login to your account\n\n"
                       "Type 'a' for the first option and 'b' for the second: ")
        if choice.lower() == "a":
            create_user_account()
        else:
            login()


if __name__ == "__main__":
    main()
