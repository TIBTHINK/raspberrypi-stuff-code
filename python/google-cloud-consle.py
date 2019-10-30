import os
from time import sleep
import random
import sys
import math

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo !!' then run the script.\nExiting.")

print("alright lets get the main programs you use")
sleep(3)
os.system("clear")
os.system("apt update")
sleep(2)
os.system("clear")
print("now lets get thoes damn packages in")
os.system("apt install -y httrack git openssh python-pip python3-pip g++ ruby")
os.system("clear")
sleep(1)
print("ok and now for the python packages")
os.system("pip3 install youtube-dl")

exit()
