# Code to test the relay circuit. Turns on for 1sec, then off for 1sec, ten times

import RPi.GPIO as GPIO
import time

# set RPi pin numbering scheme
GPIO.setmode(GPIO.BCM)

# define gpio pins
relay = 16
GPIO.setup(relay, GPIO.OUT)

for i in range(10):
    GPIO.output(relay, True)
    time.sleep(1)
    GPIO.output(relay, False)
    time.sleep(1)

