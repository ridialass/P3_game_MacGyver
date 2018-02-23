#! /usr/bin/env python3
# coding: utf-8

"""
Save MacGyver !
A Game in wich we must help MacGyver finding is way around a maze
in order to escape he must reach the exit, but before then he must
pick up objects along the way in order to conceive a siringue of chemical
so he can put to sleep the guard at the exit !

 Python Script
 Files : maze.py, classes.py, constantes.py, level.txt + images
 """

# Import of the libraries needed
import pygame
from pygame.locals import *
import constant as ct
import classes as cl

# Init of the Pygame library
pygame.init()

# Displaying the windows
Window = pygame.display.set_mode((ct.Window_Size, 480))  # setting the height to 480 so we have an upper black margin
# Icone
icone = pygame.image.load(ct.MacGyver).convert_alpha()
pygame.display.set_icon(icone)
# Title
pygame.display.set_caption(ct.Window_Title)


# displaying a background for the tile of the maze
Background_Tiles = pygame.image.load(ct.background).convert()
Window.blit(Background_Tiles, (30, 30))  # the background is streched from below the black margin to the opposite corner

# displaying the character .png
Char_img = pygame.image.load(ct.MacGyver).convert_alpha()  # Add the png and transparency

# displaying the walls of the maze
wall = pygame.image.load(ct.Wall).convert()

# displaying the objects png's
tubeIMG = pygame.image.load(ct.Tube).convert_alpha()
needleIMG = pygame.image.load(ct.Needle).convert_alpha()
etherIMG = pygame.image.load(ct.Ether).convert_alpha()


# refreshing the screen for the background to be visible over the default one
pygame.display.flip()

# Variable for the infinite loop
continue_game = 1

# Variables to check if the items have been picked or not:
TubeNotPicked = True
EtherNotPicked = True
NeedleNotPicked = True

GAME_WON = False
GAME_LOOSE = False

pygame.key.set_repeat(400, 30)  #Moving MaGyver by maintening a arrow_key pressed

level = cl.Level(ct.Level)
level.generate()
level.display(Window)
Mac = cl.Char(Char_img, level)
tube = cl.Loot(tubeIMG, level)
tube.display(tubeIMG, Window)
needle = cl.Loot(needleIMG, level)
needle.display(needleIMG, Window)
ether = cl.Loot(etherIMG, level)
ether.display(etherIMG, Window)


# infinite loop
while continue_game:

    pygame.time.Clock().tick(30)  # Limiting the loop speed to 30f/s to save processor ressources

    for event in pygame.event.get():    #Seeking every events happening while the game is running
        if event.type == QUIT:  # If any of these events is QUIT type
            continue_game = 0   # Loop is stopped and the game windows is closed

        # Keyboard touch used to moove MacGyver:
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:  # If ARROW DOWN pressed
                Mac.mooving('down')
            elif event.key == K_UP:
                Mac.mooving('up')
            elif event.key == K_LEFT:
                Mac.mooving('left')
            elif event.key == K_RIGHT:
                Mac.mooving('right')


    # Re-pasting after the events
    Window.blit(Background_Tiles, (0, 30))  # the background is streched from below the black margin to the opposite corner
    level.display(Window)
    Window.blit(Mac.Image, (Mac.x, Mac.y))

    if TubeNotPicked:
        Window.blit(tube.extra, (tube.x, tube.y))
    if (Mac.x, Mac.y) == (tube.x, tube.y):
        TubeNotPicked = False
        Window.blit(tube.extra, (0, 0))

    if NeedleNotPicked:
        Window.blit(needle.extra, (needle.x, needle.y))
    if (Mac.x, Mac.y) == (needle.x, needle.y):
        NeedleNotPicked = False
        Window.blit(needle.extra, (10, 0))

    if EtherNotPicked:
        Window.blit(ether.extra, (ether.x, ether.y))
    if (Mac.x, Mac.y) == (ether.x, ether.y):
        EtherNotPicked = False
        Window.blit(ether.extra, (30, 0))


    # refreshing screen
    pygame.display.flip()


    # EndGame Victory or loose
    if level.structure[Mac.case_y][Mac.case_x] == 'a':  # If MacGyver reach the guard :
        if TubeNotPicked is False and NeedleNotPicked is False and EtherNotPicked is False:  # If every objects have been looted, he won.
            GAME_WON = True
        else:
            GAME_LOOSE = True  # Else it's game over !


    if GAME_WON is True:
        Window.blit(Background_Tiles, (0, 30))  # draw over everything on the screen now by re-drawing the background
        font = pygame.font.Font(None, 25)
        text = font.render("You won ! MacGyver is safe thanks to you !", 1, (255, 255, 255)) # Display the text in white with rounded edge
        textrect = text.get_rect()
        textrect.centerx, textrect.centery = ct.Window_Size / 2, ct.Window_Size / 2  # Centering the text
        Window.blit(text, textrect)

        pygame.display.flip()

    if GAME_LOOSE is True:
        Window.blit(Background_Tiles, (0, 30))  # draw over everything on the screen now by re-drawing the background
        font = pygame.font.Font(None, 25)
        text = font.render("Game over! You just died.", 1, (255, 255, 255))  # Display the text in white with rounded edge
        textrect = text.get_rect()
        textrect.centerx, textrect.centery = ct.Window_Size / 2, ct.Window_Size / 2
        Window.blit(text, textrect)

        pygame.display.flip()
