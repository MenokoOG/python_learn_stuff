#python booleans, boolean data type can only be either: True or False.
a = True
b = False
print(a)
print(b)
#the first letter of a Boolean is in upper case. Booleans are often the result of evaluated expressions.
#for comparing to numbers, python evaluates the expression and returns either True or False.
print(5 ==5)
print(10 > 5)
print(20 < 10)
#these are often used in if statments.  in the next example if the value of te variable age is nore than 18, 
# the program will tell the user that they are allowed to enter.
age = 19
if age > 18:
    print("You are allowed to enter.")
#checking the type of a boolean, we can check the data type of a boolean variable using the type() method.
x = True
y = type(x) #returns class <class 'bool'>
print(y)



#python operators, operators are symbols perform operations on operands. Operands can be variables, strings, numbers, booleans, etc
print(10 + 5) #the + is the operator, the left operand is 10 and the right operand is 5, the operator adds the two numbers
x = 4
print(x) #the operator is = sign, the left operand is the variable named x while the right operand is the number 4, the operator assigns
#the right operand as the value of the left operand.
print(5 == 5) # the == operator returns True if both operands are the same or equal to each other, otherwise returns False.
print(10 > 5) #operator > returns True if the left operand is greater the the right operand, other wise returns False.