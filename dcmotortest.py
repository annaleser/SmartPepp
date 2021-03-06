import time
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Rotation and delay variables
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
delay = .000025

#Big stepper motor set up
BIG_DIR = 21   # Direction GPIO Pin
BIG_STEP = 22  # Step GPIO Pin

GPIO.setup(BIG_DIR, GPIO.OUT)
GPIO.setup(BIG_STEP, GPIO.OUT)

#DC Motor set up
rpwm = 5
lpwm = 7

GPIO.setup(rpwm,GPIO.OUT)
GPIO.setup(lpwm,GPIO.OUT)
GPIO.output(rpwm, GPIO.LOW)
GPIO.output(lpwm,GPIO.LOW)

#DC Motor start
p=GPIO.PWM(rpwm,50)
p.stop()
p.start(25)

#Variables for steppers
print("BIG")

#SPIN
GPIO.output(BIG_DIR, CW)
while True:
    GPIO.output(BIG_STEP, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(BIG_STEP, GPIO.LOW)
    time.sleep(delay)

#Stop motor
p.stop()
