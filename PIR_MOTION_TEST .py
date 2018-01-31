# PIR motion test 
# By: Anika Kashyap
# 01/24/18

# Import lib.
import RPi.GPIO as GPIO
import time

# Setting up the PIR, LED, and BUTTON 
GPIO.setmode(GPIO.BCM)
PIR = 12
GPIO.setup(PIR, GPIO.IN)
LED = 6
GPIO.setup(LED, GPIO.OUT)
BUTTON = 21
GPIO.setup(BUTTON, GPIO.IN)

# Gets things working


# Sets motion_detect_mode
motion_detect_mode = False 

# Forever loop that checks if the sensor is detecting motion or not detecting motion 
while True:

    while motion_detect_mode == True
        if GPIO.input(PIR):
            print("Motion dected! Yippie Yip Yippe")
            GPIO.output(LED, GPIO.HIGH)
        else:
            print ("Oh snap! No motion detected")
            GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)
if GPIO.input(BUTTON)
        if motion_detect_mode == True:
        motion_detect_mode = False
    else:
        motion_detect_mode = True
 
