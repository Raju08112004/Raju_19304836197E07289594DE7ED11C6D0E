class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"${amount} deposited. New balance: ${self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"${amount} withdrawn. New balance: ${self.__account_balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name} (Account {self.__account_number}): ${self.__account_balance}"

# Create an instance of the BankAccount class
account = BankAccount("12345", "John Doe", 1000)

# Test deposit and withdrawal functionality
print(account.display_balance())
print(account.deposit(500))
print(account.withdraw(200))
