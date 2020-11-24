import pygame
from objectGame import *
from config import *

# class shiporRock inherits objectGame


class shiporRock(objectGame):

    def __init__(
        self,
        imageFile,
        xPos,
        yPos,
        width,
        height,
        speed,
    ):
        super().__init__(imageFile, xPos, yPos, width, height)
        self.speed = speed
    # method that moves the object

    def move(
        self,
        max_width,
        prevWinner,
        speedIncrease1,
        speedIncrease2,
    ):

        if self.xPos >= max_width:
            self.xPos = -self.width
        if prevWinner == '1':
            self.xPos += self.speed + speedIncrease1
        elif prevWinner == '2':
            self.xPos += self.speed + speedIncrease2
        else:
            self.xPos += self.speed
