#python arithmetic operators, perform mathematical operations on its numerical operands, there are 7 basic arithmetic operators.
# + operator/addition, - operator/subtraction, * operator/multiplication, / operator/division, ** operator/exponentiation,
# % operator/remainder, // operator/floor division
# addition operator
x = 10
y = 5
print(x + y)
#can be used to concatenate or join strings
x = "Hello" + " " + "Fuckers!"
print(x)
#subtraction operator
x = 10
y = 5
print(x - y)
#multiplication operator
x = 10
y = 5
print(x * y)
# dividion operator
x = 10
y = 5
print(x / y)
x = 10
y = 5
z = x / y
z = int(z)
print(z)
#exponentiation operator
x = 2 ** 3 #same as 2 * 2 * 2
print(x)
#remainder operator
x = 5 % 2
print(x)
#floor division operator
x = 5 // 2
print(x)
#operator sequence, descirbes order of performed operations in an arithmetic expression.
x = 10 + 3 * 5 #returns 25
print(x)
#to prevent MDAS from happeneing, group expressions together, grouped expressions are performed first before others
x = (10 + 3) * 5 #now it returns 65 because 10 + 3 is 13 and then times 5.
print(x)