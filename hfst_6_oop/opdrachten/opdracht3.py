# import modules.
import RPi.GPIO as GPIO
import time
  
class Button:
    def __init__(self, button_nummer):
        self.button_nummer = button_nummer
        GPIO.setup(self.button_nummer, GPIO.IN)
        self.huidige_stand = GPIO.LOW
        self.toestand = "omlaag"
    def detect_wijziging(self):
        if GPIO.input(5) != self.huidige_stand:
            if GPIO.input(5) == GPIO.HIGH:
                print("Knop 5 is aan")
                self.toestand = "omhoog"
            else:
                print("Knop 5 is uit") 
                self.toestand = "omlaag"
        self.huidige_stand = GPIO.input(5)
        return self.toestand

class Led:
    def __init__(self, pin_nummer):
        self.pin_nummer = pin_nummer
        GPIO.setup(pin_nummer, GPIO.OUT)
    def aan(self):
        GPIO.output(self.pin_nummer, GPIO.HIGH)
    def uit(self):
        GPIO.output(self.pin_nummer, GPIO.LOW)


# Maak een knop op pin 5
knop_5 = Button(5)
# Maak een led op pin 8 en 10
led_8 = Led(8)
led_10 = Led(10)

while True:
  # Controleer wat de toestand van de knop is:
  #   "omhoog", "omlaag", "geen_wijziging"
  toestand = knop_5.detect_wijziging()

  # Als de knop is aangezet, schakel led 8 aan en 10 uit.
  if toestand == "omhoog":
    led_8.aan()
    led_10.uit()
  # Als de knop is uitgezet, schakel led 10 aan en 8 uit.
  elif toestand == "omlaag":
    led_8.uit()
    led_10.aan()
  # Als de toestand van de knop niet gewijzigd is, doe niets.
  else:
    pass
