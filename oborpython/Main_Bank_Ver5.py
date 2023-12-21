"""Main code for controlling a Bank made up of Accounts, Menoko OG 4-2-2-23"""
#Main program for controlling Bank made up of Accounts
# Bring in all the code of the Bank class
from Bank import *

#Create an instance of the Bank
oBank = Bank()

#Main code
# Create two test accounts (puts something account objects to see, you can create any number of test accounts here)
joesAccountNumber = oBank.createAccount("Joe", 100, "JP")
print("Joe's account number is:", joesAccountNumber)

marysAccountNumber = oBank.createAccount("Mary", 12345, "MP")
print("Mary's account number is:", marysAccountNumber)

while True:
    print("**************************************")
    print("To get an account balance, press b")
    print("To close an account, press c")
    print("To make a deposit, press d")
    print("To open a new account, press o")
    print("To quit, press q")
    print("To show all accounts, press s")
    print("To make a withdraw, press w")
    print("**************************************")
    
    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0] #grab first letter
    print()
    
    if action == "b":
        oBank.balance()
    
    elif action == "c":
        oBank.closeAccount()
    
    elif action == "d":
        oBank.deposit()
    
    elif action == "o":
        oBank.openAccount()
    
    elif action == "s":
        oBank.show()
    
    elif action == "q":
        break
    
    elif action == "w":
        oBank.withdraw()
    
    else:
        print("Sorry, that was not a vaild action, please try again")
print("Done")