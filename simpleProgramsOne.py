# promgram to get python version
import sys

print("Python Version")
print()
print(sys.version)
print()
print("Version Info.")
print()
print(sys.version_info)
print()
print("Python Version: ", sys.version, "Version Info: ", sys.version_info)
print("---------------------------")
# program to get date and time
import datetime

now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d-%H:%M:%S"))
print("------------------------------")
# program to accept the raduis of a circle form user and computes area.
# from math import pi
# r = float(input("Input the raduis of the circle : "))
# print("The are of the cirlce with raduis " + str(r) + " is " + str(pi * r**2))
print("-------------------------------")
# for loops practice
for x in "Shithead":
    print(x)
print("-------------------------------")
mylist = ["m-16", "ak-47", "mp5", "m-1"]  # exit the loop when x is m-1
for x in mylist:
    print(x)
    if x == "m-1":
        break
# nested for  loops
weapon = ["Rifle", "Machine", "Bazzoka", ]
assigned = ["private", "cpl", "fuckstick"]
for x in weapon:
    for y in assigned:
        print(x, y)
print("---------------------------")


# here i make a function to match weapon to assigned person
def weapon_roster():
    print(weapon[0], assigned[0])
    print(weapon[1], assigned[1])
    print(weapon[2], assigned[2])


weapon_roster()  # call the function
print("-------------------------------")
# square root program7
number = int(input("enter a number: "))
sqrt = number ** 0.5
print("square root: ", sqrt)
print("--------------------------")
print("Hello World!")
