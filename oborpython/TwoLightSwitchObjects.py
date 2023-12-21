"""Object Oriented Two Light Switch project Menok OG 4-15-23"""




class LightSwitch():
    def __init__(self):
        self.switchIsOn = False
    
    def turnON(self):
        self.switchIsOn = True
    
    def turnOff(self):
        self.switchIsOn = False
    
    def show(self):
        print(self.switchIsOn)

oLightSwtich1 = LightSwitch()
oLightSwtich2 = LightSwitch()

oLightSwtich1.show()
oLightSwtich2.show()
oLightSwtich1.turnON()
oLightSwtich2.turnOff()
oLightSwtich1.show()
oLightSwtich2.show()