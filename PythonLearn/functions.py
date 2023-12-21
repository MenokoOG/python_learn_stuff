#function is a group of statements that performs a particuliar task.
def my_func():
    x = "Hello World!"
    print(x)
my_func()
def my_func():
    x = "love python programming"
    print(x)
my_func()
#when calling a function, we can pass data using parameters/arguments, in he next example name is the parameter, then we pass 
# "John" through argument.
def hello(name):
    x = "Hello" + name
    print(x)
hello(" Jack off")
#multiple parameters/argument, separate using commas
def add_nums(num1, num2):
    sum = num1 + num2
    print(sum)
add_nums(4, 3)
#functions can have default arguments, it is done using assignment operator =, so if you do not pass an argument, the dfault will be used
def hello(name = " Joker"):
    x = "Hello" + name
    print(x)
hello(" Asshole")
hello()
#keyword arguments , the position does not matter
def my_func(fruit1, fruit2, fruit3):
    print("I love", fruit1)
    print("I love", fruit2)
    print("I love", fruit3)
my_func(fruit3 ="grapes", fruit2 = " oranges", fruit1 = "apples")
#the return satement is used to return a value to the function caller.
def add_nums(num1, num2):
    sum = num1 + num2
    return sum
print(add_nums(4, 4))

def add_nums(num1, num2):
    sum = num1 + num2
    return sum
x = add_nums(4, 3)
print(x)
def add_nums(num1, num2):
    sum = num1 + num2
    return sum
print(add_nums(3, 3))
print("this string is outside now so will be printed")

