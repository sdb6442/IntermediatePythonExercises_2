# Exercise 1 - Main Class for importing and running BankAccount class

# Import BankAccount class
from BankAccount import BankAccount

# Create an Account
checkingAccount = BankAccount('Samuel Baynes', 1000)

# Deposit $200
checkingAccount.deposit(200)

# Withdraw $50
checkingAccount.withdraw(50)

# Print balance of account by using get_balance method on the created checkingAccount
print(checkingAccount.get_balance())