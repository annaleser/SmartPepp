import time
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Rotation and delay variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
delay = .002

#Big stepper motor set up
BIG_DIR = 21   # Direction GPIO Pin
BIG_STEP = 22  # Step GPIO Pin
BIG_SPR = 200   # Steps per Revolution (360 / 7.5)
BIG_REVS = 6 #Number of times to run loop

GPIO.setup(BIG_DIR, GPIO.OUT)
GPIO.setup(BIG_STEP, GPIO.OUT)

#Small stepper motor set up
SMALL_DIR = 11   # Direction GPIO Pin
SMALL_STEP = 12  # Step GPIO Pin
SMALL_SPR = 200   # Steps per Revolution
IN_REVS = 6 #Number of times to run loop

GPIO.setup(SMALL_DIR, GPIO.OUT)
GPIO.setup(SMALL_STEP, GPIO.OUT)

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
print("Small step running")
step_count = SMALL_SPR
revolutions = IN_REVS

GPIO.output(SMALL_DIR, CCW)
for x in range(step_count*revolutions):
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(delay)

#Run big and small stepper
print("Big step running")
step_count = BIG_SPR
revolutions = BIG_REVS

GPIO.output(BIG_DIR, CW)
GPIO.output(SMALL_DIR, CW)
n = 2
for x in range(n*step_count*revolutions):
    GPIO.output(BIG_STEP, GPIO.HIGH)
    if(x%n == 0):
      GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    if(x%n == 0):
      GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(delay)
    
#Clean up pins
GPIO.cleanup()
