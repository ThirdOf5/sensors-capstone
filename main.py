# Project: Pi Watering System
# Date: Fall 2017
# Author: Caleb Jhones

import RPi.GPIO as GPIO
import time

# set RPi pin numbering scheme
GPIO.setmode(GPIO.BCM)

# define gpio pins
channel = 17 # Connected to the hygrometer
relay = 16 # Connected to the relay, which controls the solenoid
GPIO.setup(channel, GPIO.IN)
GPIO.setup(relay, GPIO.OUT)

def callback(c):
    if not GPIO.input(c): #FIXME should this have the not?
        GPIO.output(relay, True)
        time.sleep(1)
        GPIO.output(relay, False)
        print("{}: Relay triggered ".format(time.ctime()))

# tells the Pi to watch the pin and tell us when it goes either high or low
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)

# add an event for when the water level goes above/below a certain threshold
GPIO.add_event_callback(channel, callback)

while True:
    # check if we need watered once every hour while running
    time.sleep(3600)

