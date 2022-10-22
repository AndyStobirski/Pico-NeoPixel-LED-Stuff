from machine import ADC, Pin
import time


adc = ADC(Pin(27))

while True:
    print(adc.read_u16()/256) # convert to a value between 1 and 255
    time.sleep(1)