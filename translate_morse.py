import RPi.GPIO as GPIO 
from gpiozero import Button
import time

# Setup and stuff
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([12, 21], GPIO.IN)


morse_code = {
    'A': [1, 2],
    'B': [2, 1, 1, 1],
    'C': [2, 1, 2, 1],
    'D': [2, 1, 1],
    'E': [1],
    'F': [1, 1, 2, 1],
    'G': [2, 2, 1],
    'H': [1, 1, 1, 1],
    'I': [1, 1],
    'J': [1, 2, 2, 2],
    'K': [2, 1, 2],
    'L': [1, 2, 1, 1],
    'M': [2, 2],
    'N': [2, 1],
    'O': [2, 2, 2],
    'P': [1, 2, 2, 1],
    'Q': [2, 2, 1, 2],
    'R': [1, 2, 1],
    'S': [1, 1, 1],
    'T': [2],
    'U': [1, 1, 2],
    'V': [1, 1, 1, 2],
    'W': [1, 2, 2],
    'X': [2, 1, 1, 2],
    'Y': [2, 1, 2, 2],
    'Z': [2, 2, 1, 1]
}




def count(num): #Timer for determining shorts and longs
    time.sleep(0.5)
    while True:
        inpin = GPIO.input(12)
        num += 1
        if inpin != 0:
            time.sleep(0.25)
            break
    return num


def translator(morse_code, translate_list): #Translator Function
    for key, value in morse_code.items():
        if translate_list == value:
            letter = key
            return letter
        

num = 0
numlist = []
while True: #Numlist maker
    inpin = GPIO.input(12)
    endpin = GPIO.input(21)
    if inpin == 0:
        num = count(num)
        numlist.append(num)
        print(numlist)
        continue
    elif endpin == 0:
        break
    num = 0


for i in range(len(numlist)): #Input checker to determine shorts and longs
    if numlist[i] >= 2 and numlist[i] <= 999999:
        numlist[i] = 2
    elif numlist[i] >= 1000000:
        numlist[i] = 3


words = [] #Word list


while len(numlist) != 0: # This code populates the translate list so it can be turned into a letter
    translate = []
    num_threes = 0
    for letter in numlist:
        if letter != 3:
            translate.append(letter)
        elif letter == 3:
            num_threes += 1
            break
        
#Letter is translated and the used numbers are removed from the list
    letter = translator(morse_code, translate)
    words.append(letter)
    for i in range(len(translate) + num_threes):
        numlist.pop(0)


print(words)
    





    

