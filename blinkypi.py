import time
import RPi.GPIO as GPIO

led_pin_red = 21
led_pin_green = 22
led_pin_blue = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)
GPIO.setup(led_pin_blue, GPIO.OUT)


while True:

    GPIO.cleanup()
    GPIO.output(led_pin_red, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_pin_red,GPIO.LOW)
    time.sleep(1)
    GPIO.output(led_pin_green, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_pin_green,GPIO.LOW)
    time.sleep(1)
    GPIO.output(led_pin_blue, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_pin_blue,GPIO.LOW)
    time.sleep(1)
