import os
import serial
from datetime import datetime
import numpy as np

# comm port and file
commPort = "/dev/ttyACM0" # PUT YOUR SERIAL PORT HERE.

DEFAULT_BAUDRATE = 9600 # To use in serial communication
TIME_SAMPLE = 5
# Create a serial communication
print("Starting serial communication...\n")
ser = serial.Serial(commPort, DEFAULT_BAUDRATE)
time_init = datetime.now()
time_init = time_init.strftime("%H:%M")
aux = str(time_init).split(":")
hi = int(aux[0])
mi = int(aux[1])

ecg_data = []
while(True):
    if (ser.inWaiting()):
        time_now = datetime.now()
        time_now = time_now.strftime("%H:%M")
        aux = str(time_now).split(":")
        h = int(aux[0])
        m = int(aux[1])

        serial_data = ser.readline()
        serial_data = str(serial_data)
        serial_data = serial_data.replace("b'","")
        serial_data = serial_data.replace("\\r","")
        serial_data = serial_data.replace("\\n'","")
        try:
            serial_data = int(serial_data)
            print("Timestamps: ", time_now, " value: ", (serial_data))
            ecg_data.append(serial_data)
        except:
            pass
        
        if(int(abs(m-mi)) > TIME_SAMPLE):
            ecg_data = np.asarray(ecg_data)
            np.savetxt('ecg_data.txt', ecg_data)
            break