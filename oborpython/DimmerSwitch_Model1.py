"""DimmerSwitch  object project by Menoko OG 4-15-20230"""
"""The lesson here is that you can think of each object as a self-contained unit that
contains a data type, a set of the instance variables defined in the class, and
a copy of all the methods defined in the class

The data and methods of each object are packaged together. The scope of
an instance variable is defined as all the methods in the class, so all methods
have access to the instance variables associated with that object.
If this mental model makes the concepts clear, then you’re in good shape.
While this is not the way objects are actually implemented, it’s a perfectly
reasonable way to think about how an object’s instance variables and
methods work together."""

class DimmerSwtich():
    """DimmerSwitch  object project by Menoko OG 4-15-20230"""

    def __init__(self, label):
        self.label = label
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    def show(self):
        print("Label: {}".format(self.label))
        print("Switch is on?", self.switchIsOn)
        print("Brightness is: {}".format(self.brightness))

# Create first DimmerSwitch, turn it on, and raise the level twice.
oDimmer1 = DimmerSwtich("Dimmer1")
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()
oDimmer1.show()
print("******************************")

# Create second DimmerSwitch, turn it on, and raise the level 3 times.
oDimmer2 = DimmerSwtich("Dimmer2")
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.show()
print("**********************************************")

#Create third DimmerSwitch, using the defualt settings
oDimmer3 = DimmerSwtich("Dimmer3")
oDimmer3.show()
print("************************************")

# Ask each switch to show itself
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()
print("******************************************")
""" DimmerSwitch_Model2_Instatiation"""
print(type(oDimmer1))
print(oDimmer1)
print(type(oDimmer2))
print(oDimmer2)
print(type(oDimmer3))
print(oDimmer3)
"""The first line in each grouping tells us the data type. Instead of a built-in
type like integer or float, we see that all three objects are of the
programmer-defined DimmerSwitch type. (The __main__ indicates that the
DimmerSwitch code was found inside our single Python file, not imported
from any other file.)
The second line of each grouping contains a string of characters. Each
string represents a location in the memory of the computer. The memory
location is where all the data associated with each object can be found.
Notice each object is in a different location in memory. If you run this code
on your computer, you will most likely get different values, but the actual
values do not matter to understanding the concept.
All DimmerSwitch objects report the same type: class DimmerSwitch.
The extremely important takeaway is that the objects all refer to the code of
the same class, which really only exists in one place. When your program
starts running, Python reads through all the class definitions and remembers
the locations of all the classes and their methods. """
print("*****************************")
#displaying the instance variables inside the object:
print("oDimmer1 variables: {}".format(vars(oDimmer1)))
print("oDimmer2 variables: {}".format(vars(oDimmer2)))
print("oDimmer3 variables:", vars(oDimmer3))

