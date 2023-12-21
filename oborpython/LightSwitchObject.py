"""Object Oriented Light Switch project Menok OG 4-14-23"""




class LightSwitch():
    def __init__(self):
        self.switchIsOn = False
    
    def turnON(self):
        self.switchIsOn = True
    
    def turnOff(self):
        self.switchIsOn = False
    
    def show(self):
        print(self.switchIsOn)

oLightSwtich = LightSwitch()

oLightSwtich.show()
oLightSwtich.turnON()
oLightSwtich.show()
oLightSwtich.turnOff()
oLightSwtich.show()
oLightSwtich.turnON()
oLightSwtich.show()
# oLightSwtich.turnOff()
# oLightSwtich.show()


