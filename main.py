#! /usr/bin/env python
"""
Driver for SOM visualization
"""


#Import Modules
import os, pygame
from pygame.locals import *

import setup
import som as somlib
from lib import keyboard


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""

#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((1024, 668))
    pygame.display.set_caption('Fuzz!')
    pygame.mouse.set_visible(1)

#Create The Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

#Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Car Fuzzy Inferencenator", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)
    else:
        print "NO FONTS!"

#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

#Prepare Game Objects
    clock = pygame.time.Clock()

    som = somlib.Som()
    somVis = somlib.SomVisualizer(som)

    keyRemember = keyboard.KeyboardRemember((K_SPACE,))
#Main Loop
    while 1:
        clock.tick(60)

    #Handle Input Events
        lastDirKey = -1     # something invalid
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type is KEYDOWN and (event.key == K_ESCAPE or event.key == K_q):
                return

            keyRemember.update(event)

        som.update()

    #Draw Everything
        screen.blit(background, (0, 0)) # blank out the whole screen (for now)
        somVis.draw(screen)
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()

