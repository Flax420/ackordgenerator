#!/usr/bin/env python3
from pygame.mixer import *
init()

c = Sound("./sounds/c4.ogg")
csharp = Sound("./sounds/c#4.ogg")
d = Sound("./sounds/d4.ogg")
dsharp = Sound("./sounds/d#4.ogg")
e = Sound("./sounds/e4.ogg")
f = Sound("./sounds/f4.ogg")
fsharp = Sound("./sounds/f#4.ogg")
g = Sound("./sounds/g4.ogg")
gsharp = Sound("./sounds/g#4.ogg")
a = Sound("./sounds/a4.ogg")
asharp = Sound("./sounds/a4.ogg")
b = Sound("./sounds/b4.ogg")

sound_dictionary = {}

sound_dictionary["C"] = c
sound_dictionary["C#"] = csharp
sound_dictionary["D"] = d
sound_dictionary["D#"] = dsharp
sound_dictionary["E"] = e
sound_dictionary["F"] = f
sound_dictionary["F#"] = fsharp
sound_dictionary["G"] = g
sound_dictionary["G#"] = gsharp
sound_dictionary["A"] = a
sound_dictionary["A#"] = asharp
sound_dictionary["B"] = b

if __name__ == "__main__":
    c.play() 
    e.play()
    g.play()

    while True:
        continue
