from time import sleep
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)

#Rotation variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation

#Big stepper motor set up
BIG_DIR = 11   # Direction GPIO Pin
BIG_STEP = 12  # Step GPIO Pin
BIG_SPR = 48   # Steps per Revolution (360 / 7.5)

GPIO.setup(BIG_DIR, GPIO.OUT)
GPIO.setup(BIG_STEP, GPIO.OUT)
GPIO.output(BIG_DIR, CW)

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

p=GPIO.PWM(en,1000)
p.start(25)
#The default speed & direction of motor is LOW & Forward....
#r-run s-stop f-forward b-backward l-low m-medium h-high e-exit

#Run big stepper
step_count = BIG_SPR
delay = .0208

for x in range(step_count):
    GPIO.output(BIG_STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(BIG_DIR, CCW)
for x in range(step_count):
    GPIO.output(BIG_STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    sleep(delay)

#Clean up pins
GPIO.cleanup()
