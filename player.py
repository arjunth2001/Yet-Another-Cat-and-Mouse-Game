import pygame
from config import *
from objectGame import *

# player class inherits objectGame


class player(objectGame):
    def __init__(self, imageFile, xPos, yPos, width, height):
        super().__init__(imageFile, xPos, yPos, width, height)
    # method that moves player, takes direction as argument

    def move(self, direction, maxHeight, maxWidth):
        if direction == "-y":
            self.yPos -= playerSpeed
        elif direction == "+y":
            self.yPos += playerSpeed
        elif direction == "+x":
            self.xPos += playerSpeed
        elif direction == "-x":
            self.xPos -= playerSpeed

        if self.yPos >= maxHeight - self.height:
            self.yPos = maxHeight - self.height

        elif self.yPos <= 0:
            self.yPos = 0

        if self.xPos >= maxWidth - self.width:
            self.xPos = maxWidth - self.width

        elif self.xPos <= 0:
            self.xPos = 0
    # method that detects collission with an object

    def detect_collision(self, enemybody: objectGame):

        if self.yPos > enemybody.yPos + enemybody.height:
            return False
        elif self.yPos + self.height < enemybody.yPos:
            return False

        if self.xPos > enemybody.xPos + enemybody.width:
            return False
        elif self.xPos + self.height < enemybody.xPos:
            return False
        return True
