from Tkinter import *
import tkFont
import RPi.GPIO as GPIO
import time
import sys
#import serial
import datetime
#import pyfireconnect
#from firebase import firebase
#import urllib
import json
import os
import threading

#Raspberry Pi set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Motor set up
#Rotation and delay variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
delay = .00075

#Big stepper motor set up
BIG_DIR = 21   # Direction GPIO Pin
BIG_STEP = 22  # Step GPIO Pin

GPIO.setup(BIG_DIR, GPIO.OUT)
GPIO.setup(BIG_STEP, GPIO.OUT)

#TK screen set up
screen = Tk()
screen.overrideredirect(1)
screen.geometry('800x480')
screen.title("Big Spinner")

#Fonts for screen
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')
myFontLarge = tkFont.Font(family = 'Helvetica', size = 80, weight = 'bold')

def spinProgram():
    global running  #create global
    running = True

    # Create new thread
    t = threading.Thread(target=func)
    # Start new thread
    t.start()
    
def func():
  while running:
    if running == False:
      break
    else:
      GPIO.output(BIG_STEP, GPIO.HIGH)
      time.sleep(delay)
      GPIO.output(BIG_STEP, GPIO.LOW)
      time.sleep(delay)

def stopProgram():
  global running
  running = False

#Button set up
spinButton  = Button(screen, text = "SPIN", font = myFontLarge, bg = "blue", command = spinProgram, height = 2 , width = 8) 
spinButton.place(x=150, y=0)
stopButton  = Button(screen, text = "STOP", font = myFontLarge, bg = "red", command = stopProgram, height = 2 , width = 8) 
stopButton.place(x=150, y=200)

mainloop()
