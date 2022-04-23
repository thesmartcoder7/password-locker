from user import User

user_accounts = []

print("Welcome to the password vault!")

while True:
    print("\nWhat would you like to do? ")
    choice = input("a: open an account\nb: login to your account\n\n"
                   "Type 'a' for the first option and 'b' for the second: ")

    if choice.lower() == "a":
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        user_name = input("Enter your desired username: ")
        user_password = input("Enter your desired password: ")

        user_name = User(first_name, last_name, user_name, user_password)
        print("\n - - - Account successfully created! - - - ")

        user_accounts.append(user_name)

    else:
        login_name = input("Enter your username: ")
        login_password = input("Enter your password: ")
        for user in user_accounts:
            if login_name == user.username and login_password == user.password:
                print(f"\n - - - Welcome to your account, {user.first_name.title()} - - - ")
            else:
                print("\n - - - Your details are invalid - - - ")
