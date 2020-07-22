import time
import RPi.GPIO as GPIO

#Board set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#DC Motor set up
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
p=GPIO.PWM(rpwm,100)
#Start with 25% duty cycle
p.start(100)
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
p.stop()

#Spin other way with basic on off
GPIO.output(lpwm, GPIO.HIGH)
time.sleep(5)
GPIO.output(lpwm, GPIO.LOW)
