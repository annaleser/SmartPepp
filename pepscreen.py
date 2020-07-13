from Tkinter import *
import tkFont
#import RPi.GPIO as GPIO
import time
import sys
#import serial
import datetime
#import pyfireconnect
#from firebase import firebase
#import urllib
import json
import os

#Raspberry Pi set up
#GPIO.setmode(GPIO.BOARD)

#Motor set up
#************************

#TK screen set up
screen = Tk()
screen.overrideredirect(1)
screen.geometry('800x480')
screen.title("Sm^rt Pepp")

#Fonts for screen
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')
myFontSmall = tkFont.Font(family = 'Helvetica', size = 12, weight = 'bold')
myFontMed = tkFont.Font(family = 'Helvetica', size = 20, weight = 'bold')
myFontLarge = tkFont.Font(family = 'Helvetica', size = 64, weight = 'bold')

#7 inch function
def sevenProgram():
  pass

#10 inch function
def tenProgram():
  pass

#12 inch function
def twelveProgram():
  pass

#14 inch function
def fourteenProgram():
  pass

#Stop function
def stop():
  pass

#Button set up
fourteenButton  = Button(screen, text = "14 inch", font = myFont, bg = "lightgreen", command = fourteenProgram, height = 2 , width = 6) 
fourteenButton.place(x=610, y=0)

twelveButton  = Button(screen, text = "12 inch", font = myFont, bg = "lightgreen", command = twelveProgram, height = 2 , width = 6) 
twelveButton.place(x=406, y=0)

tenButton  = Button(screen, text = "10 inch", font = myFont, bg = "lightgreen", command = tenProgram, height = 2 , width = 6) 
tenButton.place(x=203, y=0)

sevenButton  = Button(screen, text = "7 inch", font = myFont, bg = "lightgreen", command = sevenProgram, height = 2 , width = 6) 
sevenButton.place(x=0, y=0)

stopButton  = Button(screen, text = "STOP", font = myFontLarge, bg = "red", command = stop, height = 5 , width = 10) 
stopButton.place(x=200, y=150)

mainloop()
