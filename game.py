#! /usr/bin/env python3
# coding: utf-8

"""
Jeu Donkey Kong Labyrinthe
Jeu labyrinthe dans lequel on doit déplacer DK jusqu'aux bananes.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py + levels, images
"""

import pygame
from pygame.locals import *

import constant as ct
import classes as cl

pygame.init()

# Limitation de vitesse de la boucle

# Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
screen = pygame.display.set_mode((ct.SCREEN_BORDER, ct.SCREEN_BORDER))
# Icone
icone = pygame.image.load(ct.ICON_IMG)
pygame.display.set_icon(icone)
# Titre
pygame.display.set_caption(ct.TITLE)

# Boucle infinie
running = 1
while running:
    home = pygame.image.load(ct.HOME_IMG).convert()
    screen.blit(home, (0, 0))
    pygame.display.flip()
    #
    running_game = 1
    running_home = 1
    choice = 0
    #
    while running_home:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    running_home = 0
                    running_game = 0
                    running = 0

                elif event.type == KEYDOWN:
                    if event.key == K_KP1:
                        running_home = 0
                        choice = "ressources/map_1.txt"
                    if event.key == K_KP0:
                        running_home = 0
                        running_game = 0
                        running = 0

    if choice != 0:
        background = pygame.image.load(ct.BCKGRD_IMG).convert()
        #
        level = cl.Level(choice)
        level.generate()
        level.display(screen)
        #
        dk = cl.Actor(ct.MACGYVER_IMG, level)

    while running_game:
        pygame.time.Clock().tick(30)
    #
        for event in pygame.event.get():
        #
        #
            if event.type == QUIT:
                running_game = 0
                running = 0
            elif event.type == KEYDOWN:
                #
                if event.type == K_ESCAPE:
                    running_game = 0
                #
                elif event.key == K_RIGHT:
                    dk.move_actor("right")
                elif event.key == K_LEFT:
                    dk.move_actor("left")
                elif event.key == K_UP:
                    dk.move_actor("up")
                elif event.key == K_DOWN:
                    dk.move_actor("down")
        #
        screen.blit(background, (0, 0))
        level.display(screen)
        #
        screen.blit(dk.direction, (dk.x, dk.y))
        pygame.display.flip()
        #
        if level.map[dk.cy][dk.cx] == "G":
            running_game = 0
pygame.quit()
