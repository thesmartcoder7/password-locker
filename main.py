from user_details import User

user_accounts = []

print("Welcome to the password vault!")


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
    for user in user_accounts:
        if login_name == user.username and login_password == user.password:
            print(f"\n - - - Welcome to your account, {user.first_name.title()} - - - ")
            print("What would you like to do? \na: add account\nb: show accounts\n"
                  "c: update account\nd: delete account ")
        else:
            print(f"\n - - - Your details are invalid - - - ")
            login()


while True:
    print("\nWhat would you like to do? ")
    choice = input("a: open an account\nb: login to your account\n\n"
                   "Type 'a' for the first option and 'b' for the second: ")
    if choice.lower() == "a":
        create_user_account()
    else:
        login()
