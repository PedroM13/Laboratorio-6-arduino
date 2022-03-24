from cgi import print_directory
from telnetlib import theNULL
from tkinter import *
import tkinter as tk
from tkinter import font
import pyfirmata2
import time

from setuptools import Command
PORT = pyfirmata2.Arduino.AUTODETECT
board = pyfirmata2.Arduino(PORT)
contador = 0
def calcular():
    global contador
    contador += 1
    if contador==2:
        board.digital[2].write(1)
        time.sleep(10)
        board.digital[2].write(0)
        time.sleep(0.1)    


    



ventana = Tk()
ventana.minsize(width=200, height=300)


titulo = tk.Label(ventana,
 text="LED",
 font=("arial",46),
 bg="lightgreen", fg="darkblue",
 padx=20,pady=20   
)
titulo.pack()


boton = tk.Button(ventana,
text="Prender led",
font=("arial",18),
bg="lightgrey", fg="black",
padx=20, pady=20,
relief="groove", bd=10,
command=calcular
)
boton.pack()
ventana.mainloop()

