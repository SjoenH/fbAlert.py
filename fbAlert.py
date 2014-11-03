import time
import requests

import RPi.GPIO as GPIO
GPIO.setup(7,GPIO.OUT)

def readLikes():
	with open('likes.txt', 'r') as f:
		   f.seek(0)
		   return f.read()

def writeLikes(a):
	a = str(a)
	with open('likes.txt', 'w') as f:
		f.write(a)

def blink(a,b): #'b' number of blinks. #Example:0.2*40 = 8 seconds of blinking.
	for i in range(b):
		if a=='up':
			GPIO.output(7,True)
			time.sleep(0.1) #Timedelay. Set to the amount of time you want the LED to shine.
			GPIO.output(7,False)
			time.sleep(0.2)
		else:
			GPIO.output(7,True)
			time.sleep(0.2)
			GPIO.output(7,False)
			time.sleep(0.1)

try:
    likes = int(readLikes())
except:
	print("Can't read likes from file.\nSetting likes to '0' and writing to file... ")
	likes = 0
	writeLikes(likes)

blink('up',10)
print('Welcome,\nReading likes from local file.\nLikes: ',likes,'\n\nRequesting updated likes for page Now!')

while True :
	likes = int(readLikes())

	try:
		r = requests.get('https://graph.facebook.com/695493627155983') #Can change with whatever FB-page.
	except:
		print("Cannot reach server: Check Network Connection.\nTrying again in 10 sec.")
		time.sleep(10)
		print("Trying again.")

	if r.status_code == requests.codes.ok : #Checking if website returns a 'OK value'.
		currentLikes = r.json()['likes'] #Seperates(?) the likes section from the rest of the JSON object.
		if likes < currentLikes :
			print('Likes: ', currentLikes, '\nChange: ', currentLikes - likes)
			likes = currentLikes
			writeLikes(likes)
			blink('up',90)
		elif likes > currentLikes :
			print('Likes: ', currentLikes, '\nChange: ', currentLikes - likes)
			likes = currentLikes
			writeLikes(likes)
			blink('down',80)
	time.sleep(10)
