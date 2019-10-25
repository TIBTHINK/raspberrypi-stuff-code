#!/usr/bin/python3

import time
from time import sleep
import os
import random

print("1 means yes")
print("2 means no")
sleep(2)
a = input("would you like to make your computer feel pain?: ")

b = int(a)

while b > 0:
    os.system("du / -h")