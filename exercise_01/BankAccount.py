# Exercise 1 - Bank Account Class
# I consulted the "Intermediate Python" Powerpoint from the class material and chatGBT
# for completing this class.

# BankAccount class
class BankAccount:
    # Constructor
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    # Deposit Method - adds amount to balance
    def deposit(self, amount):
        self.balance += amount
    
    # Withdraw Method - subtracts amount from balance
    def withdraw(self, amount):
        self.balance -= amount

    # Get Balance method - returns a message with the user's balance
    def get_balance(self):
        return f"{self.account_name} has a balance of ${self.balance}"