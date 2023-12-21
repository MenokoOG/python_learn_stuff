#a shorthand if...else statement is used when yoou only have one satement to execute, uses ternary or conditional operator.
#in this next examples we convert an if...else statement to its shorthand version.
x = 10
if x == 10:
    print("x is 10")
else:
    print("x is not 10")
#shorthand version
x = 10
print("x is 10") if x == 10 else print("x is not 10")
#another case, assing a value to a variable depending on the result of an if...else statement.
#the "x is 10" string will be assigned to the str variable becasue the given expression is True.
x = 10
str = "x is 10" if x == 10 else "x is not 10"
print(str)
