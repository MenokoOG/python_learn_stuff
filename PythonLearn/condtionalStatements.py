#condtional statements are used to execute statements based on different conditions.
#if statement, exectues a group of statements if the given expression is True
x = 10
y = 5
if x > y:
 str = "Hello World"
 print(str)
 #if...else, executes a group of statemetns if the given expression to if is False.
 age = 15
if age > 18:
    print("user is old enough to enter")
else:
    print("user is not old enough to enter")
#if...elif statement, executes a group of statements if its expression is True and the first expression is False.
x = 5
if x > 10:
    print("x is more than 10")
elif x < 10:
    print("x is less than 10")
#we can add an else statement to the if..elif statement, in this case the else is executed if both expressions 
# given to if and elif are False.
x = 10
if x > 10:
    print("x is more than 10")
elif x < 10:
    print("x is less than 10")
else:
    print("x is 10 becasue it's neither less or more than 10")
#using logical operators, we can use the and or operators with condtional statements
#in this next example, the and operator returns True if both expressions (or Boolean Values) are True.
x = 10
y = 5
if (x == 10) and (y == 5):
    str = "Hello World!"
    print(str)
#Nested if Statements
x = 15
if x > 5:
    print("x is more than 5")
    if x > 10:
        print("x is more than 10")
    else:
        print("x is NOT more than 5")
