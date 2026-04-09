import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

button = 13
state = 0

GPIO.setup(button, GPIO.IN)
GPIO.setup(26, GPIO.OUT)

while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(26, state)
        time.sleep(0.2)
