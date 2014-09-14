fbAlert.py
==========
fbAlert is a python program that monitors a facebook page and prints out a message when someone likes -and dislikes, the page.
The program is running on a Raspberry Pi and is flashing a LED trough the GPIOs.

The LED is connected to ground and to pin 7.
Raspberry Pi is connected to internet through Ethernet cable.

You need to have the RPI.GPIO module for python on the Raspberry Pi.
To install it, SSH into the RPi and run:

    $ pip install requests
    $ wget http://pypi.python.org/packages/source/R/RPi.GPIO/RPi.GPIO-0.1.0.tar.gz
    $ tar zxf RPi.GPIO-0.1.0.tar.gz
    $ cd RPi.GPIO-0.1.0
    $ sudo python setup.py install

A new version is out, but the program should work with this version of GPIO.


    $ pip install requests
