import time
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Rotation and delay variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
delay = .0125

#Big stepper motor set up
BIG_DIR = 21   # Direction GPIO Pin
BIG_STEP = 22  # Step GPIO Pin

GPIO.setup(BIG_DIR, GPIO.OUT)
GPIO.setup(BIG_STEP, GPIO.OUT)

#Small stepper motor set up
SMALL_DIR = 11   # Direction GPIO Pin
SMALL_STEP = 12  # Step GPIO Pin
SMALL_SPR = 200   # Steps per Revolution

GPIO.setup(SMALL_DIR, GPIO.OUT)
GPIO.setup(SMALL_STEP, GPIO.OUT)

#wait = int((1.0/5184)*((3.0*i/3200)-12)**4+1)
#Variables for steppers
print("SMALL")

#SLOW IN
GPIO.output(SMALL_DIR, CCW)

#IN
delay = .0005
for i in range(1000):
    delay =  -0.008*(i-.5)**4+.0005
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(delay)

#OUT
GPIO.output(SMALL_DIR, CW)
for i in range(1000):
    delay =  -0.008*((100-i)-.5)**4+.0005
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(delay)
    
#Clean up pins
GPIO.cleanup()
