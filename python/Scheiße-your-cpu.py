#!/usr/bin/python3

import time
from time import sleep
import os
import random

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo !!' then run the script.\nExiting.")


a = input("would you like to Scheiße shred your cpu into pieces: ")

if "yes" in a:
    while True:
        os.system("du / -h")
else:
    os.system("clear")
    sleep(.1)
    print("ok whore")
    exit()
