
#Include needed libraries
import os
import pandas as pd
import csv
import serial
import time
from datetime import datetime


#Serial comm config
ser = serial.Serial('COM13', 115200)
time.sleep(2)


#Get current date and time for naming csv file
now = datetime.now()
d = datetime(1, 1, 1).now()
dtString = d.strftime('{}_{}_{}'.format(d.hour%12,d.minute,d.second))
dString = now.strftime('%d_%m_%Y')


#Create new .csv file
pathDir = 'file'
filename = f'{dString}_{dtString}.csv'
df = pd.DataFrame() 
df.to_csv(f"{pathDir}/{filename}", index=False, encoding='utf-8')


#Open csv file and add headers
with open(f"{pathDir}/{filename}",'r+') as f:
    f.writelines('Time,temp,light,motion')   #file header
    
    while True:
        #Read incomming data from Pico
        b = ser.readline().decode('ascii').strip()
        print("Data: ", b, "%")

        #Log incoming data from pico and current time to csv file
        now = datetime.now()
        d = datetime(1, 1, 1).now()
        am_pm = 'am' if d.hour<12 else 'pm'
        dtString = d.strftime('{}:{}:{}:{}'.format(d.hour%12,d.minute,d.second, am_pm))
        f.writelines(f'\n{dtString},{b}')
        f.flush()
        
    ser.close() 
