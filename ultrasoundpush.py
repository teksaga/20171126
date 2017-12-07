import RPi.GPIO as GPIO
from time import sleep
from Ultrasonic import Ultrasonic
from datetime import datetime
import commands

GPIO.setmode(GPIO.BOARD)
trigger = 13
echo = 7

us = Ultrasonic(trigger, echo)

count = 0 
before = 0

while True:
	if(us.measure() < 50 and before < 50):
		count += 1
		if(count == 5):
			now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
			note = 'alart:'+now
			pushMessage = commands.getoutput("./mypush.sh {0}".format(note))
			print pushMessage
			count = 0
	else:
		count = 0
	print(us.measure())
	before = us.measure()
	sleep(0.5)
