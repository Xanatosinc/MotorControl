#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LightG = 18
LightR = 23
Motor1A = 4
Motor1B = 17
Motor1E = 24

GPIO.setup(LightG,GPIO.OUT)
GPIO.setup(LightR,GPIO.OUT)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

def lightGreen():
	GPIO.output(LightG,GPIO.HIGH)
	GPIO.output(LightR,GPIO.LOW)
def lightRed():
	GPIO.output(LightG,GPIO.LOW)
	GPIO.output(LightR,GPIO.HIGH)
def lightYellow():
	GPIO.output(LightG,GPIO.HIGH)
	GPIO.output(LightR,GPIO.HIGH)

def motorForward():
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
def motorStop():
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.LOW)
def motorReverse():
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.HIGH)
	GPIO.output(Motor1E,GPIO.HIGH)

print "Turning motor forward"
lightGreen()
motorForward()
sleep(2)

print "Pause"
lightYellow()
motorStop()
sleep(1)

print "Turning motor reverse"
lightRed()
motorReverse()
sleep(2)

print "Stopping motor"
motorStop()

GPIO.cleanup()
