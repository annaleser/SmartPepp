import time
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Rotation and delay variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
delay = .000125

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

#Variables for steppers
BIG_SPR = 200   # Steps per Revolution
SPIN = 16 #Amount to spin for full revolution
REPS = 4 #Number of times to run loop

#DC motor set up
rpwm = 5
lpwm = 7

GPIO.setup(rpwm,GPIO.OUT)
GPIO.setup(lpwm,GPIO.OUT)
GPIO.output(rpwm, GPIO.LOW)
GPIO.output(lpwm,GPIO.LOW)

#Set lpwm high to go forward and rpwm high for backward...might only need one
#since we just want one direction
#Try creating GPIO.PWM(pin, 100) but not sure if it will work... p.start()
#p.changeDutyCycle() and p.stop()

#Run small stepper to center
print("Small step running inward")

GPIO.output(SMALL_DIR, CCW)
for x in range(REPS*SMALL_SPR):
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(3*delay)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(3*delay)

#Run big and small stepper
print("Big and small step running")

GPIO.output(BIG_DIR, CW)
GPIO.output(SMALL_DIR, CW)
for i in range(int(REPS*SPIN*BIG_SPR)):
    GPIO.output(BIG_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    time.sleep(delay)
    #if(i%(SPIN) == 0):
      #GPIO.output(SMALL_STEP, GPIO.HIGH)
      #time.sleep(delay)
      #GPIO.output(SMALL_STEP, GPIO.LOW)
      #time.sleep(delay)

#Clean up pins
GPIO.cleanup()
