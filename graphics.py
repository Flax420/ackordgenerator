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
def get_key_coordinates(head, key, keys, multiplier):
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

# Returnerar rithuvudet till origo
def return_head():
    return (0,0)

# Ritar tangenter med outline etc
def draw_keys(keylist, keys, head, chord, outline_color, highlight_color, surface, multiplier):
    _chord = chord.copy() # Kopiera variabeln för att förhindra att funktionen ändrar den
    for key in keylist:
            _cords = get_key_coordinates(head, key, keys, multiplier)
            head = change_headpos(head, key, keys, multiplier)
            color = keys[key]["color"]
            if _chord and _chord[0].upper() == key:
                color = highlight_color
                _chord.pop(0)

            pygame.draw.polygon(surface, color, _cords, width=0) # Knapp
            pygame.draw.polygon(surface, outline_color, _cords, width=1) # Outline

# Spelar ett ackord
def play_chord(chord):
    for c in chord:
        if c.upper() in sound.sound_dictionary:
            sound.sound_dictionary[c.upper()].stop()
            sound.sound_dictionary[c.upper()].play()

def demo_mode(demo_index, demo_delay, demo_delay_counter, keylist, toner):
    demo_delay_counter += 1
    if demo_delay_counter >= demo_delay:
        demo_delay_counter = 0
        demo_index += 1
        toner = [keylist[demo_index]]
        if demo_index == len(keylist)-1:
            demo_index = 0
    return (demo_index, demo_delay_counter, toner)

def run(head, keys, multiplier):
    pygame.init()
    base_keylist = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    keylist = []
    for i in range(1, 4):
        for key in base_keylist:
            keylist.append(f"{key}{i}")
            keys[f"{key}{i}"] = keys[key]
    demo = False
    demo_index = 0
    demo_delay = 5
    demo_delay_counter = 0
    _toner = list(("b", "d#", "f#", "a", "c#", "e", "g#")) # Temporary variable
    input_rect = pygame.Rect(200, 200, 140, 32)
    outline_color = (57,57,57)
    highlight_color = (203, 68, 61)

    fps = 60
    fpsClock = pygame.time.Clock()

    width, height = 1191, 480
    screen = pygame.display.set_mode((width, height))
    base_font = pygame.font.Font(None, 16)

    user_text = []
    # Game loop.
    while True:
        screen.fill((128,128,128))
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and user_text:
                    user_text.pop(-1)
                elif event.key==pygame.K_DELETE:
                    demo = not demo
                elif event.key==pygame.K_RETURN:
                    # Parsa/Hämta ackord här
                    play_chord(_toner)
                else:
                    user_text += event.unicode
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update.
        # Demoläge
        if demo:
            (demo_index, demo_delay_counter, _toner) = demo_mode(demo_index, demo_delay, demo_delay_counter, keylist, _toner)
        # Draw
        draw_keys(keylist,keys,head,_toner,outline_color,highlight_color,screen,multiplier)

        #keylist.append(keylist.pop(0))
        #pygame.draw.polygon(screen, keys[key]["color"], keys[key]["positions"])
        head = return_head()
        pygame.display.flip()
        fpsClock.tick(fps)

# Test function
def main():
    global keys
    head = (0, 0)
    run(head, keys,1)
if __name__ == '__main__':
    main()
