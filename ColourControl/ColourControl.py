from machine import Pin, ADC, Timer
import time
from libs.neopixel import Neopixel
import utime
 
potentiometer_value = machine.ADC(28)

conversion_factor = 3.3/(65536)

_numpix = 1													
_pixel = Neopixel(_numpix, 0, 27, "GRBW")
_pixel.brightness(1)
_pixel.set_pixel(0, (0,0,255))
_pixel.show()

_button = Pin(15, Pin.IN, Pin.PULL_DOWN)
_led = Pin(25, Pin.OUT)

_btnCnt = 1

_red = 0
_green = 32
_blue = 0
 
while True:
    potreading = potentiometer_value.read_u16()
    
    # produces a range of 0 to 65535 for a 10K pot
    #print("potADC: ",potreading)	
    utime.sleep(0.1)
    
    tValue = int(potreading / 256)
    
    if _button.value():
        print ("Button: " + str(_btnCnt))
        _btnCnt += 1
        if _btnCnt > 4:
            _btnCnt = 1
    
    if _btnCnt == 1:
        _red = tValue
    elif _btnCnt == 2:
        _green = tValue
    elif _btnCnt == 3:
        _blue = tValue
    elif _btnCnt == 4:
        _pixel.brightness(tValue)      
    
    print ("B: "+ str(_btnCnt) + " R:" + str(_red) + ", G:" + str(_green) + ", B:"+ str(_blue))
    
    _pixel.set_pixel(0, (_red,_green,_blue))        
        
    _pixel.show()
    
    #print('Brightness ' + str(potreading / 256))
    
    
    
    