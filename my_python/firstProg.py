#printing two objects
print("Hello", "World")
#multiple statements in one line
x = 3; y = 21; sum = x + y; print("the sum is", sum)
x = 4; y = 3; print(x + y)
#one statement in multiple lines
fruits = ["orange",
       "mango",
       "banana"]
print(fruits)
#indentation is very important in python, it indicates a block of (group) of statements.
if 5 > 4:
    x = "Hello World!"
    print(x)
if 5 > 4:
    x = "Hello World!"
    print(x)
print("the block of statements below ends here.")
if 3 > 4:
    x = "Hello World!"
    print(x)
print("the block of statements below ends here.") #hello world was no tprinted due to statement not true.



#python variables
fruit = "mangos"
print(fruit)
name = "Juan"
print("Hello " + name)
#changing a variable is simple in python. remeber scope you are working in, global, local, function, etc.
name = "Juan"
name = " Joquin"
print("Hello " + name)
#assign new data type is simple in python
name = "Juan"
name = 21
name = "fuckers"
print(name)
#naming conventions
my_favorite_fruit = "mangos"
print(my_favorite_fruit)
myFavoriteFruit = "oranges"
print(myFavoriteFruit)
#legal names
myname = "Juan"
my_name = "Juan"
#_myname = "Juan" pylance extension problem
myname1 = "Juan"
myName = "Jefferson"



#Data Types
# x is an integer
x = 21
print(x)
# x is a floating point
x = 21.33
print(x)
x = 7
y = 3
print(x + y)
#strings are simply text, sinlge or double qoutes can be used.
fruit = 'mangos'
print(fruit)
fruit = "apples"
print(fruit)
#use single quotes when your string contains double quotes.
x = 'I told you "Python is fun to learn."'
y = 'I fucken roared "Python is Fun!!!"'
print(x)
print(y)
#use double quotes when your string contains single quotes
x = "Let's learn Python!"
print(x)
#booleans, boolean data type can only have one of these two values: True or False
print(10 > 5)
print(6 > 3)
print(4 > 2)
print(5 == 5)
print(5 == 6)
#list, an ordered collection data, it can contain any data type also written with square brackets ([])
myList = ["mangos", "oranges", "cherries"]
print(myList)
myList = [2, 4, 6, 8, 10]
print(myList)