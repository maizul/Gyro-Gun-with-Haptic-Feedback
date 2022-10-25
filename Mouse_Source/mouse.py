from ast import keyword
import serial
from serial import Serial
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

key = KeyboardController()
mouse = MouseController() 
try:
  ser = serial.Serial('COM4',baudrate = 9600)       # Setting Serial port number and baudrate
  while 1:                                            # While loop to continuesly scan and read data from serial port and execute
      dump = ser.readline()                           # Reading Serial port
      dump = str(dump)                                # Converting byte data into string
      dump = dump[2:-5]                               # Cleaning up the raw data recieved from serial port
      data = dump.split(',')                          # Spliting up the data to individual items in a list. the first item being the data identifier
      print(data)   
      if data[0] == "DATAL":                          # Checking if the identifier is "DATAL" which the Arduino sends the data as the gyro X, Y and Z values
        mouse.move(int(data[1]), int(data[2]))        # Moving the mouse by using the X and Y values after converting them into integer
        
      if data[0] == "DATAB":                          # Checking if the identifier is "DATAB" which the Arduino sends the values for Left/Right button
        if data[1] == 'LMB' :                         # If the Left button is pressed
          mouse.press(Button.left)                    # The corresponding button is pressed and released
          mouse.release(Button.left)
        if data[1] == 'RMB' :                         # If the Right button is pressed
          mouse.press(Button.right)                   # The corresponding button is pressed and released
          mouse.release(Button.right)
          
      if data[0] == "DATAC":                          # Checking if the identifier is "DATAB" which the Arduino sends the values for Left/Right button
        if data[1] == 'W' :                           # If the Left button is pressed
          key.press('w')                              # The corresponding button is pressed and released
          key.release('w')
        if data[1] == 'S' :                           # If the Left button is pressed
          key.press('s')                              # The corresponding button is pressed and released
          key.release('s')
        if data[1] == 'R' :                           # If the Left button is pressed
          key.press('r')                              # The corresponding button is pressed and released
          key.release('r')
            
except:
  print("Device not found or disconnected.")
  k=input("Press any key to exit.")