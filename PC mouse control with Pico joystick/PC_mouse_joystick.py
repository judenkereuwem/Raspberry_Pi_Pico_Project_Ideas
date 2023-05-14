#Title: Control PC with Raspberry Pi Pico joystick
#Author: Jude Nkereuwem
#Date: May, 2023

import pyautogui
import serial
import time


#Serial comm config
ser = serial.Serial('COM13', 115200)
time.sleep(2)


while True:

    #Read incomming data from Pico
    b = ser.readline().decode('ascii').strip()
    print("Current Status: ", b)
    
    if b == "up":
        pyautogui.moveRel(0, -10, duration=0)
    elif b == "down":
        pyautogui.moveRel(0, 10, duration=0)
    elif b == "left":
        pyautogui.moveRel(-10, 0, duration=0)
    elif b == "right":
        pyautogui.moveRel(10, 0, duration=0)
    elif b == "pressed":
        pyautogui.click()

    time.sleep(0.01)
    

ser.close()  
