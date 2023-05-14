# PC mouse control with Pico joystic

This project helps you control your PC mouse cursor using joystic interfaced with the Raspberry Pi Pico.

Requirements:
-------------

Raspberry Pi Pico:
- Joystick
- Jumper wires
- MicroPython
- "main.py" code - save inside the Pico

PC:
- Windows 10
- Python 3
- PySerial Python library
- Pyautogui Python library
- "PC_mouse_joystick.py" code


Operation
---------
- The Raspberry Pi Pico reads values from joystick.
- Pico sends joystick values to PC via USB cable and Pyserial library.
- PC syncs pico_joystick values with mouse cursor with the help of Pyautogui library.


Run the "PC_mouse_joystick.py" code on your PC, move the joystick in different directions and watch your PC mouse cursor move accordingly. Click on the joystick to enable mouse click on your PC.