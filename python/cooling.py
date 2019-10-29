#i need a 3.5 volt fan but dont ;-;
#heres the code for the hypothetical cooling system

import io
import RPi.GPIO as GPIO
from time import sleep 


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
while True:
    f = open("/sys/class/thermal/thermal_zone0/temp", "r")
    t = float(f.readline())
    tC = t/1000
    tF = 9.0/5.0 * tC + 32

    if tF > 112:
        GPIO.output(8, GPIO.HIGH)
    else:
        GPIO.output(8, GPIO.LOW)
    
