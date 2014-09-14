import time
import datetime #Debugging: Will use this later for printing out date.

import requests

import RPi.GPIO as GPIO
GPIO.setup(7,GPIO.OUT)

#Writing to file still not working. So this doesn't really do any purpose...
f = open('likes', 'r+')  #Checking last remembered nr. of likes.
f.seek(0)
likes = f.read()

def blink(a):
	print(currentLikes)
	GPIO.output(7,True)
	time.sleep(a) #Timedelay. Set to the amount of time you want the LED to shine.
	GPIO.output(7,False)

while True :
	r = requests.get('https://graph.facebook.com/695493627155983') #Can change with whatever FB-page.
	if r.status_code == requests.codes.ok : #Checking if website returns a 'OK value'.
		j = r.json()
		currentLikes = j['likes'] #Seperates(?) the likes section from the rest of the JSON object.
		writeLikes = str(currentLikes)
		if likes < currentLikes :
			likes = currentLikes
			f.write(likes'\n')
			print("Someone Liked Your Site!")
			blink(15)
			pass
		elif likes > currentLikes :
			print("It's a sad day... :(")
			likes = currentLikes
			f.write(likes'\n')
			blink(15)
			pass
		else :
			time.sleep(1) #How long you want to wait before checking FB page.
			pass
	else :
		time.sleep(2)
