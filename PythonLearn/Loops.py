#Loops are use to repetitively execute a groups of statements (or blocks of codes). in Python there are tow types of Loops
# for loop, the while loop
#the for loop is used to loop through or iterate over a sequence or iterable objects, strings, lists, sets, etc..., 
# basically anything you can loop through
#loop through list
from threading import ThreadError


pets = ["cat", "dogs", "rabbits"]
for pet in pets:
    print(pet)
tanks = ["m1Abrahm", "m60", "sherman"]
for tank in tanks:
    print(tank)
#loop through string
txt = "Hello World!"
for x in txt:
    print(x)
#range() function(method), sometimes you will need to repetitively execute a block of code but you dont't have something 
# to loop over, range() creates a sequence of numbers.
for x in range(5):
    print(x)
    #here we created a sequence of five numbers staring from 0.
#here we will print "hello fuckers!" three times.
for x in range(3):
    print("Hello Fuckers!")
#nested for loops, loop can be palced inside another for loop
animal = ["tiger", "cat", "dog"]
sound = ["roars", "meows", "barks"]
for x in animal:
    for y in sound:
        print("the" + x + " " + y)
#use else with for loop
for x in range(5):
    print("Hello World")
else:
    print("loop has ended")

#while loop, executes a group of sttements as long as the given expression is True
i = 0
while i < 5:
    print(i)
    i += 1
i = 1
while i <= 5:
    print("Hello Fuckers!")
    i += 1
#else statement is executed when the iteration of the while loop ends.
i = 1
while i <= 5:
    print("Hello There")
    i += 1
else:
    print("Loop has ended")

#break and continue, break statement stops the execution of the current loop.
pets = ["dogs", "cats", "rabbits"]
for pet in pets:
    print(pet)
    if pet == "cats":
        break
#now with break before print()
pets = ["dogs", "cats", "rabbits"]
for pet in pets:
    if pet == "cats":
        break
    print(pet)
#can use break statement on a while loop
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
#the continue statement, terminates the execution of the current iteration of the loop, and continues the execution 
# of the loop wiht the next iteration
pets = ["dogs", "cats", "rabbits"]
for pet in pets:
    if pet == "cats":
        continue
    print(pet)
#example of using it when looping through a string
txt = "hello"
for x in txt:
    if x == "l":
        continue
    print(x)
#we can use the continue statement on a while loop
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)


#pass statementis used as a palceholder when a statement is syntactically required.
#when it is executed, nothing happens
def add():
    pass
def subtract():
    pass
print("Hello World")
#it can also be used on if statements, loops, classes etc.
if 5 == 5:
    pass
else:
    pass
pets = ["cats", "dogs", "Rabbits"]
for pet in pets:
    pass
class Student:
    pass
print("Hello there")