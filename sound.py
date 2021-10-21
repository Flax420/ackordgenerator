#!/usr/bin/env python3
from pygame.mixer import *
init()

keylist = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

sound_dictionary = {}

for i in range(1, 4):
    for key in keylist:
        sound_dictionary[f"{key}{i}"] = Sound(f"./sounds/{key.lower()}{i}.mp3")
        sound_dictionary[f"{key}{i}"].set_volume(0.2)
# Demo 
if __name__ == "__main__":
    sound_dictionary["C1"].play()
    sound_dictionary["E1"].play()
    sound_dictionary["G1"].play()

    while True:
        continue
