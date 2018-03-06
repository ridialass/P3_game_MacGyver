#! /usr/bin/env python3
# coding: utf-8


"""
Save MacGyver !
A Game in wich we try to help MacGyver finding is way inside a Labyrinth.
To escape, he needs to pick up  3 objects along the way in order
to make a chemical portion to sleep the guard at the exit !

Python Script
Files : game.py, classes.py, constant.py, ressources, sounds + images
"""

# Import of the libraries needed
import pygame
from pygame import locals
from os import environ
from sys import exit

import constant as ct
import classes as cl

# Center the window on screen
environ['SDL_VIDEO_CENTEred'] = '1'
# Initiation of the Pygame library
pygame.init()

# Creation of the main window
screen = pygame.display.set_mode((ct.W_Side, 480))
# Icone
icone = pygame.image.load(ct.Icone).convert_alpha()
pygame.display.set_icon(icone)
# Title
pygame.display.set_caption(ct.Window_Title)
# Loading a floor for the labyrinth after the home page
home = pygame.image.load(ct.Home).convert()
floor = pygame.image.load(ct.Background).convert()
# Loading MacGyver
mc_img = pygame.image.load(ct.MacGyver).convert_alpha()
# Loading the walls of the labyrinth
wall = pygame.image.load(ct.Wall).convert()
# Loading the objects
tube_img = pygame.image.load(ct.Tube).convert_alpha()
needle_img = pygame.image.load(ct.Needle).convert_alpha()
ether_img = pygame.image.load(ct.Ether).convert_alpha()
# Sounds and Music
sound_win = pygame.mixer.Sound("sounds/train.wav")
sound_win.set_volume(0.5)
sound_loose = pygame.mixer.Sound("sounds/loose_1.wav")
sound_loose.set_volume(0.5)
level_1 = False
level_2 = False


def go_ahead_level_1():
    """Make a choice to play again or live."""
    running_result = 1
    while running_result:
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            # Seeking every events happening while the game is running
            if event.type == locals.QUIT:
                # If any of these events is QUIT type
                exit()
                # Loop is stopped and the game windows is closed
            elif event.type == locals.KEYDOWN:
                if event.key == locals.K_ESCAPE:
                    exit()
                elif event.key == locals.K_RETURN:
                    game_level_1()


def go_ahead_level_2():
    """Make a choice to play again or live."""
    running_result = 1
    while running_result:
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            # Seeking every events happening while the game is running
            if event.type == locals.QUIT:
                # If any of these events is QUIT type
                exit()
                # Loop is stopped and the game windows is closed
            elif event.type == locals.KEYDOWN:
                if event.key == locals.K_ESCAPE:
                    exit()
                elif event.key == locals.K_RETURN:
                    game_level_2()


def end_message(alert_text=' Game-over', app_text='Well-done'):
    """Message in case we loose."""
    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    screen.fill(white)
    # draw over everything on the screen now by re-drawing the background
    font = pygame.font.Font('ressources/BLKCHCRY.TTF', 30)
    text_1 = font.render(alert_text, True, red)
    text_2 = font.render(app_text, True, black)
    text_3 = font.render('Now, please press:', 1, green)
    text_4 = font.render('"Escape" to leave or "Enter" to replay', 1, black)
    # Display the text in white with rounded edge
    textrect_1 = text_1.get_rect()
    textrect_1.centerx, textrect_1.centery = ct.W_Side / 2, ct.W_Side / 2.75
    textrect_2 = text_2.get_rect()
    textrect_2.centerx, textrect_2.centery = ct.W_Side / 2, ct.W_Side / 2
    textrect_3 = text_3.get_rect()
    textrect_3.centerx, textrect_3.centery = ct.W_Side / 2, ct.W_Side / 1.5
    textrect_4 = text_4.get_rect()
    textrect_4.centerx, textrect_4.centery = ct.W_Side / 2, ct.W_Side / 1.25
    # Centering the text_1
    screen.blit(text_1, textrect_1)
    screen.blit(text_2, textrect_2)
    screen.blit(text_3, textrect_3)
    screen.blit(text_4, textrect_4)


def game_level_1():
    """Level_1."""
    pygame.mixer.music.load(ct.Music_1)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    game_loop(ct.Map_1)


def game_level_2():
    """Level_1."""
    pygame.mixer.music.load(ct.Music_2)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    game_loop(ct.Map_2)


def game_loop(level):
    """Main loop."""
    # Moving MaGyver by maintening a direction_key pressed
    pygame.key.set_repeat(400, 30)
    # Instanciation of class objects and usage of their methods
    stage = cl.Labyrinth(level)
    stage.generate()
    stage.display(screen)
    macgyver = cl.Actor(mc_img, stage)
    tube = cl.Bonus(tube_img, stage)
    tube.display(tube_img, screen)
    needle = cl.Bonus(needle_img, stage)
    needle.display(needle_img, screen)
    ether = cl.Bonus(ether_img, stage)
    ether.display(ether_img, screen)
    # Variables for different status of the game
    running = 1
    running_game = 0
    running_home = 0
    # Variables to check if objects have been picked-up or not
    tube_on = True
    ether_on = True
    needle_on = True
    # Variable for game result
    won = False
    loose = False
    # Loop starts
    while running:
        # Limiting the loop speed to 30f/s to save processor ressources
        screen.blit(home, (0, 0))
        pygame.display.flip()
        running_home = 1
        while running_home:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                # Seeking every events happening while the game is running
                if event.type == locals.QUIT:
                    # If any of these events is QUIT type
                    running_game = 0
                    running_home = 0
                    running = 0
                    # Loop is stopped and the game windows is closed
                elif event.type == locals.KEYDOWN:
                    if event.key == locals.K_ESCAPE:
                        running_game = 0
                        running_home = 0
                        running = 0
                    elif event.key == locals.K_RETURN:
                        running_home = 0
                        running_game = 1
        while running_game == 1:
            pygame.time.Clock().tick(30)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == locals.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == locals.KEYDOWN:
                    # Keyboard touch used to moove MacGyver:
                    if event.key == locals.K_DOWN:
                        macgyver.mooving('down')
                    elif event.key == locals.K_UP:
                        macgyver.mooving('up')
                    elif event.key == locals.K_LEFT:
                        macgyver.mooving('left')
                    elif event.key == locals.K_RIGHT:
                        macgyver.mooving('right')
            # Re-pasting after the events
            screen.blit(floor, (0, 30))
            # the background is streched from below the black margin
            stage.display(screen)
            screen.blit(macgyver.figure, (macgyver.x, macgyver.y))
            # Picking stuff
            if tube_on:
                screen.blit(tube.extra, (tube.x, tube.y))
            if (macgyver.x, macgyver.y) == (tube.x, tube.y):
                tube_on = False
                screen.blit(tube.extra, (0, 0))
            if needle_on:
                screen.blit(needle.extra, (needle.x, needle.y))
            if (macgyver.x, macgyver.y) == (needle.x, needle.y):
                needle_on = False
                screen.blit(needle.extra, (10, 0))
            if ether_on:
                screen.blit(ether.extra, (ether.x, ether.y))
            if (macgyver.x, macgyver.y) == (ether.x, ether.y):
                ether_on = False
                screen.blit(ether.extra, (30, 0))
            # refreshing screen

            # EndGame Victory or loose
            if stage.structure[macgyver.case_y][macgyver.case_x] == 'G':
                # If MacGyver reach the guard
                tube_off = tube_on is False
                needle_off = needle_on is False
                ether_off = ether_on is False
                if tube_off and needle_off and ether_off:
                    # If every objects have been looted, he won.
                    won = True
                    pygame.mixer.Sound.play(sound_win)
                else:
                    loose = True  # Else it's game over !
                    pygame.mixer.Sound.play(sound_loose)

            if won is True:
                notification = 'You have won !'
                appreciation = 'MacGyver is safe thanks to you !'
                end_message(notification, appreciation)
                go_ahead_level_2()
            if loose is True:
                notification = 'You have lost!'
                appreciation = 'MacGyver is killed !'
                end_message(notification, appreciation)
                go_ahead_level_1()
                # pygame.display.flip()

game_level_1()
pygame.mixer.music.stop()
pygame.quit()
exit()
