# Code to test the relay circuit. Turns on for 1sec, then off for 1sec, "forever"

import RPi.GPIO as GPIO
import time

# set RPi pin numbering scheme
GPIO.setmode(GPIO.BCM)

# define gpio pins
relay = 16
GPIO.setup(relay, GPIO.OUT)

while True:
    GPIO.output(relay, True)
    time.sleep(1)
    GPIO.output(relay, False)
    time.sleep(1)

