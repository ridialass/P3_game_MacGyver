#! /usr/bin/env python3
# coding: utf-8
"""Creating classes"""

import pygame
import constant as ct


class Level:
    """Docstring for Level"""

    def __init__(self, file):
        """Initialize class"""
        self.file = file
        self.map = 0

    def generate(self):
        """Generating map from file"""
        with open(self.file, "r") as file:
            map_level = []
            # reading lines from file
            for line in file:
                line_level = []
                # readind sprites from file
                for sprite in line:
                    # ignoring back-charet
                    if sprite != "\n":
                        line_level.append(sprite)
                # adding line to level list
                map_level.append(line_level)
            # saving the map
            self.map = map_level

    #
    def display(self, screen):
        """Displaying th map from generation"""
        # loading images
        wall = pygame.image.load(ct.WALL_IMG).convert()
        departure = pygame.image.load(ct.DEPARTURE_IMG).convert()
        arrival = pygame.image.load(ct.GATEKEEPER_IMG).convert_alpha()
        # browsing the level list
        numb_line = 0
        for line in self.map:
            # browsing the line list
            numb_case = 0
            for sprite in line:
                # calculating real position in pixels
                x = numb_case * ct.SPRITE_WIDTH
                y = numb_line * ct.SPRITE_WIDTH
                if sprite == " ":
                    screen.blit(wall, (x, y))
                if sprite == "M":
                    screen.blit(departure, (x, y))
                if sprite == "G":
                    screen.blit(arrival, (x, y))
                numb_case += 1
            numb_line += 1


#
class Actor:
    """Docstring for Actor"""

    def __init__(self, hero, level):
        """Actor architecture"""
        #
        self.hero = pygame.image.load(hero).convert_alpha()
        #
        self.cx = 0
        self.cy = 0
        self.x = 0
        self.y = 0
        #
        self.direction = self.hero
        self.level = level

    #
    def move_actor(self, direction):
        """Moving the actor"""
        # moving actor to the right
        if direction == "right":
            #
            if self.cx < (ct.LINE_SPRITE_NUMBER - 1):
                #
                if self.level.map[self.cy][self.cx + 1] != "#":
                    #
                    self.cx += 1
                    #
                    self.x = self.cx * ct.SPRITE_WIDTH
            #
            self.direction = self.hero
        # moving actor to the left
        if direction == "left":
            if self.cx > 0:
                if self.level.map[self.cy][self.cx - 1] != "#":
                    self.cx -= 1
                    self.x = self.cx * ct.SPRITE_WIDTH
            self.direction = self.hero
        # Moving actor up
        if direction == "up":
            if self.cy > 0:
                if self.level.map[self.cy - 1][self.cx] != "#":
                    self.cy -= 1
                    self.y = self.cy * ct.SPRITE_WIDTH
            self.direction = self.hero
        # Moving actor down
        if direction == "down":
            if self.cy < (ct.SPRITE_WIDTH - 1):
                if self.level.map[self.cy + 1][self.cx] != "#":
                    self.cy += 1
                    self.y = self.cy * ct.SPRITE_WIDTH
            self.direction = self.hero
