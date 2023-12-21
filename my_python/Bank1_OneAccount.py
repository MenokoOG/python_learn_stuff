"""Analysis of Required Operations and Data
A list of operations a person would want to do with a bank account would
include:
Create (an account)
Deposit
Withdraw
Check balance
Next, here is a minimal list of the data we would need to represent a bank
account:
Customer name
Password
Balance
Notice that all the operations are action words (verbs) and all the data
items are things (nouns). A real bank account would certainly be capable of
many more operations and would contain additional pieces of data (such as
the account holder’s address, phone number, and Social Security number),
but to keep the discussion clear, I’ll start with just these four actions and
three pieces of data. Further, to keep things simple and focused, I’ll make
all amounts an integer number of dollars. I should also point out that in a
real bank application, passwords would not be kept in cleartext
(unencrypted) as it is in these examples."""

"""Non-OOP, Bank Version 1, Single account """

accountName = 'Joe'
accountBalance = 100
acoountPassword = 'soup'

while True:
    print()
    print('Press b to get balance')
    print('Press d to make deposit')
    print('Press w to make a withdraw')
    print('Press s to show account')
    print('Press q to quit')
    print()
    
    action = input('What do you want to do?')
    action = action.lower() #force lowercase
    action = action[0] # just use first letter
    print()
    
    if action == 'b':
        print('Get Balance:')
        userword = input('Please enter the passsword: ')
        if userword != acoountPassword:
            print('Incorrect passsword')
        else:
            print('Your balance is: {}'.format(accountBalance))
    elif action == 'd':
        print('Deposit:')
        userDepositsAmount = input('Please enter amount to deposit: ')
        userDepositsAmount = int(userDepositsAmount)
        userPassword = ('Please enter the password: ')
        
        if userDepositsAmount < 0:
            print('You cannot deposit a negative amount!')
        elif userPassword != acoountPassword:
            print('Incorrect password')
        else: #OK
            accountBalance = accountBalance + userDepositsAmount
            print(" Your new balance is: {}".format(accountBalance))
    elif action == 's': #show
        print('Show')
        print('Name: {}'.format(accountName))
        print('Balance: {}'.format(accountBalance))
        print('Password: {}'.format(acoountPassword))
        
    elif action == 'q':
        break
    
    elif action == 'w':
        print('Withdraw:')
        
        userWithDrawAmount = input('Please enter amount to withdraw: ')
        userWithDrawAmount = int(userWithDrawAmount)
        userPassword = input('Please enter password: ')
        
        if userWithDrawAmount < 0:
            print('You cannot withdraw a negative amount.')
            
        elif userPassword != acoountPassword:
            print('Inccorect password for this account.')
            
        elif userWithDrawAmount > accountBalance:
            print('You cannot withdraw more than you have in your account')
            
        else: # OK
            accountBalance = accountBalance - userWithDrawAmount
            print('Your new balance is: {}'.format(accountBalance))
print('Done')