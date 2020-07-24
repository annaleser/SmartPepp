import time
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Rotation and delay variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation

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

#delay =  -0.008*(i-.5)**4+.0005
#delay = -0.0426667*(i**4)+0.0853333*(i**3)-0.0533333*(i**2)+0.0106667*i
#delay = -4.2666666666666*(10**-14)*(i**4)+8.533333333333*(10**-11)*(i**3)-5.333333333333*(10**-8)*(i**2)+0.0000106667*i
#delay = -2.6666666666666*(10**-15)*(i**4)+1.0666666666666*(10**-11)*(i**3)-1.333333333333*(10**-8)*(i**2)+5.333333333333*(10**-6)*i
#delay = -4*(10**-15)*(i**4)+1.6*(10**-11)*(i**3)-2*(10**-8)*(i**2)+8*(10**-6)*i
#Variables for steppers
print("SMALL")

#IN
GPIO.output(SMALL_DIR, CCW)
delay = .0005
for i in range(2000):
    GPIO.output(SMALL_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(SMALL_STEP, GPIO.LOW)
    time.sleep(delay)
