# Menoko OG 4-14-2023 for OOP project
"""To model a real-world object in code, we need to decide what data will
represent that object’s attributes and what operations it can perform. These
two concepts are often referred to as an object’s state and behavior,
respectively: the state is the data that the object remembers, and the
behaviors are the actions that the object can do.

State and Behavior: Light Switch Example
Listing 2-1 is a software model of a standard two-position light switch
written in procedural Python. This is a trivial example, but it will
demonstrate state and behavior."""
#procedural Light Switch

def turnOn():
    global switchIsOn
    # turn light on
    switchIsOn = True
    
def turnOff():
    global switchIsOn
    #turn light off
    switchIsOn = False
# Main Code
switchIsOn = False # a global Boolean variable

#test code
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)
    