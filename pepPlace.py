from Tkinter import *
import tkFont
import RPi.GPIO as GPIO
import time
import threading
import sys
#import datetime
#import pyfireconnect
#from firebase import firebase
#import urllib
#import json
#import os

#WARNING: MAY NOT END PROPERLY...14 changed for newer nums

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

# Not running at start
global isRunning
isRunning = False

# 7 inch function
def sevenProgram():
  global isRunning
  if(isRunning == False):
    print("7")
    seven = threading.Thread(target=pepPizza, args=(0.0000784,0.0004270,0.0001721,0.0003031,9.504132231,14500))
    seven.start()

# 10 inch function hi
def tenProgram():
  global isRunning
  if(isRunning == False):
    print("10")
    ten = threading.Thread(target=pepPizza, args=(0.0000506,0.0005740,0.0000895,0.0004621,19.83471074,17750))
    ten.start()

# 12 inch function
def twelveProgram():
  global isRunning
  if(isRunning == False):
    print("12")
    twelve = threading.Thread(target=pepPizza, args=(0.0000630,0.0004610,0.0000803,0.0004805,28.92561983,19500))
    twelve.start()

# 14 inch function
def fourteenProgram():
  global isRunning
  if(isRunning == False):
    print("14")
    fourteen = threading.Thread(target=pepPizza, args=(0.0000515,0.0002613,0.0000552,0.000123,25,22500))
    fourteen.start()

# Pep pizza function given 2 linear functions, mx+b, time, and amount to move at end
def pepPizza(mSpin,bSpin,mMove,bMove,totalTime,reps):
  global isRunning
  isRunning = True
  center()
  slice(26)
  spin(mSpin,bSpin)
  move(IN,mMove,bMove)
  time.sleep(3*totalTime/4)
  stopAll()
  # Move slower at end test
  slice(20)
  spin(0,mSpin*totalTime*(3/2)+bSpin) # if 3/2 is bigger it will spin slower
  time.sleep(totalTime/4)
  stopAll()
  back(reps)

# Slice function
def slice(speed):
    # Create rpm for dc
    global dc
    dc.start(speed)

# Spin functions
def spin(m,b):
    global spinning
    spinning = True
    
    # Set direction of spin
    GPIO.output(BIG_DIR, 0)

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
      delay = m*(time.time()-startTime)+b
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
  move = threading.Thread(target=moveFunc, args=(m,b))
  # Start new thread
  move.start()
    
def moveFunc(m,b):
  while moving:
    if moving == False:
      break
    else:
      delay = m*(time.time()-startTime)+b
      GPIO.output(SMALL_STEP, GPIO.HIGH)
      time.sleep(delay)
      GPIO.output(SMALL_STEP, GPIO.LOW)
      time.sleep(delay)

# Move to center (used to be 10000)
def center():
  GPIO.output(SMALL_DIR, IN)
  for i in range(6000):
      GPIO.output(SMALL_STEP, GPIO.HIGH)
      time.sleep(.000001)
      GPIO.output(SMALL_STEP, GPIO.LOW)
      time.sleep(.000001)
  
  # Create start time var
  global startTime
  startTime = time.time()

# End function to move out
def back(amt):
  GPIO.output(SMALL_DIR, OUT)
  for i in range(amt):
      GPIO.output(SMALL_STEP, GPIO.HIGH)
      time.sleep(.000001)
      GPIO.output(SMALL_STEP, GPIO.LOW)
      time.sleep(.000001)

# Stop functions
def stopSlicing():
  global dc
  dc.stop()

def stopSpinning():
  global spinning
  spinning = False
  
def stopMoving():
  global moving
  moving = False

def stopAll():
  try:
    stopSlicing()
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
  global isRunning
  isRunning = False

# Button set up
fourteenButton  = Button(screen, text = "14 in.", font = myFont, bg = "lightgreen", command = fourteenProgram, height = 2 , width = 4) 
fourteenButton.place(x=450, y=0)

twelveButton  = Button(screen, text = "12 in.", font = myFont, bg = "lightgreen", command = twelveProgram, height = 2 , width = 4) 
twelveButton.place(x=300, y=0)

tenButton  = Button(screen, text = "10 in.", font = myFont, bg = "lightgreen", command = tenProgram, height = 2 , width = 4) 
tenButton.place(x=150, y=0)

sevenButton  = Button(screen, text = "7 in.", font = myFont, bg = "lightgreen", command = sevenProgram, height = 2 , width = 4) 
sevenButton.place(x=0, y=0)

stopButton  = Button(screen, text = "STOP", font = myFontLarge, bg = "red", command = stopAll, height = 2 , width = 6) 
stopButton.place(x=100, y=160)

mainloop()
