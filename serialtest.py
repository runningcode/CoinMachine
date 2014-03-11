#!/usr/bin/env python

import serial
import RPi.GPIO as GPIO

port = serial.Serial("/dev/ttyAMA0", baudrate=9600)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

runningtotal = 0.0
transactiontotal = 0.0
pennies = 0
nickels = 0
dimes = 0
quarters = 0

while True:
	coinval = ord(port.read(1))
	if   coinval == 1:
		print "You got a penny!"
		pennies += 1
		runningtotal += .01
		transactiontotal += .01
	elif coinval ==  5:
		print "You got a nickel!"
		nickels+= 1
		runningtotal += .05
		transactiontotal += .05
	elif coinval == 10:
		print "You got a dime!"
		dimes+= 1
		runningtotal += .10
		transactiontotal += .10
	elif coinval == 25:
		print "That was a quarter!"
		quarters+= 25
		runningtotal += .25
		transactiontotal += .25

