import time
from machine import Pin, Timer
from random import randrange
from libs.neopixel import Neopixel
 
numpix = 11	# Number of pixels on the strip												
pixels = Neopixel(numpix, 0, 28, "GRB")

lightBlue = (0,0,96)
lightRed = (96,0,0)

off = (0,0,0)

ledHours = (0,5)
ledMinutes = (5,11)


pixels.brightness(32)

#pixels.set_pixel(1, lightBlue)
#pixels.show()

#
#	Set the led range, derived from pPadLength
#	to the value specified by pValue
#
def setValues (pValue, pPadLength):
    
    ledColour = lightRed
    ledRange = ledHours	#0,5
    if pPadLength == 6:
        ledRange = ledMinutes	#6,11
        ledColour = lightBlue
    
    b = intToBin(pValue,pPadLength)
 
    for p in range(ledRange[0],ledRange[1]):
        if b[p-ledRange[0]] ==  '1':
            pixels.set_pixel(p, ledColour)
        else:
            pixels.set_pixel(p, off)
            
    pixels.show()

#
#	Convert pVal to it's binary representation of length pPadlen
#	
def intToBin(pVal, pPadLen):
    b = bin(pVal)	#returns 0b....
    b = '000000' + b[-(len(b)-2):]	#trim off the first two chars
    b = b[-pPadLen:]	#get the right pPadLen characters
    return b

hour = 0
minute = 0

timer = Timer()

def counter(timer):
    
    global hour
    global minute
    
    setValues(minute,6)
    setValues(hour,5)

    minute+=1
    if minute > 59:
        minute = 0
        hour += 1
        if hour > 23:
            hour = 0
    
    pixels.show()
    
timer.init(freq=20, mode=Timer.PERIODIC, callback=counter)


    
