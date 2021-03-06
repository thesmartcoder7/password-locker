from user_details import User, Credentials
import random
import pyperclip

# TODO 1. Get all the characters needed for the password generator
characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']


# TODO 2. Create the password generator function
def generate_password():
    """
    this function is responsible for generating a 15 character random, secure password
    :return: it returns the randomly generated password to the function that calls it
    """
    try:
        length = int(input("\nChoose a password length between 8 and 15 random characters: "))
        if length < 8 or length > 15:
            print("Range Error: You are not allowed to generate a password shorter than 8 characters or longer than 15")
            generate_password()
        else:
            r_letters = [random.choice(characters) for _ in range(5)]
            r_numbers = [random.choice(numbers) for _ in range(5)]
            r_symbols = [random.choice(symbols) for _ in range(5)]
            gen_password = r_letters + r_numbers + r_symbols
            random.shuffle(gen_password)
            generated_password = "".join(gen_password)
            final_password = generated_password[0:length]

            return final_password

    except ValueError:
        print("Please enter the right length! Just numbers. No words allowed!")
        generate_password()


# TODO 3. Create a function to create a user account from the user input
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


# TODO 4. Create a function to allow users to login
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
                       "c: edit account\nd: delete account\ne: logout\nchoice: ")
        if option.lower() == "a":
            account_login_password = "12345"
            account_name = input("\nEnter the name of the account you'd like to add: ")
            account_login_name = input("Enter the username for the account: ")
            password_choice = input("Enter 'g' to generate a random secure password or 'w' to write your own: ")
            if password_choice.lower() == "g":
                account_login_password = generate_password()
                user_copy = f"username: {account_login_name}\npassword: {account_login_password}"
                pyperclip.copy(user_copy)
                print("\nYour details have been copied to clipboard")
                print("\n - - - Account added successfully! - - - \n")
            elif password_choice.lower() == "w":
                account_login_password = input("Enter your desired password for the account: ")
                user_copy = f"username: {account_login_name}\npassword: {account_login_password}"
                pyperclip.copy(user_copy)
                print("\nYour details have been copied to clipboard")
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


# TODO 5. Create a function to add account and the user's accounts array
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
    print(user.accounts)


# TODO 6. Create a function to allow users to edit the accounts within
def edit_account(user):
    """
    this is responsible for editing the individual accounts
    :param user: the user parameter in this context represents the User object instance
    :return: this function does not return anything, it just does its work
    """
    if len(user.accounts) == 0:
        print("\n - - - There are no accounts for your to edit! - - - ")
    else:
        to_edit = input("Which account's credentials would you like to edit? ")
        for account in user.accounts:
            if account.name.lower() == to_edit.lower():
                account.username = input(f"Your old username is {account.username}. What is your new username? ")
                password_choice = input("Enter 'g' to generate a random secure password or 'w' to write your own: ")
                if password_choice.lower() == "g":
                    account.password = generate_password()
                    user_copy = f"username: {account.username}\npassword: {account.password}"
                    pyperclip.copy(user_copy)
                    print("\nYour details have been copied to clipboard")
                    print("\n - - - Your account has been successfully updated! - - - \n")
                elif password_choice.lower() == "w":
                    account.password = input("Enter your desired password for the account: ")
                    user_copy = f"username: {account.username}\npassword: {account.password}"
                    pyperclip.copy(user_copy)
                    print("\nYour details have been copied to clipboard")
                    print("\n - - - Your account has been successfully updated! - - - \n")


# TODO 7. Create an account to allow users  to delete a specific account
def delete_account(user):
    """
    this function is responsible for removing the credentials for the selected user
    :param user: in this context, the user represents the object instance of the User class
    :return: this function does not return anything, it just does its work
    """
    if len(user.accounts) == 0:
        print("\n - - - There are no accounts to delete in this collection - - - ")
    else:
        to_delete = input("\nWhich account's credentials would you like to delete? ")
        for account in user.accounts:
            if account.name.lower() == to_delete.lower():
                user.delete_account(account)
                print("\n - - - Your account's credentials have been successfully deleted! - - - \n")


def main():
    print("Welcome to the password vault!")
    program_is_running = True
    while program_is_running:
        print("\nWhat would you like to do? ")
        choice = input("a: open an account\nb: login to your account\nc: close application\n\n"
                       "Type 'a' for the first option, 'b' for the second, and 'c' for the last: ")
        if choice.lower() == "a":
            create_user_account()
        elif choice.lower() == "b":
            login()
        elif choice.lower() == "c":
            program_is_running = False
        else:
            print("\nThat is not a valid input! Try again")

    print("\n - - - Shutting down the application - - - ")


if __name__ == "__main__":
    main()
