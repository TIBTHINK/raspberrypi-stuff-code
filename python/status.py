import io
from time import sleep 
while True:
    f = open("/sys/class/thermal/thermal_zone0/temp", "r")
    t = f.readline ()
    cputemp = "CPU temp: "+t
    sleep(1)
    print(cputemp)
