#python type conversion, if you try to concatenate or combine a string and a number, you will get error
#x = 21
#text = "this number"
#print(x + text)
#to prevent error, first convert the type of number to string (str) using str() function
x = 21
x = str(x)
text = "this number"
print(x + " " + text)
#convert to integer, int() method retunrs the integer version of object
x = 4.55
x = int(x)
print(x)
#the next is string to integer then add to integer
x = "50"
x = int(x) + 60
print(x)
#convert to float, float method returns the float point version of the given object.
x = 4
x = float(x)
print(x)
#this next statement is an example of convert a string to a floating point then add it to another floating point
x = "4.3"
sum = float(x) + 6.5
print(sum)