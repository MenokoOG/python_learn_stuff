# some scripting practice code

number = int(input("enter a number: "))
sqrt = number ** 0.5
print("square root: ", sqrt)

num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")
print("num1 before swapping: ", num1)
print("num2 before swapping: ", num2)
temp = num1
num1 = num2
num2 = temp
print("num1 after swapping:", num1)
print("num2 after swapping: ", num2)

# celsius to fahrenheit
c = float(input("Enter temp in Centigrade: "))
f = (1.8*c) + 32
print("Temperature in Fahrenheit={0:2f}".format(f))

# fahrenheit to celsius
f = float(input("enter temp in fahrenheit: "))
c = ((f-32) * 5/9)
print("Temperature in Centigrade={0:2f}".format(c))

def my_name():
    name = input("what is your name? ".lower())
    print("Hello {}, hope your good!".format(name))
