from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO 
from gpiozero import Button
#Import Modules

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.IN)

while True:
    pin12 = GPIO.input(12)
    if pin12 == 0:
        song = AudioSegment.from_mp3("morselong.mp3")
        play(song)
        continue
    else:
        continue
