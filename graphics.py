#!/usr/bin/env python3
import sys
 
import pygame
from pygame.draw import polygon, rect
from pygame.locals import *
import sound
 

# I dictionaryn keys finns en nestad dictionary med positioner som behöver head adderat och sedan multiplier gångrat
# Head_offset ska adderas till head och color definerar färgen som ska fylla tangenten
keys = {}
keys["C"] = {"positions": [(0,0), (0,137), (30,137), (30,91), (17,91), (17,0), (0,0)], "head_offset": (33,0), "color": (255,255,255)}
keys["C#"] = {"positions": [(0,0), (0,91), (20,91), (20,0), (0,0)], "head_offset": (33,0), "color": (0,0,0)}
keys["D"] = {"positions": [(0,0), (0,91), (-7,91), (-7,137), (23,137), (23,91), (17,91), (17,0), (0,0)], "head_offset": (33,0), "color": (255,255,255)}
keys["E"] = {"positions": [(0,0), (0,91), (-13,91), (-13,137), (17,137), (17,0), (0,0)], "head_offset": (33,0), "color": (255,255,255)}
keys["G"] = {"positions": [(0,0), (0,91), (-7,91), (-7,137), (25,137), (25,91), (17,91), (17,0), (0,0)], "head_offset": (33,0), "color": (255,255,255)}
keys["A"] = {"positions": [(0,0), (0,91), (-9,91), (-9,137), (23,137), (23,91), (17,91), (17,0), (0,0)], "head_offset": (33,0), "color": (255,255,255)}

# Identiska knappar
keys["D#"] = keys["C#"]
keys["F#"] = keys["C#"]
keys["G#"] = keys["C#"]
keys["A#"] = keys["C#"]

keys["F"] = keys["C"]
keys["B"] = keys["E"]
# Drawing head 
head = (0,0)

# Returnerar kordinater för en polygon
def get_key_polygon(head, key, keys, multiplier):
    _kordinater = [] # Standardvärde
    if key in keys:
        for k in keys[key]["positions"]:
            (_x, _y) = k
            _x += k[0]*multiplier + head[0]
            _y += k[1]*multiplier + head[1]
            _kordinater.append((_x, _y))
    return _kordinater

# Ändrar rithuvudets position baserat på nyckel
def change_headpos(head, key, keys, multiplier):
    (_x, _y) = (0,0) # Standardvärde
    if key in keys:
        (_x, _y) = head
        _x += keys[key]["head_offset"][0] * multiplier
        _y += keys[key]["head_offset"][1] * multiplier
    return (_x, _y)

def return_head():
    return (0,0)

def run(head, keys, multiplier):
    pygame.init()
    keylist = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"] * 2
    fps = 10
    fpsClock = pygame.time.Clock()
    _toner = list(("c", "c#", "c"))
    print(_toner)
     
    width, height = 794, 480
    screen = pygame.display.set_mode((width, height))
    # Game loop.
    while True:
        screen.fill((128,128,128))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update.
        _toner = list(("c", "c#", "c"))
        # Draw
        for key in keylist:
            _cords = get_key_polygon(head, key, keys, multiplier)
            head = change_headpos(head, key, keys, multiplier)
            color = keys[key]["color"]
            if _toner and _toner[0].upper() == key:
                color = (203, 68, 61)
                _toner.pop(0)

            pygame.draw.polygon(screen, color, _cords, width=0) # Knapp
            pygame.draw.polygon(screen, (57,57,57), _cords, width=1) # Outline
        

        #keylist.append(keylist.pop(0))
        #pygame.draw.polygon(screen, keys[key]["color"], keys[key]["positions"])
        head = return_head()
        pygame.display.flip()
        fpsClock.tick(fps)

def main():
    global keys
    head = (0, 0)
    run(head, keys,1)
if __name__ == '__main__':
    main()
