from machine import Pin, PWM
import neopixel
import time
import random

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
buzzer = PWM(Pin(16))
buzzer.freq(500)

np = neopixel.NeoPixel(machine.Pin(17), 16)

target = random.randint(0,15)
speed = round(random.uniform(0.01, 0.03),2)
    
while True:
    
    for i in range(0, 15):
        print(button.value())
        np[i] = (255,0,0)
        np[target] = (255,255,0)
        np.write()
        time.sleep(speed)
        np[i] = (0,0,0)
        
        while button.value() == 1 and i == target:
            np[target] = (0,255,0)
            np.write()
            buzzer.duty_u16(1000)
            time.sleep(0.5)
            buzzer.duty_u16(0)
        
            target = random.randint(0,15)
        

