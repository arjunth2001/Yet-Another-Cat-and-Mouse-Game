import pygame

# class that defines objects of game

# paren of player and shiporrock


class objectGame:
    def __init__(self, imageFile, objX, objY, objWidth, objHeight):
        self.xPos = objX
        self.yPos = objY
        self.width = objWidth
        self.height = objHeight
        self.image = pygame.transform.scale(
            pygame.image.load(imageFile), (objWidth, objHeight))
    # method that draws on screen the object

    def objDraw(self, background):
        background.blit(self.image, (self.xPos, self.yPos))
