# https://www.circuitschools.com/how-to-use-adc-on-raspberry-pi-pico-in-detail-with-micropython-example/

from machine import Pin, ADC
import utime
 
potentiometer_value = machine.ADC(28)
 
while True:
    potreading = potentiometer_value.read_u16()     
    print("potADC: ",potreading)	#max value of 65535
    utime.sleep(0.1)