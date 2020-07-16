import RPi.GPIO as GPIO
import multiprocessing 
import time
GPIO.setmode(GPIO.BCM)
class StepMotor:
    directionPin=0
    pulsePin=0
    rps = 0 
    stepResolution=0 #200
    delay=0 #f = 1/T
    correctionFactor = .21 # accounts for linear relationship between some extra delay in the motor driver*
    def __init__(self,direction,step,res = 200, rev= 2):
        self.p = multiprocessing.Process 
        self.directionPin=direction
        self.pulsePin=step
        self.stepResolution = res
        self.rps = rev
        x = self.correctionFactor - (.02*(self.rps - 2)) 
        self.delay = x/(self.stepResolution*self.rps) 
        GPIO.setup(self.directionPin, GPIO.OUT)
        GPIO.setup(self.pulsePin, GPIO.OUT)
        GPIO.output(self.directionPin, GPIO.HIGH)
        GPIO.output(self.pulsePin, GPIO.LOW)
    def setRPS(self,n):
        x = self.correctionFactor - (.02*(self.rps - 2)) 
        self.rps=n
        self.delay = x/(self.stepResolution*self.rps) 
    def setStepRes(self,n):
        x = self.correctionFactor - (.02*(self.rps - 2)) 
        self.stepResolution = n
        self.delay = x/(self.stepResolution*self.rps) 
    def setDirection(self, direction):
        if direction == 1:
          GPIO.output(self.directionPin, GPIO.HIGH)
        else:
          GPIO.output(self.directionPin, GPIO.LOW)
    def __runxSteps(self,n = 1):
        for i in range(0,n):
             time.sleep(self.delay/3)
             GPIO.output(self.pulsePin,GPIO.HIGH)
             time.sleep(self.delay/3)
             GPIO.output(self.pulsePin,GPIO.LOW)
             time.sleep(self.delay/3)
    def runxSteps(self,n):
        self.p=multiprocessing.Process(target=self.__runxSteps,args=[n])
        self.p.start()
    def stop(self):
        self.p.terminate()
