
#Overload protection

from picozero import LED, Button, Speaker
from time import sleep


speaker = Speaker(11)

button1 = Button(12)
button2 = Button(13)
button3 = Button(14)
button4 = Button(15)

led1 = LED(19)
led2 = LED(18)
led3 = LED(17)
led4 = LED(16)

led1_state = 0
led2_state = 0
led3_state = 0
led4_state = 0

total_led = 0


while True:
    
    #LED 1
    if button1.is_pressed and led1_state == 0:
        led1_state = 1
        if led1_state == 1:
            led1.on()
            total_led = total_led+1
            
    elif button1.is_pressed and led1_state == 1:
        led1_state = 0
        if led1_state == 0:
            led1.off()
            total_led = total_led-1
            
    #LED 2
    if button2.is_pressed and led2_state == 0:
        led2_state = 1
        if led2_state == 1:
            led2.on()
            total_led = total_led+1
            
    elif button2.is_pressed and led2_state == 1:
        led2_state = 0
        if led2_state == 0:
            led2.off()
            total_led = total_led-1
            
    #LED 3
    if button3.is_pressed and led3_state == 0:
        led3_state = 1
        if led3_state == 1:
            led3.on()
            total_led = total_led+1
            
    elif button3.is_pressed and led3_state == 1:
        led3_state = 0
        if led3_state == 0:
            led3.off()
            total_led = total_led-1
            
    #LED 4
    if button4.is_pressed and led4_state == 0:
        led4_state = 1
        if led4_state == 1:
            led4.on()
            total_led = total_led+1
            
    elif button4.is_pressed and led4_state == 1:
        led4_state = 0
        if led4_state == 0:
            led4.off()
            total_led = total_led-1
            
            
    print(total_led)
    sleep(0.3) 
    
    
    if total_led == 4:
        speaker.on()
        
        
    elif total_led < 4:
        speaker.off()
        
        
    



            
            
            
        
    
    


