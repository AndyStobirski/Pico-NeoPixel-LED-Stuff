import time
import random
from machine import Pin, Timer
from libs.neopixel import Neopixel

#
# Our Blinking frog
#
class Frog:

    # pRandomBlinkPeriod - time, in millisecond, when to attempt a blink
    # pDataPin - GP pin used for Neopixel data
    # pStateMachine - unique state machine for frog
    # pEyeColour - colour of frog eye (R,G,B) where 0-255 for each value
    def __init__(self, pRandomBlinkPeriod, pDataPin, pStateMachine, pEyeColour):
        
        self.Name = "Frog" + str(pDataPin)
        
        self.Eyes = Neopixel(2, pStateMachine, pDataPin, "GRBW")
        
        self.ColourEye = pEyeColour
        self.ColourEyeClosed = (0,0,0)
        
        # Indicates blink state
        self.Blinking = False
        
        #the dice to roll to check if we can   
        self.BlinkProbability = (1,4)
        
        # This does the actual blinking
        self.tmrAttemptBlinkTimer = Timer()        
        self.tmrAttemptBlinkTimer.init(period=pRandomBlinkPeriod, mode=Timer.PERIODIC, callback=self.AttempBlink)        
    
        #used to fade in / out eyes
        self.tmrEyesMove = Timer()
        
        #hold the eyes in current colour state
        self.tmrEyesHold= Timer()
        
        #Control the blinking
        self.BlinkCount = 255	
        self.BlinkPeriod = 2	#period of timer controlling eye fade in and out
        self.BlinkStep = 5	
        self.BlinkEyesHold = 200 #period eyes held closed for 
    



# Set eye brightness
    def SetEyeBrightness(self, pBright):
        #print("Bright: "+ str(pBright))
        self.Eyes.brightness(pBright)
        self.Eyes.fill(self.ColourEye)
        self.Eyes.show() 
    
    
    # Roll a dice every time it's called to see if frog can blink
    # We use two timers for the blink: one to fade rapidly in and out,
    # and the other to hold the current state
    def AttempBlink(self,timer):
        if self.Blinking == True:
            return
        
        if random.randint(self.BlinkProbability[0],self.BlinkProbability[1]) == self.BlinkProbability[0]:        
            self.Blink()
    
    
    # Perform a blink
    def Blink(self):
        print(self.Name + " blinked")
        self.Blinking = True
        self.BlinkCount = 255
        self.BlinkStep = -abs(self.BlinkStep)	#Step is a minus number, we're counting down
        
        # Init the timer to begin fade down
        self.tmrEyesMove.init(period = self.BlinkPeriod, mode = Timer.PERIODIC, callback = self.EyesMove)        
        
    # fade the eyes in or out, dependant upon the self.BlinkStep value
    def EyesMove(self, timer):
        
        self.BlinkCount += self.BlinkStep
    
        self.SetEyeBrightness(self.BlinkCount)
    
        if self.BlinkCount >= 255:	#blink has finished
            self.tmrEyesMove.deinit()
            self.Blinking = False
        elif self.BlinkCount < 0:
            # eyes are closed, activate the timer to open them after a short time
            self.tmrEyesMove.deinit()  
            self.tmrEyesHold.init(period = self.BlinkEyesHold, mode = Timer.ONE_SHOT, callback = self.EyesHold)
                  
    
    # Keep the eyes closed for the timer period, them start EyesMove to open them
    def EyesHold(self, timer):
        self.BlinkStep = abs(self.BlinkStep) #force to a positive
        self.tmrEyesMove.init(period=self.BlinkPeriod, mode=Timer.PERIODIC, callback=self.EyesMove)
    
frog1 = Frog(1000, 28, 0, (8,0,0))	#GP28
frog2 = Frog(1300, 16, 1, (0,8,0))	#GP16


