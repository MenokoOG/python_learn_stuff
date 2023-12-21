#Logical Operator
#logical operators are commonly used with Booleans. there are 3 logical operators. and, or, not
#logical and returns True if both operands are True
print(True and True)
print(True and False)
print(False and False)
#logical operators are commonly used on expressions
expr = (5 == 5) and (4 == 4)
print(expr)
x = 4
expr = (x > 3) and (8 < x) #False
print(expr)
#logical or operator, retunrs True if either of the operands is True.
print(True or True)
print(True or False)
print(False or False)
expr = (5 == 5) or (4 == 5) #True because one of the statements is True
print(expr)
expr = (10 > 5) or (40 < 30) #True because one of the statements is True
print(expr)
#logical not operator, returns True if the operand is False.
print(not(False)) #True
expr = not(10 > 20)
print(expr)
expr = not(10 == 10)
print(expr)