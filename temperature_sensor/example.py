#/usr/bin/python
import tsys01
from time import sleep

sensor = tsys01.TSYS01()

if not sensor.init():
    print("Error initializing sensor")
    exit(1)

f=open("Data.txt", "w+")

for i in range(10):
    
    if not sensor.read():
        print("Error reading sensor")
        exit(1)
        
    temp = sensor.temperature()
    print("%.2f") % (temp)
    f.write("Temperature: %.2f C \r\n" % (sensor.temperature()))
    sleep(0.2)
f.close()


                

