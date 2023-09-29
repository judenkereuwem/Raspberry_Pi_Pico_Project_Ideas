
Title: Pico data logger to csv file.

Description: This system takes sensor data from Raspberry Pi Pico then logs it into a .csv file on your PC.

Use case: This can be useful in cases like: when you want to gatther sensor data to train an AI model for anormally detection.


NOTE:
If you are new to the Raspberry Pi Pico: check out my [Beginners Tutorials](https://judeok.wixsite.com/placidlearn/raspberry-pi-pico)



Requirement:

Hardaware:
- PC
- Raspberry Pi Pico
- Compartible USB cable
- LDR
- 10K Resistor
- Breadboard
- Jumper cables

Software:
- PC: Python 3, IDE of choice, PySerial library (pip install pyserial), Pandas (pip install pandas).
- Pico: Micropython, Thonny IDE



Setup:
- Create project folder on your PC - "Pico data logging"
- Inside the project folder, create an empty folder - named "file". (This is where all your csv filles will be saved)
- Copy "main.py" code to Thonny IDE then save it as "main.py" inside the Raspberry Pi Pico the exit Thonny.
- Open "data_logging.py" code with Python IDE on your PC.
- With your Pico still plugged to your computer, run the "data_logging.py" code:
 -- You should see a new file created inside the "file folder - named with the current date and time" (for easy identification of file session)
 -- Once you are done collecting your data, stop the program (Ctrl+C)
 -- You can now vew your data by double clicking on it, or opening it as sheet with tools like MS-Excel.