import io
from time import sleep 

while True:
    f = open("/sys/class/thermal/thermal_zone0/temp", "r")
    t = float(f.readline())
    tC = t/1000
    tF = 9.0/5.0 * tC + 32
    
    print(round(tF))
    sleep(1)
