# This is basic python prog to simulate ATM

# Import the package
from banking_pkg import account

# Define function to display ATM Menu


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# Register a user
print("          === Automated Teller Machine ===          ")
name = input("Enter name to register:  ")
pin = input("Enter PIN:  ")
balance = 0
print(name, "has been registered with a starting balance of", '$' + str(balance))

# Check for ATM login
while True:
    print("\n          === Automated Teller Machine ===          ")
    print("\nLOGIN ")
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter PIN: ")
    if (name_to_validate == name and pin_to_validate == pin):
        print("\nLogin successful!")
        break
    else:
        print("\nInvalid credentials!")

# For Successful login, take user option and call appropriate function
while True:
    atm_menu(name)
    option = input("Choose an option: ")  # User's option
    if option == '1':
        account.show_balance(balance)     # Show account balance
    elif option == '2':
        balance = account.deposit(balance)  # Deposit to account
        account.show_balance(balance)
    elif option == '3':
        balance = account.withdraw(balance)  # Withdrawal from account
        account.show_balance(balance)
    elif option == '4':
        account.logout(name)                 # Logout
        break
    else:
        print("\nInvalid option!")           # Invalid option
