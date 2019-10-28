import os
from time import sleep
import random
import sys

os.system = os

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo !!' then run the script.\nExiting.")

print("alright lets get the main programs you use")
sleep(3)
os("clear")
os("apt update")
sleep(2)
os("clear")
print("now lets get thoes damn packages in")
os("apt install -y httrack git openssh python-pip python3-pip g++ ruby")
os("clear")
sleep(1)
print("ok and now for the python packages")
os("pip3 install youtube-dl")

exit()
