import time
import datetime #Debugging: Will use this later for printing out date.

import requests

import RPi.GPIO as GPIO
GPIO.setup(7,GPIO.OUT)

def readLikes():
	f = open('likes', 'r+')
	f.seek(0)
	return f.read()
likes = int(readLikes())
print(likes)

def writeLikes(a):
	f = open('likes', 'r+')
	a = str(a)
	f.write(a)

def blink(a):
	print(currentLikes)
	GPIO.output(7,True)
	time.sleep(a) #Timedelay. Set to the amount of time you want the LED to shine.
	GPIO.output(7,False)
	pass

while True :
	time.sleep(10) #Waiting before trying to request site.
	r = requests.get('https://graph.facebook.com/695493627155983') #Can change with whatever FB-page.
	if r.status_code == requests.codes.ok : #Checking if website returns a 'OK value'.
		j = r.json()
		currentLikes = j['likes'] #Seperates(?) the likes section from the rest of the JSON object.
		if likes < currentLikes :
			likes = currentLikes
			writeLikes(likes)
			print("Someone Liked Your Site!")
			blink(15)
			pass
		elif likes > currentLikes :
			print("It's a sad day... :(")
			likes = currentLikes
			writeLikes(likes)
			blink(15)
			pass
		else :
			pass
	else :
		print("Cannot reach server...Trying again in 10 sec.")
