# Function for balance show
def show_balance(balance):
    print("The Current Account Balance is: ", balance)

# Function for deposit to account


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return balance + float(amount)

# Function for withdrawal from account


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    return balance - float(amount)

# Function for logout


def logout(name):
    print("GoodBye", name + '!')
