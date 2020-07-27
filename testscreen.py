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
b_delay = .0015 # Big stepper delay
s_delay = .000075 # Small stepper delay

#Big stepper motor set up
BIG_DIR = 21   # Direction GPIO Pin
BIG_STEP = 22  # Step GPIO Pin

GPIO.setup(BIG_DIR, GPIO.OUT)
GPIO.setup(BIG_STEP, GPIO.OUT)

#Small stepper motor set up
SMALL_DIR = 16   # Direction GPIO Pin
SMALL_STEP = 18  # Step GPIO Pin

GPIO.setup(SMALL_DIR, GPIO.OUT)
GPIO.setup(SMALL_STEP, GPIO.OUT)

#DC motor set up
rpwm = 5
lpwm = 7

GPIO.setup(rpwm,GPIO.OUT)
GPIO.setup(lpwm,GPIO.OUT)
GPIO.output(rpwm, GPIO.LOW)
GPIO.output(lpwm,GPIO.LOW)

#TK screen set up
screen = Tk()
screen.overrideredirect(1)
screen.geometry('800x480')
screen.title("Test Screen")

#Fonts for screen
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')
myFontLarge = tkFont.Font(family = 'Helvetica', size = 64, weight = 'bold')

#Functions for starting and stopping spin
def spinProgram():
    global spinning  #create global
    spinning = True

    # Create new thread
    spin = threading.Thread(target=spinFunc)
    # Start new thread
    spin.start()
    
def spinFunc():
  while spinning:
    if spinning == False:
      break
    else:
      GPIO.output(BIG_STEP, GPIO.HIGH)
      time.sleep(b_delay)
      GPIO.output(BIG_STEP, GPIO.LOW)
      time.sleep(b_delay)

def stopSpinning():
  global spinning
  spinning = False

#Functions for moving motor in and out
def inProgram():
    global movingIn  #create global
    movingIn = True
    global movingOut
    movingOut = False

    # Create new thread
    moveIn = threading.Thread(target=inFunc)
    # Start new thread
    moveIn.start()
    
def inFunc():
  num = 1
  while movingIn:
    if movingIn == False:
      break
    else:
      num = -2.6666666666666*(10**-15)*((num/1000.0)**4)+1.0666666666666*(10**-11)*((num/1000.0)**3)-1.333333333333*(10**-8)*((num/1000.0)**2)+5.333333333333*(10**-6)*(num/1000.0)
      GPIO.output(SMALL_DIR, CCW)
      GPIO.output(SMALL_STEP, GPIO.HIGH)
      time.sleep(num)
      GPIO.output(SMALL_STEP, GPIO.LOW)
      time.sleep(num)

def outProgram():
    global movingOut  #create global
    movingOut = True
    global movingIn
    movingIn = False

    # Create new thread
    moveOut = threading.Thread(target=outFunc)
    # Start new thread
    moveOut.start()
    
def outFunc():
  while movingOut:
    if movingOut == False:
      break
    else:
      GPIO.output(SMALL_DIR, CW)
      GPIO.output(SMALL_STEP, GPIO.HIGH)
      time.sleep(s_delay)
      GPIO.output(SMALL_STEP, GPIO.LOW)
      time.sleep(s_delay)

def stopMoving():
  global movingIn
  global movingOut
  movingIn = False
  movingOut = False
  
#Functions for slicing
def sliceProgram():
    global slicing  #create global
    slicing = True

    # Create rpm for dc
    global dc
    global speed
    dc = GPIO.PWM(rpwm, 50)
    dc.start(speed)

def stopSlicing():
  global dc
  global slicing
  slicing = False
  dc.stop()
  
def faster():
  global speed
  global slicing
  speed = speed + 1
  if slicing == True:
    global dc
    dc.stop()
    dc.start(speed)
  rpms.delete(1.0,END)
  rpms.insert(END, str(speed))
  
def slower():
  global speed
  global slicing
  speed = speed - 1
  if slicing == True:
    global dc
    dc.stop()
    dc.start(speed)
  rpms.delete(1.0,END)
  rpms.insert(END, str(speed))
  
#Stop everything
def stopAll():
  #All variables False
  global slicing
  slicing = False
  global movingIn
  global movingOut
  movingIn = False
  movingOut = False
  global spinning
  spinning = False
  #All motors stop
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
    
#Button set up
stopButton  = Button(screen, text = "STOP", font = myFontLarge, bg = "red", command = stopAll, height = 2 , width = 5) 
stopButton.place(x=175, y=110)

inButton  = Button(screen, text = "IN", font = myFont, bg = "green", command = inProgram, height = 2 , width = 4) 
inButton.place(x=5, y=10)
stopMoveButton  = Button(screen, text = "STOP", font = myFont, bg = "blue", command = stopMoving, height = 2 , width = 4) 
stopMoveButton.place(x=5, y=160)
outButton  = Button(screen, text = "OUT", font = myFont, bg = "purple", command = outProgram, height = 2 , width = 4) 
outButton.place(x=5, y=310)

spinButton  = Button(screen, text = "SPIN", font = myFont, bg = "yellow", command = spinProgram, height = 2 , width = 4) 
spinButton.place(x=450, y=85)
stopSpinButton  = Button(screen, text = "STOP", font = myFont, bg = "orange", command = stopSpinning, height = 2 , width = 4) 
stopSpinButton.place(x=450, y=240)

rpms = Text(screen, font = myFont, width=2, height=1)
rpms.place(x=270, y=5)
global speed
speed = 25
rpms.insert(END, str(speed))
global slicing
slicing = False
fasterButton = Button(screen, text = "<", font = myFont, bg = "pink", command = slower, height = 1 , width = 2)
fasterButton.place(x=185, y=5)
slowerButton = Button(screen, text = ">", font = myFont, bg = "grey", command = faster, height = 1 , width = 2)
slowerButton.place(x=335, y=5)

startSliceButton = Button(screen, text = "SLICE", font = myFont, bg = "aqua", command = sliceProgram, height = 1 , width = 4)
startSliceButton.place(x=175, y=375)
stopSliceButton = Button(screen, text = "STOP", font = myFont, bg = "violet", command = stopSlicing, height = 1 , width = 4)
stopSliceButton.place(x=320, y=375)

mainloop()
