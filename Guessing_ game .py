# Light up Guessing Game
# Anika Kashyap
# Jan 3rd, 2018
# Guess number (1,20), shows blue if to low, red if to high, green if correct. You get 5 tries
import random
import time
import RPi.GPIO as GPIO

def game_over():
    ''' My game over function'''
    print ("You ran out of guesses :(")
    print ("Cookies")

def blink_led(pin):
    for i in range (5):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.2)

def easter_egg (r,g,b):
    for i in range (5):
        GPIO.output(r,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(r,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(g,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(g,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(b,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(b,GPIO.LOW)

GPIO.setmode(GPIO.BCM) 
led_pin_red = 21
led_pin_green = 22
led_pin_blue = 23

GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)
GPIO.setup(led_pin_blue, GPIO.OUT)

# Tittle and Insturctions
print("*" * 80)
print ("Light up guessing game")
print ("*" * 80)
print ("""
You have 5 gusses to guess a number between one 1 and 20
Too low --> blue
Too high --> red
Correct --> green
""")

play_again= "Y"

while play_again == "Y":

    # Get a random number (1 and 20)
    num = random.randint(1,20)

    # Start a loop (5 tries)
    guesses = 0
    while guesses < 5:
        # Get a guess from user
        guess = input ("Guess a number from 1 to 20: ")
        if guess == "My puppy = cute":
             easter_egg(led_pin_red,led_pin_green,led_pin_blue)
        else:
            guess = int (guess)
            guesses += 1
            # Check if guess is correct,too low or too high
            if guess == num:
                print("You are correct")
                # Make it blink green
                blink_led(led_pin_green)
                break
            elif guess < num:
                print("Too low")
                # Make it blink blue
                blink_led(led_pin_blue)
            else: # Must be to high

                    print ("Too High")
                    # Make it blink red
                    blink_led(led_pin_red)
    else:
                game_over()
                play_again = input ("Do you won't to play again? (Y or N): ").upper()

print ("Thank you for for playing!")







