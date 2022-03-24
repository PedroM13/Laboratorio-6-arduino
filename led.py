import pyfirmata2
import time
PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)

it = pyfirmata2.util.Iterator(board)
it.start()

board.digital[3].mode = pyfirmata2.INPUT
n=0
f=0
while True:
    sw = board.digital[3].read()
    if sw is True:
        #board.digital[2].write(1)
        #time.sleep(5)
        n=n+1
        
      
    
    if n==2:
        print(" LED VERDE ENCENDIDA ")
        board.digital[2].write(1)
        time.sleep(5)    
        n=n+1 
        print(" LED VERDE APAGADA ")
    else:
        board.digital[2].write(0)
        time.sleep(0.1)
        
        

    if n==5:
        print(" LED AZUL ENCENDIDA ")
        board.digital[4].write(1)
        time.sleep(5)
        n=0
        print(" LED AZUL APAGADA ")
    else:
        board.digital[4].write(0)
        time.sleep(0.1)
        
   
    
