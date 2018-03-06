#! /usr/bin/env python3
# coding: utf-8

"""Class for the game."""


import pygame  # needed ?
import logging as lg

import constant as ct

import random


class Actor:
    """This is the class used for MacGyver sprite."""

    def __init__(self, figure, level):
        """self.Position = Char.get_rect()."""
        self.figure = pygame.image.load(ct.MacGyver).convert_alpha()
        self.case_x = 0
        self.case_y = 1
        # Starting from 1 so the hero move down at DOWN_KEY press.
        self.x = 0
        self.y = 30
        # Initial position of character is set bellow the upper black margin.
        self.level = level

    # :
    def mooving(self, direction):
        """Keyboard touch used to moove MacGyver."""
        if direction == 'right':
            if self.case_x < (ct.Nbr_Sprite_Side - 1):
                # Character can't go off screen
                if self.level.structure[self.case_y][self.case_x + 1] != '#':
                    # He can't pass trough walls etheir !
                    self.case_x += 1
                    self.x = self.case_x * ct.Sprite_Size
                    # print(self.x, self.y)

        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != '#':
                    self.case_x -= 1
                    self.x = self.case_x * ct.Sprite_Size
                    # print(self.x, self.y)

        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != '#':
                    if self.level.structure[self.case_y - 1][self.case_x] != 'C':
                        self.case_y -= 1
                        self.y = self.case_y * ct.Sprite_Size
                        # print(self.x, self.y)

        if direction == 'down':
            if self.case_y < (ct.Nbr_Sprite_Side):
                if self.level.structure[self.case_y + 1][self.case_x] != '#':
                    self.case_y += 1
                    self.y = self.case_y * ct.Sprite_Size
                    # print(self.x, self.y)


class Labyrinth:
    """class used for the maze."""

    def __init__(self, file):
        """Init method."""
        self.file = file  # ct.Level
        self.structure = 0

    def generate(self):
        """Generating labyrinth."""
        try:
            with open(self.file, "r") as file:
                # Opening Level.txt as only readable
                map_structure = []
                # defining level structure as an empty list
                for line in file:
                    line_in_map = []
                    for sprite in line:
                        if sprite != '\n':
                            line_in_map.append(sprite)
                            # Sprites to the line_in_map list, except for \n
                    map_structure.append(line_in_map)
                    # We append the line_in_map list to the map_structure_list
                self.structure = map_structure
            # we re-define the structure
        except FileNotFoundError as e:
            lg.critical("Verify if map file exists and is readable")

    def display(self, screen):
        """Display the labyrinth."""
        wall = pygame.image.load(ct.Wall).convert()
        guardian = pygame.image.load(ct.Guardian).convert_alpha()
        try:
            num_line = 0
            for line in self.structure:
                num_case = 0
                for sprite in line:
                    # We check for each sprite in line
                    x = num_case * ct.Sprite_Size
                    # each sprites position is calculated
                    y = num_line * ct.Sprite_Size
                    if sprite == '#':  # m = wall
                        screen.blit(wall, (x, y))
                        # We blit the wall-img to the position on the case
                    elif sprite == 'G':
                        screen.blit(guardian, (x, y))
                        # We blit the guardian-img
                    num_case += 1
                    # once done with a sprite, we follow with the next entry
                num_line += 1
                # once done with a line, we follow with the next
        except FileNotFoundError as e:
            lg.critical("Characters images must be complete in their rep.")


class Bonus:
    """The class for the items."""

    def __init__(self, extra, map):
        """Init items."""
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        self.map = map
        self.loaded = True
        self.extra = extra
        self.structure = list(self.map.structure)

    def display(self, extra, screen):
        """Display items in random sprites."""
        while self.loaded:
            self.case_x = random.randint(0, ct.Nbr_Sprite_Side - 1)
            # We randomize the case_x position
            self.case_y = random.randint(0, ct.Nbr_Sprite_Side - 1)
            # same for case_y position
            if self.structure[self.case_y][self.case_x] == '0':
                # if the randomized position is located on a free space
                self.y = self.case_y * ct.Sprite_Size
                # We define/accept the position for the object
                self.x = self.case_x * ct.Sprite_Size
                self.loaded = False
                # Once we have defined a items position, we kill the loop
