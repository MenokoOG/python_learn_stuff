"""DimmerSwitch  object project by Menoko OG 4-15-20230"""

class DimmerSwtich():
    """DimmerSwitch  object project by Menoko OG 4-15-20230"""
    def __init__(self):
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
        print("Switch is on?", self.switchIsOn)
        print("Brightness is:", self.brightness)

#Main Code
oDimmer = DimmerSwtich()

#turn switch onm, and raise level 5 times
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

#Lower the level 2 times, and turn swithc off
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()

#turn switch on, and raise the level 3 times
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()
    

