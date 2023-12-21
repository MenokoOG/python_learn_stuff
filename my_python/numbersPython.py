#numbers, there are three types, integer, floating point, and complex
#integers are numbers without decimals
a = 3
b = 4
c = 5
print(a, b, c)
#floating point numbers or a float is a number with decimals
a = 3.0
b = 4.21
c = 5.33
print(a + b + c)
#complex number is an imagenary number, append a j or J to a numeric value to yield a complex number
a = 3j
b = 4.21j
c = 5.33j
print(a + b + c)
#getting type of numerical values, use type() function
a = 3
b = 21
c = 4.0
d = 5.21
e = 4.21j
f = 5.33j
print (type(a))
print (type(b))
print (type(c))
print (type(d))
print (type(e))
print (type(f))
#add, subtract, multiply, divide numbers
x = 2 + 4
print(x)
x = 4 - 2
print(x)
x = 4 * 2
print(x)
x = 4 / 2
print(x)



#python number methods
#rounding a number, round() function rounds a floating point to a specified point.
#syntax round(number, ndigits), number to round off then the number of decimal places
pi = 3.1415926535897
two_decimals = round(pi, 2)
three_decimals = round(pi, 3)
fourDecimals = round(pi, 4)
print(two_decimals)
print(three_decimals)
print(fourDecimals)
#raising a number to a power, the pow() function is used to raise a number to specified power
#syntax pow(base, exp), the base number then the exponent
x = pow(4, 2) #same as 4 * 4
y = pow(4, 3) #same as 4 * 4 * 4
print(x)
print(y)
#absolute value function abs(), returns the non-negative value of a nnumber
a = abs(-4)
b = abs(-3.21)
print(a)
print(b)
#quotient and remainder, divmod() funtion takes two numbers and return a pair of numbers consisting of thier quotient and remainder.
# in the following example, 5 is divided 2, therefore the quotient is 2 and the remainder is 1.
x = divmod(5, 2)
print(x)


