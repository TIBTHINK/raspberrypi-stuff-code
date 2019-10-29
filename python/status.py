import io
import os
from time import sleep

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo !!' then run the script.\nExiting.")

a = input("is this a raspberry pi?: ")

if "yes" in a:
    while True:
        import RPi.GPIO as GPIO

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
        while True:
            f = open("/sys/class/thermal/thermal_zone0/temp", "r")
            t = float(f.readline())
            tC = t/1000
            tF = 9.0/5.0 * tC + 32


            print(round(tF))
            sleep(1)
    else:
        print("sorry but this program will most likely not work on your pc")



