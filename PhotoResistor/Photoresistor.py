from machine import ADC, Pin
from time import sleep

photoPIN = 28

def readLight(photoGP):
    photoRes = ADC(Pin(28))
    light = photoRes.read_u16()
    light = round(light/65535*100,2)
    return light

while True:
    print("light: " + str(readLight(photoPIN)) +"%")
    sleep(1)