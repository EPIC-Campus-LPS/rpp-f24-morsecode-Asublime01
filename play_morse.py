from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO 
from gpiozero import Button
import time
#Import Modules

time.sleep(3)
hello = [1, 1, 1, 1, "n", 1, "n", 1, 2, 1, 1, "n", 1, 2, 1, 1, "n", 2, 2, 2]

long = AudioSegment.from_mp3("morselong.mp3")

short = AudioSegment.from_mp3("morseshort.mp3")


for unit in hello:
    if unit == 1:
        play(short)
    elif unit == 2:
        play(long)
    elif unit == "n":
        time.sleep(3)

        

        