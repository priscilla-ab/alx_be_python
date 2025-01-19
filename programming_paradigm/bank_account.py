# Define the BankAccount class
class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance (default is 0)."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the specified amount from the account balance if sufficient funds exist."""
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            raise ValueError("Withdraw amount must be positive.")

    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
