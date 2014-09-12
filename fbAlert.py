import time
import datetime #Debugging: Will use this later for printing out date.

import facebook #Graph api. Might want to install manually.
import os

import RPi.GPIO as GPIO

GPIO.setup(7,GPIO.OUT)

filefoo = open('filefoo.txt','r+') #Checking last remembered nr. of likes.

def blink():
	GPIO.output(7,True)
	time.sleep(1) #Timedelay. Set to the amount of time you want the LED to shine.
	GPIO.output(7,False)

while True:
	blink()
	time.sleep(2)
	pass
