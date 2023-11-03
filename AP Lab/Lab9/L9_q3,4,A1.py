class Bank:
    def __init__(self, name, age, account_number, account_type, balance):
        if 18 <= age <= 100:
            self.age = age
        else:
            raise ValueError("Age must be between 18 and 100")

        if 10000 <= account_number <= 99999:
            self.account_number = account_number
        else:
            raise ValueError("Account number must have exactly 5 digits")

        if account_type in ["S", "C"]:
            self.account_type = account_type
        else:
            raise ValueError("Account type must be 'S' (Savings) or 'C' (Current)")

        self.name = name
        self.balance = balance

    def display_account_details(self):
        print("Account Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)
        print()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def __del__(self):
        print(f"Account {self.account_number} is closed.")

# Creating a new account
def create_new_account():
    name = input("Enter the account holder's name: ")
    try:
        age = int(input("Enter the account holder's age: "))
        if not (18 <= age <= 100):
            raise ValueError("Age must be between 18 and 100")
        account_number = int(input("Enter the account number (5 digits): "))
        if not (10000 <= account_number <= 99999):
            raise ValueError("Account number must have exactly 5 digits")
        account_type = input("Enter the account type (S for Savings, C for Current): ")
        if account_type not in ["S", "C"]:
            raise ValueError("Account type must be 'S' (Savings) or 'C' (Current)")
        balance = float(input("Enter the initial balance: "))

        new_account = Bank(name, age, account_number, account_type, balance)
        print("Account created successfully.")
        return new_account
    except ValueError as e:
        print("Account creation failed:", e)
        return None

# List to store bank accounts
accounts = []

# Menu-driven program
while True:
    print("\nBank Operations Menu:")
    print("1. Create a New Account")
    print("2. Display Account Details")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_account = create_new_account()
        if new_account:
            accounts.append(new_account)

    elif choice == 2:
        account_number = int(input("Enter the account number: "))
        found = False
        for account in accounts:
            if account.account_number == account_number:
                account.display_account_details()
                found = True
                break
        if not found:
            print("Account not found.")

    elif choice == 3:
        account_number = int(input("Enter the account number: "))
        amount = float(input("Enter the deposit amount: "))
        found = False
        for account in accounts:
            if account.account_number == account_number:
                account.deposit(amount)
                found = True
                break
        if not found:
            print("Account not found.")

    elif choice == 4:
        account_number = int(input("Enter the account number: "))
        amount = float(input("Enter the withdrawal amount: "))
        found = False
        for account in accounts:
            if account.account_number == account_number:
                account.withdraw(amount)
                found = True
                break
        if not found:
            print("Account not found.")

    elif choice == 5:
        break
