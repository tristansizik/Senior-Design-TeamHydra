#!/usr/bin/python
import ms5837
import time

sensor = ms5837.MS5837_02BA() # Default I2C bus is 1 (Raspberry Pi 3)

if not sensor.init():
        print ("Sensor could not be initialized")
        exit(1)

# Spew readings

f=open("Data.txt", "w+")

for i in range(3):
    
    if not sensor.read():
	print("Error reading sensor")
	exit(1)
    
    else:
        print("P: %0.1f mbar  %0.3f psi\tT: %0.2f C  %0.2f F") % (
        sensor.pressure(), # Default is mbar (no arguments)
        sensor.pressure(ms5837.UNITS_psi), # Request psi
        sensor.temperature(), # Default is degrees C (no arguments)
        sensor.temperature(ms5837.UNITS_Farenheit)) # Request Farenheit
        f.write("P: %0.1f mbar  %0.3f psi\tT: %0.2f C  %0.2f F" % 
        (sensor.pressure(),sensor.pressure(ms5837.UNITS_psi),
	sensor.temperature(),sensor.temperature(ms5837.UNITS_Farenheit)))
f.close()
exit(1)
