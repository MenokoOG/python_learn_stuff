""" Two example accounts and populate them with viable data for testing. Menoko OG 4-18-2023 This project will import the class from the compiled pyc file to create the account objects"""
# Test program using accounts
# ver. 1, using explicit variable for each Account object
from Account import *

#create two accounts
oJoesAccount = Account("Joe", 100, "JoesPassword")
print("Created an account for Joe")

oMarysAccount = Account("Mary", 12345, "MarysPassword")
print("Created an account for Mary")

oJoesAccount.show()
oMarysAccount.show()
print()

# Call some methods on the different accounts
print("Calling methods of the two account...")

oJoesAccount.deposit(50, "JoesPassword")
oMarysAccount.withdraw(345, "MarysPassword")
oMarysAccount.deposit(100, "MarysPassword")

#show the accounts
oJoesAccount.show()
oMarysAccount.show()

#create another account with infromation from the user 
print()
userName = input("What is the name for the new user account? ")
userBalance = input("What is the starting balance for this account? ")
userPassword = input("What is the password you want to use for this account? ")
oNewAccount = Account(userName, userBalance, userPassword)

#show new account
oNewAccount.show()

#deposit 100 into new account
oNewAccount.deposit(100, userPassword)
usersBalance = oNewAccount.getBalance(userPassword)
print()
print("After depositing 100, the user's balance is: {}".format(usersBalance))

oNewAccount.show()
