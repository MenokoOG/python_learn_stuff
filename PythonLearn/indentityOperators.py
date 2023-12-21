#Identity operators are used to compare two values to determine if they point to the same object.
#there are two identity operators, is operator, is not operator
# the is operator returns True if both operands point to the same object. In the following example
#there are two list stored in the x and y variables. the is operator will return False becasue the 
# even though they varaibles have same value, they do not point to same object
from re import X


x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)
#here it will return True because both x and z point to the same object.
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is z)
#here it can be beter understood by comparing it with the equality operator =
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
x = ["Hello", "World", 4]
y = ["Hello", "World", 4]
c = ["Hello", "World", 3]
z = x
b = y
d = c
print(x == y)
print(x is y)
print(z is x)
print(c == x, c == y)
print(d is c)
print(d == c)
#the is not operator retunrs True if both operands do not point to the same object
# it is basically opposite of is operator.
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is not y)
x = [1, 2, 3]
y = [1, 2, 3]
z = x 
print(x is not z) #False becasue z is x
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
x = ["Hello", "World", 4]
y = ["Hello", "World", 4]
c = ["Hello", "World", 3]
z = x
b = y
d = c
print(x == y)
print(x is not y)
print(z is not  x)
print(c == x, c == y)
print(d is not c)
print(d == c)