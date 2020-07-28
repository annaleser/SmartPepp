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

# Raspberry Pi set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Motor set up
# Rotation and delay variables
OUT = 1     # Clockwise Rotation
IN = 0    # Counterclockwise Rotation

# Big stepper motor set up
BIG_DIR = 21   # Direction GPIO Pin
BIG_STEP = 22  # Step GPIO Pin

GPIO.setup(BIG_DIR, GPIO.OUT)
GPIO.setup(BIG_STEP, GPIO.OUT)

# Small stepper motor set up
SMALL_DIR = 16   # Direction GPIO Pin
SMALL_STEP = 18  # Step GPIO Pin

GPIO.setup(SMALL_DIR, GPIO.OUT)
GPIO.setup(SMALL_STEP, GPIO.OUT)

# DC Motor set up
rpwm = 5
lpwm = 7

GPIO.setup(rpwm,GPIO.OUT)
GPIO.setup(lpwm,GPIO.OUT)
GPIO.output(rpwm, GPIO.LOW)
GPIO.output(lpwm,GPIO.LOW)

global dc
dc = GPIO.PWM(rpwm, 50)

# TK screen set up
screen = Tk()
screen.overrideredirect(1)
screen.geometry('800x480')
screen.title("Sm^rt Pepp")

# Fonts for screen
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')
myFontLarge = tkFont.Font(family = 'Helvetica', size = 80, weight = 'bold')

# 7 inch function
def sevenProgram():
  print("7")

# 10 inch function
def tenProgram():
  print("10")

# 12 inch function
def twelveProgram():
  print("12")
  twelve = threading.Thread(target=pepPizza, args=(0.0010318,0.0103844,0.0000803,0.0004948))
  twelve.start()

# 14 inch function
def fourteenProgram():
  print("14")

# Pep pizza function
def pepPizza(mSpin,bSpin,mMove,bMove):
  center()
  slice(41)
  spin(mSpin,bSpin)
  move(IN,mMove,bMove)
  time.sleep(29.78723404)
  stopAll()

# Slice functions
def slice(speed):
    global slicing  #create global
    slicing = True

    # Create rpm for dc
    global dc
    dc.start(speed)

# Spin functions
def spin(m,b):
    global spinning  #create global
    spinning = True

    # Create new thread
    spin = threading.Thread(target=spinFunc, args=(m,b))
    # Start new thread
    spin.start()
    
def spinFunc(m,b):
  global startTime
  while spinning:
    if spinning == False:
      break
    else:
      delay = m*(startTime-time.time())+b
      GPIO.output(BIG_STEP, GPIO.HIGH)
      time.sleep(delay)
      GPIO.output(BIG_STEP, GPIO.LOW)
      time.sleep(delay)

# Move functions
def move(direction,m,b):
  global moving
  moving = True
    
  # Set direction to move
  GPIO.output(SMALL_DIR, direction)

  # Create new thread
  move = threading.Thread(target=moveFunc, args=(delay))
  # Start new thread
  move.start()
    
def moveFunc(m,b):
  while movingIn:
    if movingIn == False:
      break
    else:
      delay = m*(startTime-time.time())+b
      GPIO.output(SMALL_STEP, GPIO.HIGH)
      time.sleep(delay)
      GPIO.output(SMALL_STEP, GPIO.LOW)
      time.sleep(delay)

#Move to center
def center():
  for i in range(10000):
      GPIO.output(SMALL_DIR, IN)
      GPIO.output(SMALL_STEP, GPIO.HIGH)
      time.sleep(.000075)
      GPIO.output(SMALL_STEP, GPIO.LOW)
      time.sleep(.000075)
  global startTime
  startTime = time.time()

# Stop functions
def stopSlicing():
  global dc
  global slicing
  slicing = False
  dc.stop()

def stopSpinning():
  global spinning
  spinning = False
  
def stopMoving():
  global moving
  moving = False

def stopAll():
  try:
    dc.stop()
  except:
    pass
  try:
    stopSpinning()
  except:
    pass
  try:
    stopMoving()
  except:
    pass

# Button set up
fourteenButton  = Button(screen, text = "14 inch", font = myFont, bg = "lightgreen", command = fourteenProgram, height = 2 , width = 6) 
fourteenButton.place(x=610, y=0)

twelveButton  = Button(screen, text = "12 inch", font = myFont, bg = "lightgreen", command = twelveProgram, height = 2 , width = 6) 
twelveButton.place(x=406, y=0)

tenButton  = Button(screen, text = "10 inch", font = myFont, bg = "lightgreen", command = tenProgram, height = 2 , width = 6) 
tenButton.place(x=203, y=0)

sevenButton  = Button(screen, text = "7 inch", font = myFont, bg = "lightgreen", command = sevenProgram, height = 2 , width = 6) 
sevenButton.place(x=0, y=0)

stopButton  = Button(screen, text = "STOP", font = myFontLarge, bg = "red", command = stopAll, height = 2 , width = 8) 
stopButton.place(x=150, y=175)

mainloop()
