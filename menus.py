import pygame
from config import *
from level import *

# method that shows instruction screen


def instruction(clevel):
    background_ins = objectGame(INST_IMAGE, 0, 0, 1811, 996)
    background_ins.objDraw
    while not clevel.gameOver:
        clevel.game_screen.fill((110, 159, 211))
        background_ins.objDraw(clevel.game_screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                clevel.gameOver = 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

# method that shows main menu


def main_menu():

    pygame.mixer.music.load(MUSIC_SCORE)
    pygame.mixer.music.play(-1)
    clevel = level(GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
    background_menu = objectGame(MENU_IMAGE, 0, 0, 1811, 996)
    background_menu.objDraw
    while not clevel.gameOver:
        clevel = level(GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
        clevel.game_screen.fill((110, 159, 211))
        background_menu.objDraw(clevel.game_screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                clevel.gameOver = 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    clevel.run_level_loop()
                if event.key == pygame.K_RETURN:
                    instruction(clevel)
                if event.key == pygame.K_KP_ENTER:
                    instruction(clevel)
