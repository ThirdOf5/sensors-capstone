import RPi.GPIO as GPIO
import statistics
import time

GPIO.setmode(GPIO.BCM)

sensor = 17 # hygrometer pin
relay = 16 # relay/solenoid pin

class Water:
    def __init__(self, sensor=17, relay=16, wait=3600, dur=1):
        ''' Initialize a waterer instance. This sets variables and
            sets up our GPIO.
            INPUTS:
                sensor: the input pin for the hygrometer sensor
                relay:  the output pin for the relay/solenoid
                wait:   how long to wait between polling the sensor
                dur:    how long to turn the water on
            OUTPUTS:
                void
        '''
        self.sensor = sensor
        self.relay = relay
        self.wait = wait
        self.duration = dur
        self.log = [time.time()] # a log of when watering has happened. Add the current time as a baseline

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor, GPIO.IN)
        GPIO.setup(relay, GPIO.OUT)

    def check_hygrometer(self):
        ''' Checks if the soil humidity is too low.
            The hygrometer unit I am using has a digital output and a
            built-in potentiometer to tune what the output is on that
            digital out pin. As such, we just poll that pin rather than
            reading an analogue value and mucking with an ADC.
            INPUTS:
                n/a
            OUTPUTS:
                bool. True if needs water, False if there is enough water
        '''
        return not GPIO.input(self.sensor)

    def water_plant(self, needs_water):
        ''' If needs_water is True, open the solenoid for a set amount
            of time, and then close it again.
            INPUTS:
                needs_water: bool if the plant needs water or not
            OUTPUTS:
                bool. True if watering happened, False otherwise
        '''
        if needs_water:
            GPIO.output(self.relay, True)
            time.sleep(self.duration)
            GPIO.output(self.relay, False)
            print(time.ctime() + " : Plant watered for {} seconds!".format(self.duration))
            return True
        return False

    def do_water(self):
        ''' Loop until the user exits the program. '''
        while 1:
            if self.water_plant(self.check_hygrometer()):
                self.log.append(time.time())
            time.sleep(self.wait)

    def calc_time_delta(self):
        ''' Calculates the mean time between waterings.
            INPUTS:
                n/a
            OUTPUTS:
                double. Represents the mean time between all instances of watering the plant
        '''
        deltas = list()
        for i in range(len(self.log) - 1):
            # calculate the difference between i and i+1
            deltas.append(self.log.at(i + 1) - self.log.at(i))
        return statistics.mean(deltas)

# MAIN
if __name__ == '__main__':
    time.sleep(60) # wait a minute after starting the code, in case the sensor isn't in place yet etc
    w = Water() # change any input variables here if desired!
    try:
        w.do_water()
    except EOFError:
        print("\nMean time between waterings: {}".format(w.calc_time_delta(self))


