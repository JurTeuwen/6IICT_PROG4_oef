# import raspberry pi GPIO module
import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, pin_nummer):
        self.pin_nummer = pin_nummer
        GPIO.setup(pin_nummer, GPIO.OUT)
    def aan(self):
        GPIO.output(self.pin_nummer, GPIO.HIGH)
    def uit(self):
        GPIO.output(self.pin_nummer, GPIO.LOW)


# Maak een led aan op pin 5 en pin 21
led_5 = Led(5)
led_21 = Led(21)

# Schakel de leds afwisselend aan/uit.
while True:
    led_5.aan()
    led_21.uit()
    time.sleep(1)

    led_5.uit()
    led_21.aan()
    time.sleep(1)