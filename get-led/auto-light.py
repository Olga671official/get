import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

led = 26
trans = 6
state = 0

GPIO.setup(trans, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    if GPIO.input(trans):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)
