
import time
from machine import Pin, Timer
from libs.neopixel import Neopixel
 
numpix = 11	# Number of pixels on the strip												
pixels = Neopixel(numpix, 0, 28, "GRB")
 
off = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
white = (255,255,255)
orange = (255,165,0)

# the block of LEDs to draw
colours = (red,green, blue,white,orange)

# set the start of block draw position
posAdjust = 1
posCtr = 0

# block brightness
bright = 1
brightAdjust = 1

pixels.brightness(bright)

timer = Timer()

# Independent function for controlling LED brightness
def brightnessControl(timer):
    
    global bright
    global brightAdjust
    
    pixels.brightness(bright)
    
    bright += brightAdjust
    
    if bright > 255:
        brightAdjust = -1
    elif bright < 1:
        brightAdjust = 1
                


timer.init(freq=3, mode=Timer.PERIODIC, callback=brightnessControl)



while True:
    
    # clear the strip
    for o in range(numpix):
        pixels.set_pixel(o, off)         
    
    # Set the start point
    if posCtr >= 6:
        posAdjust = -1
    elif posCtr == 0:
        posAdjust = 1
    
    # Draw the coloured group of leds
    for p in range(5):
        pixels.set_pixel(posCtr + p, colours[p])
    
    pixels.show()    
    time.sleep(0.3)

    posCtr += posAdjust
    




