import keyboard
import pyfirmata2
import time
PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)
while True:
    if keyboard.is_pressed('a') and keyboard.is_pressed('y'):
      board.digital[2].write(1)
      time.sleep(.5)
      board.digital[2].write(0) 
      time.sleep(.1)