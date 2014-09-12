import time
import datetime

import RPi.GPIO as GPIO

GPIO.setup(7,GPIO.OUT)

def blink():
	GPIO.output(7,True)
	time.sleep(1)
	GPIO.output(7,False)


blink()