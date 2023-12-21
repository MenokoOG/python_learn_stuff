"""Multiple account objects in a dictionary Menoko OG 4-19-2023"""
#Test program usings accounts, Ver 3, using a dictionary of accounts
from Account import *

accountsDict = {}
nextAccountNumber = 0

# Create two accounts:
oAccount = Account("Joe", 100, "JoesPassword")
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print("Account number for Joe is:", joesAccountNumber)
nextAccountNumber = nextAccountNumber + 1
print()
oAccount = Account("Mary", 12345, "MarysPassword")
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print("Account number for Mary is:", marysAccountNumber)
nextAccountNumber = nextAccountNumber + 1
print()
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
# Call some methods on the different accounts
print("***calling some methods of two accounts...***********")
accountsDict[joesAccountNumber].deposit(50, "JoesPassword")
accountsDict[marysAccountNumber].withdraw(345, "MarysPassword")
accountsDict[marysAccountNumber].deposit(100, "MarysPassword")
# Show Accounts
print("**********Showing Accounts with updates*******")
accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()

# Create another account with innformation from the user
print("*****************************")
print()
userName = input("What is the name for te new user account? ")
userBalance = input("What is the starting balance for this account? ")
userPassword = input("What is the password you want to use for this account? ")
oAccount = Account(userName, userBalance, userPassword)
newAccountNumber = nextAccountNumber
accountsDict[newAccountNumber] = oAccount
print("Account number for new account is:", newAccountNumber)
nextAccountNumber = nextAccountNumber + 1

accountsDict[newAccountNumber].show()
