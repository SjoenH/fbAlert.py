import time
import requests

import RPi.GPIO as GPIO
GPIO.setup(7,GPIO.OUT)

def readLikes():
	with open('likes', 'r+') as f:
		   f.seek(0)
		   return f.read()

def writeLikes(a):
	a = str(a)
	with open('likes', 'r+') as f:
		f.write(a)

def blink(a):
	GPIO.output(7,True)
	time.sleep(a) #Timedelay. Set to the amount of time you want the LED to shine.
	GPIO.output(7,False)
	pass

try:
    likes = int(readLikes())
except:
    likes = 0
    writeLikes(likes)

print('Welcome,\nReading likes from local file.\nLikes: ',likes,'\n\nRequesting updated likes for page in 10 seconds...\nNB: No confirmation dialog if same as local var.\n')

while True :
	time.sleep(10) #Waiting before trying to request site.
	r = requests.get('https://graph.facebook.com/695493627155983') #Can change with whatever FB-page.
	if r.status_code == requests.codes.ok : #Checking if website returns a 'OK value'.
		currentLikes = r.json()['likes'] #Seperates(?) the likes section from the rest of the JSON object.
		if likes < currentLikes :
			print('Likes: ', currentLikes, '\nChange: ', currentLikes - likes)
			likes = currentLikes
			writeLikes(likes)
			blink(15)
			pass
		elif likes > currentLikes :
			print('Likes: ', currentLikes, '\nChange: -', likes - currentLikes)
			likes = currentLikes
			writeLikes(likes)
			blink(15)
			pass
		else :
			pass
	else :
		print("Cannot reach server...Trying again in 10 sec.")
