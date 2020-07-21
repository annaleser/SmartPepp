import time
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Rotation and delay variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
delay = .0000125

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

#Stepper motor variables
straightAmt = 1000
spin = 16

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

GPIO.output(SMALL_DIR, CCW)
wait = 104
#Slow start small stepper
for i in range(straightAmt/3):
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(wait*delay)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(wait*delay)
    wait = wait - 0.5

#Run small stepper to center
print("Small step running inward")

for i in range(straightAmt):
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(4*delay)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(4*delay)

#Run big and small stepper
print("Big and small step running")

GPIO.output(BIG_DIR, CW)
GPIO.output(SMALL_DIR, CW)

for i in range(straightAmt*spin):
    GPIO.output(BIG_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    time.sleep(delay)
    if(i%(spin) == 0):
      GPIO.output(SMALL_STEP, GPIO.HIGH)
      time.sleep(delay)
      GPIO.output(SMALL_STEP, GPIO.LOW)
      time.sleep(delay)
    delay = delay + 0.00000000130208333

wait = 1
#Slow stop small stepper
for i in range(straightAmt/3):
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    GPIO.output(BIG_STEP, GPIO.HIGH)
    time.sleep(wait*delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(wait*delay)
    wait = wait + 0.5

#Clean up pins
GPIO.cleanup()
