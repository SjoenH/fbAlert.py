import time
import datetime #Debugging: Will use this later for printing out date.

import requests

import RPi.GPIO as GPIO
GPIO.setup(7,GPIO.OUT)

#Writing to file still not working. So this doesn't really do any purpose...
filefoo = open('filefoo.txt','r+') #Checking last remembered nr. of likes.
likes = filefoo.read()

def blink(a):
	print(currentLikes)
	GPIO.output(7,True)
	time.sleep(a) #Timedelay. Set to the amount of time you want the LED to shine.
	GPIO.output(7,False)

except Exception:
	pass
	
loop = 'forever'
while loop == 'forever':
	r = requests.get('https://graph.facebook.com/695493627155983') #Can change with whatever FB-page.
	j = r.json()
	currentLikes = j['likes'] #Seperates(?) the likes section from the rest of the JSON object.
	writeLikes = str(currentLikes)
	if likes < currentLikes :
		likes = currentLikes
		# filefoo.truncate(0)
		# filefoo.write(writeLikes)
		print("Someone Liked Your Site!")
		blink(2)
	elif likes > currentLikes :
		print("It's a sad day... :(")
		likes = currentLikes
		# filefoo.truncate(0)
		# filefoo.write(writeLikes)
		blink(1)
	else :
		time.sleep(1) #How often you want to check FB page.