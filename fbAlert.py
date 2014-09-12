import time
import datetime #Debugging: Will use this later for printing out date.

import os

import RPi.GPIO as GPIO

GPIO.setup(7,GPIO.OUT)

filefoo = open('filefoo.txt','r+') #Checking last remembered nr. of likes.

def blink():
	GPIO.output(7,True)
	time.sleep(1) #Timedelay
	GPIO.output(7,False)

while True:
	blink()
	time.sleep(3)
	pass
