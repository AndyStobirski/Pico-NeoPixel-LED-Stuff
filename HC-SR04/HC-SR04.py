# https://www.freva.com/hc-sr04-ultrasonic-distance-sensor-with-raspberry-pi-pico/

from machine import Pin
import time

trig = Pin(17, Pin.OUT)
echo = Pin(16, Pin.IN, Pin.PULL_DOWN)

while True:
    trig.value(0)		# To make sure the sensor does not emmit any sound
    time.sleep(0.1)		# We wait for a short period to settle the sensor
    trig.value(1)		# Let the sensor emit a sound
    time.sleep_us(2)	# Emitting for a very short time : 2 microseconds
    trig.value(0)		# Stop emitting the sound
     
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()
        
    # Calculate the distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17165 / 1000000
    distance = round(distance, 0)
    print ('Distance:',"{:.0f}".format(distance),'cm')
    time.sleep(1)