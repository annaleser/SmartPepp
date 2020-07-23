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
s_delay = .00025
b_delay = .000025

#Big stepper motor set up
BIG_DIR = 21   # Direction GPIO Pin
BIG_STEP = 22  # Step GPIO Pin

GPIO.setup(BIG_DIR, GPIO.OUT)
GPIO.setup(BIG_STEP, GPIO.OUT)

#Small stepper motor set up
SMALL_DIR = 11   # Direction GPIO Pin
SMALL_STEP = 12  # Step GPIO Pin

GPIO.setup(SMALL_DIR, GPIO.OUT)
GPIO.setup(SMALL_STEP, GPIO.OUT)

#DC Motor set up
rpwm = 5
lpwm = 7

GPIO.setup(rpwm,GPIO.OUT)
GPIO.setup(lpwm,GPIO.OUT)
GPIO.output(rpwm, GPIO.LOW)
GPIO.output(lpwm,GPIO.LOW)

p = GPIO.PWM(rpwm, 50)

#TK screen set up
screen = Tk()
screen.overrideredirect(1)
screen.geometry('800x480')
screen.title("Sm^rt Pepp")

#Fonts for screen
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')
myFontSmall = tkFont.Font(family = 'Helvetica', size = 12, weight = 'bold')
myFontMed = tkFont.Font(family = 'Helvetica', size = 20, weight = 'bold')
myFontLarge = tkFont.Font(family = 'Helvetica', size = 80, weight = 'bold')

#7 inch function
def sevenProgram():
  print("7")

def ten():
  print("10")

#10 inch function
def tenProgram():
  global t = Process(target=ten)
  t.start()

#12 inch function
def twelveProgram():
  GPIO.output(BIG_DIR, CW)
  for i in range(1000):
    GPIO.output(BIG_STEP, GPIO.HIGH)
    time.sleep(b_delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    time.sleep(b_delay)

#14 inch function
def fourteenProgram():
  p.start(25)
  GPIO.output(BIG_DIR, CW)
  GPIO.output(SMALL_DIR, CCW)
  for i in range(10000):
    GPIO.output(BIG_STEP, GPIO.HIGH)
    time.sleep(b_delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    time.sleep(b_delay)
  p.stop()

#Stop function
def stop():
  p.stop()
  t.stop()
  GPIO.output(rpwm, GPIO.LOW)
  GPIO.output(lpwm,GPIO.LOW)
  GPIO.output(BIG_STEP, GPIO.LOW)
  GPIO.output(SMALL_STEP,GPIO.LOW)

#Button set up
fourteenButton  = Button(screen, text = "14 inch", font = myFont, bg = "lightgreen", command = fourteenProgram, height = 2 , width = 6) 
fourteenButton.place(x=610, y=0)

twelveButton  = Button(screen, text = "12 inch", font = myFont, bg = "lightgreen", command = twelveProgram, height = 2 , width = 6) 
twelveButton.place(x=406, y=0)

tenButton  = Button(screen, text = "10 inch", font = myFont, bg = "lightgreen", command = tenProgram, height = 2 , width = 6) 
tenButton.place(x=203, y=0)

sevenButton  = Button(screen, text = "7 inch", font = myFont, bg = "lightgreen", command = sevenProgram, height = 2 , width = 6) 
sevenButton.place(x=0, y=0)

stopButton  = Button(screen, text = "STOP", font = myFontLarge, bg = "red", command = stop, height = 2 , width = 8) 
stopButton.place(x=150, y=175)

mainloop()
