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
from multiprocessing import *

#Raspberry Pi set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Motor set up
#Rotation and delay variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
delay = .0001

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

def spin():
  GPIO.output(BIG_STEP, GPIO.HIGH)
  time.sleep(delay)
  GPIO.output(BIG_STEP, GPIO.LOW)
  time.sleep(delay)

p = Process(target=spin)

#spin function
def spinProgram():
  print("hi")
  p.start()
  p.join()

#Stop function
def stop():
  p.terminate()

#Button set up
spinButton  = Button(screen, text = "Spin", font = myFont, bg = "lightgreen", command = spinProgram, height = 2 , width = 6) 
spinButton.place(x=150, y=0)

stopButton  = Button(screen, text = "STOP", font = myFontLarge, bg = "red", command = stop, height = 2 , width = 8) 
stopButton.place(x=150, y=175)

mainloop()
