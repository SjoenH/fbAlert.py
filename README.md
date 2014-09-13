fbAlert.py
==========
fbAlert is a python program that monitors a facebook page and prints out a message when someone likes the page. (...and dislikes)
The program is running on a Raspberry Pi and is flashing a LED trough the GPIOs.

The LED is connected to ground and to pin 7.
Raspberry Pi is connected to internet through Ethernet cable.

You need to install RPI.GPIO module for python on the Raspberry Pi. So ssh into the RPi and run:
  $ wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.1.0.tar.gz
  $ tar zxf RPi.GPIO-0.1.0.tar.gz
  $ cd RPi.GPIO-0.1.0
  $ sudo python setup.py install

NB! A new version is out, but the program should work with this version of GPIO.