import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

leds = [17, 27, 22]
count = 0
while count < 10:
        for led in leds:
                GPIO.output(led, True)
                time.sleep(1)
                GPIO.output(led, False)
        count += 1