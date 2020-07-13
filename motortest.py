import time
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#Rotation variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation

#Big stepper motor set up
BIG_DIR = 11   # Direction GPIO Pin
BIG_STEP = 12  # Step GPIO Pin
BIG_SPR = 48   # Steps per Revolution (360 / 7.5)

GPIO.setup(BIG_DIR, GPIO.OUT)
GPIO.setup(BIG_STEP, GPIO.OUT)

#Small stepper motor set up
SMALL_DIR = 13   # Direction GPIO Pin
SMALL_STEP = 15  # Step GPIO Pin
SMALL_SPR = 48   # Steps per Revolution (360 / 7.5)

GPIO.setup(SMALL_DIR, GPIO.OUT)
GPIO.setup(SMALL_STEP, GPIO.OUT)
GPIO.output(SMALL_DIR, CW)

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

#Run big stepper
step_count = BIG_SPR
delay = .0208

GPIO.output(BIG_DIR, CW)
for x in range(step_count):
    GPIO.output(BIG_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    time.sleep(delay)

time.sleep(.5)
GPIO.output(BIG_DIR, CCW)
for x in range(step_count):
    GPIO.output(BIG_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    time.sleep(delay)

#Run small stepper
step_count = SMALL_SPR
delay = .0208

GPIO.output(SMALL_DIR, CW)
for x in range(step_count):
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(delay)

time.sleep(.5)
GPIO.output(SMALL_DIR, CCW)
for x in range(step_count):
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(delay)
    
#Clean up pins
GPIO.cleanup()
