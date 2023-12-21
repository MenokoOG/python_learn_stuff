"""Menoko OG TV object project 4-15-2023
Building a TV class and then create TV objects"""
#TV Class
class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM =10
        self.volume = self.VOLUME_MAXIMUM // 2 #integer divide
    
    def power(self):
        self.isOn = not self.isOn   #toggle
    
    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False #changing the volume while muted unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume + 1
            
    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume -1
    
    def channellUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0 #wrap around to the first channel
    
    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1 # wrap around to the top channel
    
    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted
        
    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
            # if the newChannel is not in our list of channels, do not do anything
    
    def showInfo(self):
        print()
        print("TV Status:")
        if self.isOn:
            print("    TV is: On")
            print("    Channel is: {}".format(self.channelList[self.channelIndex]))
            if self.isMuted:
                print("    Volume is: {} (sound is muted)".format(self.volume))
            else:
                print("    Volume is: {}".format(self.volume))
        else:
            print("    TV is: Off")

#Main code
oTV = TV()  #creae the TV object

#turn the TV on and show the status
oTV.power()
oTV.showInfo()

#CHange the channel up twice, raise the volume twice, show status
oTV.channellUp()
oTV.channellUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

#Turn TV off, show status, turn TV on, show status
oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

# Lower the volume, mute the sound, show status
oTV.volumeDown()
oTV.mute()
oTV.showInfo()

#change the channel to 11, mute the sound, show status
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()