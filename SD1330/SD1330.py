# https://www.electroniclinic.com/ssd1306-oled-display-with-raspberry-pi-pico/

# https://github.com/makerportal/rpi-pico-ssd1306

from machine import Pin, I2C, ADC
from lib.ssd1306 import SSD1306_I2C
from lib.oled import Write, GFX, SSD1306_I2C
from lib.oled.fonts import ubuntu_mono_15, ubuntu_mono_20
import time
from libs.neopixel import Neopixel


#
#	Configure the hardware
#

# configure the display
WIDTH =128
HEIGHT= 64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

# configure the fonts
write15 = Write(oled, ubuntu_mono_15)
write20 = Write(oled, ubuntu_mono_20)

# configure the potentiometer
pot = ADC(Pin(27))

# configure the button
modeSelector = Pin(15, Pin.IN, Pin.PULL_DOWN)
colourSet = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Configure the Neopixel
pixel = Neopixel(1, 0, 28, "GRB")

#
#	Configure the variables
#

# UI Mode
mode = 0	#0 Red, 1 Green, 2 Blue, 3 Brightness
modeText = ("Red       ", "Green     ", "Blue      ", "Brightness")


# colours
cRed = 0
cGreen = 255
cBlue = 0
cBright = 255

# Get the potentiometer value converted to 1 to 256
def GetPot():
    return int(pot.read_u16()/256)

# Return the value of the selected colour
def GetColour():
    if mode == 0:
        return cRed
    elif mode == 1:
        return cGreen
    elif mode == 2:
        return cBlue
    else:
        return cBright
    
# Set the value of the colour specified by the current mode
def SetColour(pValue):
    global cRed, cGreen, cBlue, cBright
    
    if mode == 0:
        cRed = pValue
    elif mode == 1:
        cGreen = pValue
    elif mode == 2:
        cBlue = pValue
    else:
        cBright = pValue    
    
# display the current mode and it's selected value
def DisplaySetMode():
    write15.text("Mode: " + modeText[mode] + ": " , 0, 0)
    
    #current value the selected mode
    write15.text("Value: " + str(GetColour())+ '    ', 0, 20)
    oled.show()

# Set the mode of the neopixel
def SetNeoPixel():
    pixel.fill((cRed, cGreen, cBlue))
    pixel.brightness(cBright)
    pixel.show()     
    

DisplaySetMode()

# doings of the things
while True:

    if modeSelector.value():
        mode += 1        
        if mode > 3:
            mode = 0
            
        DisplaySetMode()
        
    
    if colourSet.value():
        SetColour(GetPot())
        DisplaySetMode()
        SetNeoPixel()
    
    
    
    
    # Output the potentiometer value
    write15.text("Pot: " + str(GetPot()) + '    ', 0, 40)    
    oled.show()     
   




