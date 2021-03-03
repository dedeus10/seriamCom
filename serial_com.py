import os
import serial
from datetime import datetime
import numpy as np
import pandas as pd

# comm port and file
commPort = "/dev/ttyACM0" # PUT YOUR SERIAL PORT HERE.

DEFAULT_BAUDRATE = 57600 # To use in serial communication
TIME_SAMPLE = 5
# Create a serial communication
print("Starting serial communication...\n")
ser = serial.Serial(commPort, DEFAULT_BAUDRATE)
sample = 0
while(True):
    #Random value different than zero
    second_start=10
    #Wait until second 0 to sync signal
    while(second_start != 0):
        #Get current time
        time_init = datetime.now()
        time_init = time_init.strftime("%H:%M:%S")
        aux = str(time_init).split(":")
        hour_start = int(aux[0])
        minute_start = int(aux[1])
        second_start = int(aux[2])
        print("Waiting to start...", time_init)

    
    print(">>Starting Experiment...Please wait")

    miss=0
    ecg_data, timestamps = [],[]

    while(True):
        #Wait until serial is available
        if (ser.inWaiting()):
            #Get current time
            time_now = datetime.now()
            time_now = time_now.strftime("%d-%m-%Y_%H:%M:%S")
            aux = str(time_now).split("_")
            aux2 = aux[1].split(":")
            h = int(aux2[0])
            m = int(aux2[1])

            #Get data from serial
            serial_data = ser.readline()
            serial_data = str(serial_data)
            serial_data = serial_data.replace("b'","")
            serial_data = serial_data.replace("\\r","")
            serial_data = serial_data.replace("\\n'","")
            try:
                serial_data = int(serial_data)
                #print("Timestamps: ", time_now, " value: ", (serial_data))
                ecg_data.append(serial_data)
                timestamps.append(time_now)
            except:
                miss+=1
                pass
            
            if(int(abs(m-minute_start)) >= TIME_SAMPLE):
                ecg_data = np.asarray(ecg_data)
                filename = 'luis_ecg_data_'+time_now.replace(':','_')+'.csv'
                df = pd.DataFrame(np.asarray([timestamps, ecg_data]).T, columns=['Timestamps', 'ECG'])
                df.to_csv(filename)
                sample+=1
                print("Data stored... SAMPLE: ", sample)
                print("Misses: ", miss)
                
                break