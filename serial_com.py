import os
import serial
from datetime import datetime

# comm port and file
commPort = "/dev/ttyACM0" # PUT YOUR SERIAL PORT HERE.

DEFAULT_BAUDRATE = 9600 # To use in serial communication

# Create a serial communication
print("Starting serial communication...\n")
ser = serial.Serial(commPort, DEFAULT_BAUDRATE)

while(True):
    if (ser.inWaiting()):
        serial_data = ser.readline()
        print(serial_data)