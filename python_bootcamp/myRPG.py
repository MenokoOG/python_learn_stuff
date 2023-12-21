#-------------------------------------------------------------------------------
# Name:        myRPG
# Purpose: an rpg question game for python exercise
#
# Author:      jefft
#
# Created:     28/10/2022
# Copyright:   (c) jefft 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def tha_rpg():
    print("the Game starts!!!!!")

def game_strt():
    start_gm =input("Would you like to play a story game with me? \n Please put 1 for yes and 2 for No")
    if start_gm != int:
        print("What the Fuck!!!!! {} is not  1 or 2!!".format(start_gm))
    elif start_gm == "1":
        start_gm = int(start_gm)
        if start_gm == 1:
            print("Awessome get ready for some fun!!", tha_rpg())
    elif start_gm == "2":
        start_gm = int(start_gm)
        if start_gm == 2:
            print("Sorry you did not want to play")

def my_rpg():
    name = str(input("Please enter your name: "))
    print("Welcome {}".format(name), game_strt())

# make the next function another file and then import into this start script.

#here make start_gm function to pass variables to run next code blocks for type conversion

my_rpg()