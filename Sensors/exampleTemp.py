#!/usr/bin/python
import tsys01
from time import sleep

sensor = tsys01.TSYS01()

if not sensor.init():
    print("Error initializing sensor")
    exit(1)

while True:
    if not sensor.read():
        print("Error reading sensor")
        exit(1)
    print("Temperature: %.2f C\t") % (sensor.temperature())
    sleep(0.2)
