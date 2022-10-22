from machine import ADC, Pin
import time
from libs.neopixel import Neopixel


numpix = 12	# Number of pixels on the strip												
ring = Neopixel(numpix, 0, 28, "GRB")

ring.fill((255,255,255))
ring.show()


adc = ADC(Pin(27))

while True:
    print(adc.read_u16()/256)
    ring.brightness(int(adc.read_u16()/256))
    ring.fill((255,255,255))
    
    ring.show()
    time.sleep(1)