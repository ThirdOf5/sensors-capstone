import RPi.GPIO as GPIO
import time

# set RPi pin numbering scheme
GPIO.setmode(GPIO.BCM)

# define gpio pins
channel = 17
led = 16
GPIO.setup(channel, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

def callback(c):
    if GPIO.input(c):
        print("LED off")
        GPIO.output(16, False)
    else:
        print("LED on")
        GPIO.output(16, True)

# tells the Pi to watch the pin and tell us when it goes either high or low
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)

# add an event for when the water level goes above/below a certain threshold
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(0.05)

