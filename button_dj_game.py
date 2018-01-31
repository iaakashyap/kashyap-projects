# By Anika
# DJ Raspi
# Jan 16th, 2018
# A music playing DJ Machine

# import needed libraies
import RPi.GPIO as GPIO
import time
import random
import os

# Returns a list of mp3 sound files for the opath given
def  get_MP3_sounds (sound_path):
    sound_files = os.listdir(sound_path)
    sound_files = [sound_file for sound_file in sound_files if sound_file.endswith('mp3')]
    return sound_files

# Plays a random sound from list of mp3s for the path given
def play_random_sound(sound_path, sound_files):
    sound_file = random.choice(sound_files)
    os.system("omxplayer -o local '" + sound_path + "/" + sound_file + "' &")

# Folders with sound files
path_music = "/usr/share/scratch/Media/Sounds/Music Loops"
path_vocals = "/usr/share/scratch/Media/Sounds/Vocals"
path_effects = "/usr/share/scratch/Media/Sounds/Effects"
                    
# Get the list of music loops and vocals (mp3s only)
sounds_music = get_MP3_sounds(path_music) 
sounds_vocals = get_MP3_sounds(path_vocals) 
sounds_effects = get_MP3_sounds(path_effects)

# Varibles for button pins
button_pin1 = 6
button_pin2 = 19

# Set up numbering system
GPIO.setmode(GPIO.BCM)

# Setup GPIO for input 
GPIO.setup (button_pin1, GPIO.IN)
GPIO.setup (button_pin2, GPIO.IN)



# Clear the screen
os.system("clear")

# Tittle Screen and instructions
title = """
    DJ RASPI TIME!!!
    Press button one for Music sounds
    Press button 2 for Music vocals
    press Ctrl + C to exit
"""

print(title)

while True:
    if GPIO.input(button_pin1):
        print ("You pressed button #1!")
        play_random_sound(path_music, sounds_music)
        time.sleep(.1)
    if GPIO.input(button_pin2):
        print ("You pressed button #2!")
        play_random_sound(path_music, sounds_vocals)
        time.sleep(.1)
    if GPIO.input(button_pin1) and GPIO.input(button_pin2):
        print ("You pressed button #1 and #2! Easter Egg!")
        play_random_sound(path_effects, sounds_effects)
        time.sleep(.1)
    time.sleep(.1)
    

