import time
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#DC Motor set up
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
p=GPIO.PWM(en,1000)
#Start with 25% duty cycle
p.start(100)
GPIO.output(in2,GPIO.HIGH)
time.sleep(5)
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
GPIO.output(in2,GPIO.LOW)
p.stop()
