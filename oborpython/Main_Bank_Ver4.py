"""Multiple account objects with interactive menu Menoko OG 4-19-2023"""
#Test program usings accounts, Ver 4, using a dictionary of accounts and an interactive menu
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

#test code for debugging
# accountsDict[joesAccountNumber].show()
# accountsDict[marysAccountNumber].show()

while True:
    print("********************")
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press o to open a new account")
    print("Press w to make a withdraw")
    print("Press s to show all accounts")
    print("Press q to quit")
    print("********************")
    
    action = input("What do you want to do? ")
    action = action.lower()
    action = action[0]
    print()
    
    if action == "b":
        print("***Get Balance***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input("Please enter the password: ")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print("Your balance is:", theBalance)
    
    elif action == "d":
        print("***Deposit***")
        userAccountNumber = input("Please enter the account number: ")
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input("Please enter amount to deposit: ")
        userDepositAmount = int(userDepositAmount)
        userPassword = input("Please enter password: ")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userPassword)
        if theBalance is not None:
            print("Your new balance is:", theBalance)
            
    elif action == "o":
        print("***Open Account***")
        userName = input("What is the name for the new user account? ")
        userStartingAmount = input("What is the starting balance for this account? ")
        userStartingAmount = int(userStartingAmount)
        userPassword = input("What is the passowrd you want to use for this account? ")
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print("Your new account number is:", nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()
        
    elif action == "s":
        print("Show:")
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print("    Account number:", userAccountNumber)
            oAccount.show()
    
    elif action == "q":
        break
    
    elif action == "w":
        print("***Withdraw***")
        userAccountNumber = input("Please enter your account number: ")
        userAccountNumber = int(userAccountNumber)
        userWithdrawAmount = input("Please enter the amount to withdraw: ")
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input("Please enter the password: ")
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawAmount, userPassword)
        if theBalance is not None:
            print("Withdrew:", userWithdrawAmount)
            print("Your new balance is:", theBalance)
    
    else:
        print("Sorry, that was not a valid action. Please try agian.")
print("Done")
        