import time
import RPi.GPIO as GPIO
import MotorDriver
import multiprocessing

#Board set up
GPIO.setwarnings(False)

#Rotation variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation

#Big stepper motor set up
BIG_DIR = 21   # Direction GPIO Pin
BIG_STEP = 22  # Step GPIO Pin
bigM = MotorDriver.StepMotor(BIG_DIR,BIG_STEP) #Using motor class

#Small stepper motor set up
SMALL_DIR = 11   # Direction GPIO Pin
SMALL_STEP = 12  # Step GPIO Pin
smallM = MotorDriver.StepMotor(SMALL_DIR,SMALL_STEP) #Using motor class

#DC motor set up
in1 = 3
in2 = 5
en = 7

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

#DC Motor commented out for testing of bottom motors
#Create PWM instance with channel and 1000 frequency
#*p=GPIO.PWM(en,1000)
#Start with 25% duty cycle
#*p.start(25)
#The default speed & direction of motor is LOW & Forward....
#SPEED
    #p.ChangeDutyCycle(25 - low, 50 - med, 75 - high)
#DIRECION
    #GPIO.output(in1,GPIO.LOW)
    #GPIO.output(in2,GPIO.LOW)
    #forward: in1 HIGH, in2 LOW
    #backward: in1 LOW, in2 HIGH
    #stop: in1 LOW, in2 LOW
#Stop PWM
#*p.stop()

#Run small stepper inward
print("Small step running in")
smallM.setDirection(CCW)
smallM.runxSteps(100)
while(smallM.p.is_alive()):
  pass

#Run big and small stepper
print("Big and small step running")
smallM.setDirection(CW)
smallM.runxSteps(100)
bigM.runxSteps(100)
while(smallM.p.is_alive() and bigM.p.is_alive()):
  pass
    
#Clean up pins
GPIO.cleanup()
