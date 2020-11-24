import pygame
from config import *
from objectGame import *
from player import *
from shipOrRock import *
import math

# to be initialised from menu


class level:
    # variables that store values for lvl
    winner = 'None'  # winner of lvl
    Player1Score = 0
    Player2Score = 0
    Player1Time = 0
    Player2Time = 0
    Player1Cross = 0
    Player2Cross = 0
    levelOver = 0
    gameOver = 0
    timeLimit1 = 30
    timeLimit2 = 30
    speedIncrease1 = 0  # implementation of speed increase
    speedIncrease2 = 0
    prevWinner = '0'
    escape = 0
    # the class constructor

    def __init__(
        self,
        title,
        width,
        height,
    ):
        self.title = title
        self.width = width
        self.height = height
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
    # method that pauses

    def pause(self):
        # pauses the music,
        # because people usually pause games
        # during calls and stuff

        pygame.mixer.music.pause()

        # the pause screen image
        background_pause = objectGame(PAUSE_IMG, 0, 0, 1811, 996)
        background_pause.objDraw
        paused = True
        # calculating time spent inside
        # this funtion to compensate in main loop

        startTime = pygame.time.get_ticks()
        seconds = 0
        while paused:
            self.game_screen.fill((110, 159, 211))
            background_pause.objDraw(self.game_screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = 1
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        paused = False
        seconds = pygame.time.get_ticks() - startTime
        # unpause music before leaving
        pygame.mixer.music.unpause()
        return seconds

    # method that sets winner for level
    def getWinner(self):
        # the whole logic for finding winner
        # is available in instructions
        if not self.Player1Cross and self.Player2Cross:
            self.winner = '2'
            self.prevWinner = '2'
            self.timeLimit2 += 10
        elif not self.Player2Cross and self.Player1Cross:

            self.winner = '1'
            self.prevWinner = '1'
            self.timeLimit1 += 10
        elif not self.Player2Cross and not self.Player1Cross:
            self.winner = 'None'
        else:
            if self.Player1Time > self.Player2Time:
                self.winner = '2'
                self.prevWinner = '2'
                self.timeLimit2 += 10
            elif self.Player2Time > self.Player1Time:
                self.winner = '1'
                self.prevWinner = '1'
                self.timeLimit1 += 10
            else:
                if self.Player1Score > self.Player2Score:
                    self.winner = '1'
                    self.prevWinner = '1'
                    self.timeLimit1 += 10
                elif self.Player2Score > self.Player1Score:
                    self.winner = '2'
                    self.prevWinner = '2'
                    self.timeLimit2 += 10
                else:
                    self.winner = 'Tie'
#  method that ends the level

    def endlevel(self):
        # renders text to the screen before next lvl
        if self.levelOver and self.winner == '1':
            text = FONT.render(WIN1MSG, True, BLACK_COLOR)
        elif self.levelOver and self.winner == '2':
            text = FONT.render(WIN2MSG, True, BLACK_COLOR)
        elif self.levelOver and self.winner == 'None':
            text = FONT.render(LOST, True, BLACK_COLOR)
        else:
            text = FONT.render(TIE, True, BLACK_COLOR)
        self.game_screen.blit(text, (825, 350))
        pygame.display.update()
        CLOCK.tick(1)

    # method that runs main loop
    def run_level_loop(self):
        self.winner = 'None'
        self.Player1Score = 0
        self.Player2Score = 0
        self.Player1Time = 0
        self.Player2Time = 0
        self.Player1Cross = 0
        self.Player2Cross = 0
        self.levelOver = 0
        self.gameOver = 0
        self.escape = 0
        flag = [0] * 100
        direction = 0
        # initialising all objects
        # printing to screen
        Player1 = player(MOUSE_UP, 880, 900, 36, 40)
        Player2 = player(MOUSE_DOWN, 880, 0, 36, 40)
        enemy1 = shiporRock(
            CAT,
            20,
            594,
            72,
            56,
            S1,
        )
        enemy2 = shiporRock(
            CAT,
            20,
            424,
            72,
            56,
            S2,
        )
        enemy3 = shiporRock(
            FOX,
            20,
            260,
            68,
            55,
            S3,
        )
        enemy4 = shiporRock(
            FOX,
            20,
            766,
            68,
            55,
            S3,
        )
        enemy5 = shiporRock(
            CAT,
            20,
            98,
            68,
            56,
            S2,
        )
        enemy6 = shiporRock(
            FOX,
            560,
            594,
            72,
            56,
            S1,
        )
        enemy7 = shiporRock(
            CAT,
            340,
            424,
            72,
            56,
            S2,
        )
        enemy8 = shiporRock(
            CAT,
            430,
            260,
            68,
            55,
            S3,
        )
        enemy9 = shiporRock(
            CAT,
            700,
            766,
            68,
            55,
            S3,
        )
        enemy10 = shiporRock(
            FOX,
            390,
            98,
            68,
            56,
            S2,
        )
        coin1 = objectGame(COIN_IMG, 1363, 380, 53, 56)
        coin2 = objectGame(COIN_IMG, 1486, 380, 53, 56)
        coin3 = objectGame(COIN_IMG, 1607, 380, 53, 56)
        coin4 = objectGame(COIN_IMG, 1707, 380, 53, 56)
        coin5 = objectGame(COIN_IMG, 1127, 712, 53, 56)
        coin6 = objectGame(COIN_IMG, 2, 480, 53, 56)
        coin7 = objectGame(COIN_IMG, 137, 480, 53, 56)
        coin8 = objectGame(COIN_IMG, 262, 480, 53, 56)
        coin9 = objectGame(COIN_IMG, 382, 480, 53, 56)
        coin10 = objectGame(COIN_IMG, 845, 480, 53, 56)
        coin11 = objectGame(COIN_IMG, 629, 371, 53, 56)
        coin12 = objectGame(COIN_IMG, 1483, 712, 53, 56)
        coin13 = objectGame(COIN_IMG, 1610, 712, 53, 56)
        coin14 = objectGame(COIN_IMG, 1725, 712, 53, 56)
        coin15 = objectGame(COIN_IMG, 10, 200, 53, 56)
        coin16 = objectGame(COIN_IMG, 152, 200, 53, 56)
        coin17 = objectGame(COIN_IMG, 265, 200, 53, 56)
        life1 = objectGame(CRYSTAL, 135, 376, 27, 55)
        life2 = objectGame(CRYSTAL, 1670, 482, 27, 55)
        life3 = objectGame(CRYSTAL, 1663, 151, 27, 55)
        life4 = objectGame(CRYSTAL, 121, 720, 27, 55)
        fence1 = objectGame(FENCE, 0, 535, 482, 54)
        fence2 = objectGame(FENCE, 1329, 546, 482, 54)
        fence3 = objectGame(FENCE, 0, 316, 482, 54)
        fence4 = objectGame(FENCE, 1329, 207, 482, 54)
        fence5 = objectGame(FENCE, 1329, 316, 482, 54)
        fence6 = objectGame(FENCE, 0, 645, 482, 54)
        rock1 = objectGame(ROCKS, 19, 826, 68, 57)
        rock2 = objectGame(ROCKS, 643, 648, 68, 57)
        rock3 = objectGame(ROCKS, 880, 823, 68, 57)
        rock4 = objectGame(ROCKS, 880, 151, 68, 57)
        rock5 = objectGame(ROCKS, 1130, 370, 68, 57)
        bomb1 = objectGame(BOMB, 883, 544, 74, 58)
        bomb2 = objectGame(BOMB, 1147, 206, 74, 58)
        bomb3 = objectGame(BOMB, 648, 715, 74, 58)
        bomb4 = objectGame(BOMB, 1372, 720, 74, 58)

        background = objectGame(BCKGRND, 0, 0, 1811, 996)

        self.game_screen.fill((110, 159, 211))
        background.objDraw(self.game_screen)
        Player1.move(direction, self.height, self.width)
        Player1.objDraw(self.game_screen)
        enemy1.move(self.width, '1', self.speedIncrease1,
                    self.speedIncrease2)
        enemy1.objDraw(self.game_screen)
        enemy2.move(self.width, '1', self.speedIncrease1,
                    self.speedIncrease2)
        enemy2.objDraw(self.game_screen)
        enemy3.move(self.width, '1', self.speedIncrease1,
                    self.speedIncrease2)
        enemy3.objDraw(self.game_screen)
        enemy4.move(self.width, '1', self.speedIncrease1,
                    self.speedIncrease2)
        enemy4.objDraw(self.game_screen)
        enemy5.move(self.width, '1', self.speedIncrease1,
                    self.speedIncrease2)
        enemy5.objDraw(self.game_screen)
        enemy6.move(self.width, '1', self.speedIncrease1,
                    self.speedIncrease2)
        enemy6.objDraw(self.game_screen)
        enemy7.move(self.width, '1', self.speedIncrease1,
                    self.speedIncrease2)
        enemy7.objDraw(self.game_screen)
        enemy8.move(self.width, '1', self.speedIncrease1,
                    self.speedIncrease2)
        enemy8.objDraw(self.game_screen)
        enemy9.move(self.width, '1', self.speedIncrease1,
                    self.speedIncrease2)
        enemy9.objDraw(self.game_screen)
        enemy10.move(self.width, '1', self.speedIncrease1,
                     self.speedIncrease2)
        enemy10.objDraw(self.game_screen)
        coin1.objDraw(self.game_screen)
        coin2.objDraw(self.game_screen)
        coin3.objDraw(self.game_screen)
        coin4.objDraw(self.game_screen)
        coin5.objDraw(self.game_screen)
        coin6.objDraw(self.game_screen)
        coin7.objDraw(self.game_screen)
        coin8.objDraw(self.game_screen)
        coin9.objDraw(self.game_screen)
        coin10.objDraw(self.game_screen)
        coin11.objDraw(self.game_screen)
        coin12.objDraw(self.game_screen)
        coin13.objDraw(self.game_screen)
        coin14.objDraw(self.game_screen)
        coin15.objDraw(self.game_screen)
        coin16.objDraw(self.game_screen)
        coin17.objDraw(self.game_screen)
        fence1.objDraw(self.game_screen)
        fence2.objDraw(self.game_screen)
        fence3.objDraw(self.game_screen)
        fence4.objDraw(self.game_screen)
        fence5.objDraw(self.game_screen)
        fence6.objDraw(self.game_screen)
        rock1.objDraw(self.game_screen)
        rock2.objDraw(self.game_screen)
        rock3.objDraw(self.game_screen)
        rock4.objDraw(self.game_screen)
        rock5.objDraw(self.game_screen)
        life1.objDraw(self.game_screen)
        life2.objDraw(self.game_screen)
        life3.objDraw(self.game_screen)
        life4.objDraw(self.game_screen)
        bomb1.objDraw(self.game_screen)
        bomb2.objDraw(self.game_screen)
        bomb3.objDraw(self.game_screen)
        bomb4.objDraw(self.game_screen)

        text = FONT.render(PLAYER1, True, BLACK_COLOR)
        self.game_screen.blit(text, (825, 350))
        text = FONT1.render(MSG1, True, BLACK_COLOR)
        self.game_screen.blit(text, (1300, 912))
        text = FONT1.render(MSG2, True, BLACK_COLOR)
        Player2.objDraw(self.game_screen)
        self.game_screen.blit(text, (1300, 14))
        pygame.display.update()
        CLOCK.tick(1)

        # Here goes the main loop of P1
        # Starting time from here
        timerStart = pygame.time.get_ticks()
        while not self.gameOver:
            seconds = math.floor((pygame.time.get_ticks() - timerStart) / 1000)
            # loop through events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = '-y'
                    elif event.key == pygame.K_DOWN:
                        direction = '+y'
                    elif event.key == pygame.K_RIGHT:
                        direction = '+x'
                    elif event.key == pygame.K_LEFT:
                        direction = '-x'
                    elif event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_p:
                        timerStart += self.pause()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key \
                        == pygame.K_DOWN or event.key == pygame.K_RIGHT \
                            or event.key == pygame.K_LEFT:
                        direction = 0
            # drawing the objects again
            self.game_screen.fill((110, 159, 211))
            background.objDraw(self.game_screen)

            Player1.move(direction, self.height, self.width)
            Player1.objDraw(self.game_screen)
            enemy1.move(self.width, '1', self.speedIncrease1,
                        self.speedIncrease2)
            enemy1.objDraw(self.game_screen)
            enemy2.move(self.width, '1', self.speedIncrease1,
                        self.speedIncrease2)
            enemy2.objDraw(self.game_screen)
            enemy3.move(self.width, '1', self.speedIncrease1,
                        self.speedIncrease2)
            enemy3.objDraw(self.game_screen)
            enemy4.move(self.width, '1', self.speedIncrease1,
                        self.speedIncrease2)
            enemy4.objDraw(self.game_screen)
            enemy5.move(self.width, '1', self.speedIncrease1,
                        self.speedIncrease2)
            enemy5.objDraw(self.game_screen)
            enemy6.move(self.width, '1', self.speedIncrease1,
                        self.speedIncrease2)
            enemy6.objDraw(self.game_screen)
            enemy7.move(self.width, '1', self.speedIncrease1,
                        self.speedIncrease2)
            enemy7.objDraw(self.game_screen)
            enemy8.move(self.width, '1', self.speedIncrease1,
                        self.speedIncrease2)
            enemy8.objDraw(self.game_screen)
            enemy9.move(self.width, '1', self.speedIncrease1,
                        self.speedIncrease2)
            enemy9.objDraw(self.game_screen)
            enemy10.move(self.width, '1', self.speedIncrease1,
                         self.speedIncrease2)
            enemy10.objDraw(self.game_screen)
            coin1.objDraw(self.game_screen)
            coin2.objDraw(self.game_screen)
            coin3.objDraw(self.game_screen)
            coin4.objDraw(self.game_screen)
            coin5.objDraw(self.game_screen)
            coin6.objDraw(self.game_screen)
            coin7.objDraw(self.game_screen)
            coin8.objDraw(self.game_screen)
            coin9.objDraw(self.game_screen)
            coin10.objDraw(self.game_screen)
            coin11.objDraw(self.game_screen)
            coin12.objDraw(self.game_screen)
            coin13.objDraw(self.game_screen)
            coin14.objDraw(self.game_screen)
            coin15.objDraw(self.game_screen)
            coin16.objDraw(self.game_screen)
            coin17.objDraw(self.game_screen)
            fence1.objDraw(self.game_screen)
            fence2.objDraw(self.game_screen)
            fence3.objDraw(self.game_screen)
            fence4.objDraw(self.game_screen)
            fence5.objDraw(self.game_screen)
            fence6.objDraw(self.game_screen)
            rock1.objDraw(self.game_screen)
            rock2.objDraw(self.game_screen)
            rock3.objDraw(self.game_screen)
            rock4.objDraw(self.game_screen)
            rock5.objDraw(self.game_screen)
            life1.objDraw(self.game_screen)
            life2.objDraw(self.game_screen)
            life3.objDraw(self.game_screen)
            life4.objDraw(self.game_screen)
            bomb1.objDraw(self.game_screen)
            bomb2.objDraw(self.game_screen)
            bomb3.objDraw(self.game_screen)
            bomb4.objDraw(self.game_screen)
            text = FONT1.render(MSG1, True, BLACK_COLOR)
            self.game_screen.blit(text, (1300, 912))
            text = FONT1.render(MSG2, True, BLACK_COLOR)
            self.game_screen.blit(text, (1300, 14))
            Player1.objDraw(self.game_screen)

            # flag array that checks if player crossed
            # the score should not increase even if the player
            # crosses the lines again
            if Player1.detect_collision(enemy1):
                break
            elif Player1.detect_collision(enemy2):
                break
            elif Player1.detect_collision(enemy3):
                break
            elif Player1.detect_collision(enemy4):
                break
            elif Player1.detect_collision(enemy5):
                break
            elif Player1.detect_collision(enemy6):
                break
            elif Player1.detect_collision(enemy7):
                break
            elif Player1.detect_collision(enemy8):
                break
            elif Player1.detect_collision(enemy9):
                break
            elif Player1.detect_collision(enemy10):
                break
            elif Player1.detect_collision(rock1):
                break
            elif Player1.detect_collision(rock2):
                break
            elif Player1.detect_collision(rock3):
                break
            elif Player1.detect_collision(rock4):
                break
            elif Player1.detect_collision(rock5):
                break
            elif Player1.detect_collision(bomb1):
                break
            elif Player1.detect_collision(bomb2):
                break
            elif Player1.detect_collision(bomb3):
                break
            elif Player1.detect_collision(bomb4):
                break
            elif Player1.detect_collision(fence1):
                break
            elif Player1.detect_collision(fence2):
                break
            elif Player1.detect_collision(fence3):
                break
            elif Player1.detect_collision(fence4):
                break
            elif Player1.detect_collision(fence5):
                break
            elif Player1.detect_collision(fence6):
                break
            elif Player1.detect_collision(life1):
                seconds -= 10
                life1.xPos = -99
            elif Player1.detect_collision(life2):
                seconds -= 10
                life2.xPos = -99
            elif Player1.detect_collision(life3):
                seconds -= 10
                life3.xPos = -99
            elif Player1.detect_collision(life4):
                seconds -= 10
                life4.xPos = -99
            elif Player1.detect_collision(coin1):
                self.Player1Score += 3
                coin1.xPos = -99
            elif Player1.detect_collision(coin2):
                self.Player1Score += 3
                coin2.xPos = -99
            elif Player1.detect_collision(coin3):
                self.Player1Score += 3
                coin3.xPos = -99
            elif Player1.detect_collision(coin4):
                self.Player1Score += 3
                coin4.xPos = -99
            elif Player1.detect_collision(coin5):
                self.Player1Score += 3
                coin5.xPos = -99
            elif Player1.detect_collision(coin6):
                self.Player1Score += 3
                coin6.xPos = -99
            elif Player1.detect_collision(coin7):
                self.Player1Score += 3
                coin7.xPos = -99
            elif Player1.detect_collision(coin8):
                self.Player1Score += 3
                coin8.xPos = -99
            elif Player1.detect_collision(coin9):
                self.Player1Score += 3
                coin9.xPos = -99
            elif Player1.detect_collision(coin10):
                self.Player1Score += 3
                coin10.xPos = -99
            elif Player1.detect_collision(coin11):
                self.Player1Score += 3
                coin11.xPos = -99
            elif Player1.detect_collision(coin12):
                self.Player1Score += 3
                coin12.xPos = -99
            elif Player1.detect_collision(coin13):
                self.Player1Score += 3
                coin13.xPos = -99
            elif Player1.detect_collision(coin14):
                self.Player1Score += 3
                coin14.xPos = -99
            elif Player1.detect_collision(coin15):
                self.Player1Score += 3
                coin15.xPos = -99
            elif Player1.detect_collision(coin16):
                self.Player1Score += 3
                coin16.xPos = -99
            elif Player1.detect_collision(coin17):
                self.Player1Score += 3
                coin17.xPos = -99
            elif Player1.yPos <= 650 and not flag[0]:

                self.Player1Score += 5
                flag[0] = 1
            elif Player1.yPos <= 481 and not flag[1]:
                self.Player1Score += 5
                flag[1] = 1
            elif Player1.yPos <= 318 and not flag[2]:
                self.Player1Score += 5
                flag[2] = 1
            elif Player1.yPos <= 151 and not flag[3]:
                self.Player1Score += 5
                flag[3] = 1
            elif Player1.yPos <= 765 and not flag[4]:
                self.Player1Score += 10
                flag[4] = 1
            elif Player1.yPos <= 592 and not flag[5]:
                self.Player1Score += 10
                flag[5] = 1
            elif Player1.yPos <= 425 and not flag[6]:
                self.Player1Score += 10
                flag[6] = 1
            elif Player1.yPos <= 262 and not flag[7]:
                self.Player1Score += 10
                flag[7] = 1
            elif Player1.yPos <= 93 and not flag[8]:
                self.Player1Score += 10
                flag[8] = 1
            elif Player1.yPos == 0:
                self.Player1Cross = 1
                break

            if self.timeLimit1 == seconds:
                text = FONT.render(TLE, True, BLACK_COLOR)
                self.game_screen.blit(text, (825, 350))
                pygame.display.update()
                CLOCK.tick(1)
                break
            # Time Limit
            text = FONT1.render(
                TLEFT + str(self.timeLimit1 - math.floor(seconds)),
                True,
                BLACK_COLOR
                )
            self.game_screen.blit(text, (1540, 18))
            text = FONT1.render(
                SCOREMSG + str(math.floor(self.Player1Score)),
                True,
                BLACK_COLOR
                )
            self.game_screen.blit(text, (25, 18))
            pygame.display.update()
            CLOCK.tick(REFRESH_RATE)
        if self.gameOver == 1:
            return
        # Same thing goes on for p2
        # Reinitialising everything back for player 2
        Player1 = player(MOUSE_UP, 880, 900, 36, 40)
        Player2 = player(MOUSE_DOWN, 880, 0, 36, 40)
        enemy1 = shiporRock(
            CAT,
            20,
            594,
            72,
            56,
            S1,
        )
        enemy2 = shiporRock(
            CAT,
            20,
            424,
            72,
            56,
            S2,
        )
        enemy3 = shiporRock(
            FOX,
            20,
            260,
            68,
            55,
            S3,
        )
        enemy4 = shiporRock(
            FOX,
            20,
            766,
            68,
            55,
            S3,
        )
        enemy5 = shiporRock(
            CAT,
            20,
            98,
            68,
            56,
            S2,
        )
        enemy6 = shiporRock(
            FOX,
            560,
            594,
            72,
            56,
            S1,
        )
        enemy7 = shiporRock(
            CAT,
            340,
            424,
            72,
            56,
            S2,
        )
        enemy8 = shiporRock(
            CAT,
            430,
            260,
            68,
            55,
            S3,
        )
        enemy9 = shiporRock(
            CAT,
            700,
            766,
            68,
            55,
            S3,
        )
        enemy10 = shiporRock(
            FOX,
            390,
            98,
            68,
            56,
            S2,
        )
        coin1 = objectGame(COIN_IMG, 1363, 380, 53, 56)
        coin2 = objectGame(COIN_IMG, 1486, 380, 53, 56)
        coin3 = objectGame(COIN_IMG, 1607, 380, 53, 56)
        coin4 = objectGame(COIN_IMG, 1707, 380, 53, 56)
        coin5 = objectGame(COIN_IMG, 1127, 712, 53, 56)
        coin6 = objectGame(COIN_IMG, 2, 480, 53, 56)
        coin7 = objectGame(COIN_IMG, 137, 480, 53, 56)
        coin8 = objectGame(COIN_IMG, 262, 480, 53, 56)
        coin9 = objectGame(COIN_IMG, 382, 480, 53, 56)
        coin10 = objectGame(COIN_IMG, 845, 480, 53, 56)
        coin11 = objectGame(COIN_IMG, 629, 371, 53, 56)
        coin12 = objectGame(COIN_IMG, 1483, 712, 53, 56)
        coin13 = objectGame(COIN_IMG, 1610, 712, 53, 56)
        coin14 = objectGame(COIN_IMG, 1725, 712, 53, 56)
        coin15 = objectGame(COIN_IMG, 10, 200, 53, 56)
        coin16 = objectGame(COIN_IMG, 152, 200, 53, 56)
        coin17 = objectGame(COIN_IMG, 265, 200, 53, 56)
        life1 = objectGame(CRYSTAL, 135, 376, 27, 55)
        life2 = objectGame(CRYSTAL, 1670, 482, 27, 55)
        life3 = objectGame(CRYSTAL, 1663, 151, 27, 55)
        life4 = objectGame(CRYSTAL, 121, 720, 27, 55)
        fence1 = objectGame(FENCE, 0, 535, 482, 54)
        fence2 = objectGame(FENCE, 1329, 546, 482, 54)
        fence3 = objectGame(FENCE, 0, 316, 482, 54)
        fence4 = objectGame(FENCE, 1329, 207, 482, 54)
        fence5 = objectGame(FENCE, 1329, 316, 482, 54)
        fence6 = objectGame(FENCE, 0, 645, 482, 54)
        rock1 = objectGame(ROCKS, 19, 826, 68, 57)
        rock2 = objectGame(ROCKS, 643, 648, 68, 57)
        rock3 = objectGame(ROCKS, 880, 823, 68, 57)
        rock4 = objectGame(ROCKS, 880, 151, 68, 57)
        rock5 = objectGame(ROCKS, 1130, 370, 68, 57)
        bomb1 = objectGame(BOMB, 883, 544, 74, 58)
        bomb2 = objectGame(BOMB, 1147, 206, 74, 58)
        bomb3 = objectGame(BOMB, 648, 715, 74, 58)
        bomb4 = objectGame(BOMB, 1372, 720, 74, 58)
        # Printing again
        background = objectGame(BCKGRND, 0, 0, 1811, 996)
        self.Player1Time = seconds
        self.game_screen.fill((110, 159, 211))
        background.objDraw(self.game_screen)
        Player2.move(direction, self.height, self.width)
        Player2.objDraw(self.game_screen)
        enemy1.move(self.width, '2', self.speedIncrease1,
                    self.speedIncrease2)
        enemy1.objDraw(self.game_screen)
        enemy2.move(self.width, '2', self.speedIncrease1,
                    self.speedIncrease2)
        enemy2.objDraw(self.game_screen)
        enemy3.move(self.width, '2', self.speedIncrease1,
                    self.speedIncrease2)
        enemy3.objDraw(self.game_screen)
        enemy4.move(self.width, '2', self.speedIncrease1,
                    self.speedIncrease2)
        enemy4.objDraw(self.game_screen)
        enemy5.move(self.width, '2', self.speedIncrease1,
                    self.speedIncrease2)
        enemy5.objDraw(self.game_screen)
        enemy6.move(self.width, '2', self.speedIncrease1,
                    self.speedIncrease2)
        enemy6.objDraw(self.game_screen)
        enemy7.move(self.width, '2', self.speedIncrease1,
                    self.speedIncrease2)
        enemy7.objDraw(self.game_screen)
        enemy8.move(self.width, '2', self.speedIncrease1,
                    self.speedIncrease2)
        enemy8.objDraw(self.game_screen)
        enemy9.move(self.width, '2', self.speedIncrease1,
                    self.speedIncrease2)
        enemy9.objDraw(self.game_screen)
        enemy10.move(self.width, '2', self.speedIncrease1,
                     self.speedIncrease2)
        enemy10.objDraw(self.game_screen)
        coin1.objDraw(self.game_screen)
        coin2.objDraw(self.game_screen)
        coin3.objDraw(self.game_screen)
        coin4.objDraw(self.game_screen)
        coin5.objDraw(self.game_screen)
        coin6.objDraw(self.game_screen)
        coin7.objDraw(self.game_screen)
        coin8.objDraw(self.game_screen)
        coin9.objDraw(self.game_screen)
        coin10.objDraw(self.game_screen)
        coin11.objDraw(self.game_screen)
        coin12.objDraw(self.game_screen)
        coin13.objDraw(self.game_screen)
        coin14.objDraw(self.game_screen)
        coin15.objDraw(self.game_screen)
        coin16.objDraw(self.game_screen)
        coin17.objDraw(self.game_screen)
        fence1.objDraw(self.game_screen)
        fence2.objDraw(self.game_screen)
        fence3.objDraw(self.game_screen)
        fence4.objDraw(self.game_screen)
        fence5.objDraw(self.game_screen)
        fence6.objDraw(self.game_screen)
        rock1.objDraw(self.game_screen)
        rock2.objDraw(self.game_screen)
        rock3.objDraw(self.game_screen)
        rock4.objDraw(self.game_screen)
        rock5.objDraw(self.game_screen)
        life1.objDraw(self.game_screen)
        life2.objDraw(self.game_screen)
        life3.objDraw(self.game_screen)
        life4.objDraw(self.game_screen)
        bomb1.objDraw(self.game_screen)
        bomb2.objDraw(self.game_screen)
        bomb3.objDraw(self.game_screen)
        bomb4.objDraw(self.game_screen)
        text = FONT1.render(MSG2, True, BLACK_COLOR)
        self.game_screen.blit(text, (1300, 912))
        text = FONT1.render(MSG1, True, BLACK_COLOR)
        self.game_screen.blit(text, (1300, 14))
        text = FONT.render(PLAYER2, True, BLACK_COLOR)
        Player2.objDraw(self.game_screen)
        self.game_screen.blit(text, (825, 350))
        pygame.display.update()
        CLOCK.tick(1)
        # Game loop for Second Player
        timerStart = pygame.time.get_ticks()
        while not self.gameOver:
            seconds = math.floor((pygame.time.get_ticks() - timerStart) / 1000)
            # loop through events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = '-y'
                    elif event.key == pygame.K_DOWN:
                        direction = '+y'
                    elif event.key == pygame.K_RIGHT:
                        direction = '+x'
                    elif event.key == pygame.K_LEFT:
                        direction = '-x'
                    elif event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_p:
                        timerStart += self.pause()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key \
                        == pygame.K_DOWN or event.key == pygame.K_RIGHT \
                            or event.key == pygame.K_LEFT:
                        direction = 0
            self.game_screen.fill((110, 159, 211))
            background.objDraw(self.game_screen)

            Player2.move(direction, self.height, self.width)
            Player2.objDraw(self.game_screen)
            enemy1.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy1.objDraw(self.game_screen)
            enemy2.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy2.objDraw(self.game_screen)
            enemy3.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy3.objDraw(self.game_screen)
            enemy4.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy4.objDraw(self.game_screen)
            enemy5.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy5.objDraw(self.game_screen)
            enemy6.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy6.objDraw(self.game_screen)
            enemy7.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy7.objDraw(self.game_screen)
            enemy8.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy8.objDraw(self.game_screen)
            enemy9.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy9.objDraw(self.game_screen)
            enemy10.move(self.width, '2', self.speedIncrease1,
                         self.speedIncrease2)
            enemy10.objDraw(self.game_screen)
            coin1.objDraw(self.game_screen)
            coin2.objDraw(self.game_screen)
            coin3.objDraw(self.game_screen)
            coin4.objDraw(self.game_screen)
            coin5.objDraw(self.game_screen)
            coin6.objDraw(self.game_screen)
            coin7.objDraw(self.game_screen)
            coin8.objDraw(self.game_screen)
            coin9.objDraw(self.game_screen)
            coin10.objDraw(self.game_screen)
            coin11.objDraw(self.game_screen)
            coin12.objDraw(self.game_screen)
            coin13.objDraw(self.game_screen)
            coin14.objDraw(self.game_screen)
            coin15.objDraw(self.game_screen)
            coin16.objDraw(self.game_screen)
            coin17.objDraw(self.game_screen)
            fence1.objDraw(self.game_screen)
            fence2.objDraw(self.game_screen)
            fence3.objDraw(self.game_screen)
            fence4.objDraw(self.game_screen)
            fence5.objDraw(self.game_screen)
            fence6.objDraw(self.game_screen)
            rock1.objDraw(self.game_screen)
            rock2.objDraw(self.game_screen)
            rock3.objDraw(self.game_screen)
            rock4.objDraw(self.game_screen)
            rock5.objDraw(self.game_screen)
            life1.objDraw(self.game_screen)
            life2.objDraw(self.game_screen)
            life3.objDraw(self.game_screen)
            life4.objDraw(self.game_screen)
            bomb1.objDraw(self.game_screen)
            bomb2.objDraw(self.game_screen)
            bomb3.objDraw(self.game_screen)
            bomb4.objDraw(self.game_screen)
            text = FONT1.render(MSG2, True, BLACK_COLOR)
            self.game_screen.blit(text, (1300, 912))
            text = FONT1.render(MSG1, True, BLACK_COLOR)
            self.game_screen.blit(text, (1300, 14))
            Player2.objDraw(self.game_screen)
            # Same Implemention of flag array
            if Player2.detect_collision(enemy1):
                break
            elif Player2.detect_collision(enemy2):
                break
            elif Player2.detect_collision(enemy3):
                break
            elif Player2.detect_collision(enemy4):
                break
            elif Player2.detect_collision(enemy5):
                break
            elif Player2.detect_collision(enemy6):
                break
            elif Player2.detect_collision(enemy7):
                break
            elif Player2.detect_collision(enemy8):
                break
            elif Player2.detect_collision(enemy9):
                break
            elif Player2.detect_collision(enemy10):
                break
            elif Player2.detect_collision(rock1):
                break
            elif Player2.detect_collision(rock2):
                break
            elif Player2.detect_collision(rock3):
                break
            elif Player2.detect_collision(rock4):
                break
            elif Player2.detect_collision(rock5):
                break
            elif Player2.detect_collision(bomb1):
                break
            elif Player2.detect_collision(bomb2):
                break
            elif Player2.detect_collision(bomb3):
                break
            elif Player2.detect_collision(bomb4):
                break
            elif Player2.detect_collision(fence1):
                break
            elif Player2.detect_collision(fence2):
                break
            elif Player2.detect_collision(fence3):
                break
            elif Player2.detect_collision(fence4):
                break
            elif Player2.detect_collision(fence5):
                break
            elif Player2.detect_collision(fence6):
                break
            elif Player2.detect_collision(life1):
                seconds -= 10
                life1.xPos = -99
            elif Player2.detect_collision(life2):
                seconds -= 10
                life2.xPos = -99
            elif Player2.detect_collision(life3):
                seconds -= 10
                life3.xPos = -99
            elif Player2.detect_collision(life4):
                seconds -= 10
                life4.xPos = -99
                # Gets extra score for hitting coins
            elif Player2.detect_collision(coin1):
                self.Player2Score += 3
                coin1.xPos = -99
            elif Player1.detect_collision(coin2):
                self.Player1Score += 3
                coin2.xPos = -99
            elif Player2.detect_collision(coin3):
                self.Player2Score += 3
                coin3.xPos = -99
            elif Player2.detect_collision(coin4):
                self.Player2Score += 3
                coin4.xPos = -99
            elif Player2.detect_collision(coin5):
                self.Player2Score += 3
                coin5.xPos = -99
            elif Player2.detect_collision(coin6):
                self.Player2Score += 3
                coin6.xPos = -99
            elif Player2.detect_collision(coin7):
                self.Player2Score += 3
                coin7.xPos = -99
            elif Player2.detect_collision(coin8):
                self.Player2Score += 3
                coin8.xPos = -99
            elif Player2.detect_collision(coin9):
                self.Player2Score += 3
                coin9.xPos = -99
            elif Player2.detect_collision(coin10):
                self.Player2Score += 3
                coin10.xPos = -99
            elif Player2.detect_collision(coin11):
                self.Player2Score += 3
                coin11.xPos = -99
            elif Player2.detect_collision(coin12):
                self.Player2Score += 3
                coin12.xPos = -99
            elif Player2.detect_collision(coin13):
                self.Player2Score += 3
                coin13.xPos = -99
            elif Player2.detect_collision(coin14):
                self.Player2Score += 3
                coin14.xPos = -99
            elif Player2.detect_collision(coin15):
                self.Player2Score += 3
                coin15.xPos = -99
            elif Player2.detect_collision(coin16):
                self.Player2Score += 3
                coin16.xPos = -99
            elif Player2.detect_collision(coin17):
                self.Player2Score += 3
                coin17.xPos = -99
            elif Player2.yPos + Player2.height >= 257 and not flag[9]:
                self.Player2Score += 5
                flag[9] = 1
            elif Player2.yPos + Player2.height >= 418 and not flag[10]:
                self.Player2Score += 5
                flag[10] = 1
            elif Player2.yPos + Player2.height >= 588 and not flag[11]:
                self.Player2Score += 5
                flag[11] = 1
            elif Player2.yPos + Player2.height >= 763 and not flag[12]:
                self.Player2Score += 5
                flag[12] = 1
            elif Player2.yPos + Player2.height >= 822 and not flag[13]:

                self.Player2Score += 10
                flag[13] = 1
            elif Player2.yPos + Player2.height >= 822 and not flag[14]:
                self.Player2Score += 10
                flag[14] = 1
            elif Player2.yPos + Player2.height >= 646 and not flag[15]:
                self.Player2Score += 10
                flag[15] = 1
            elif Player2.yPos + Player2.height >= 477 and not flag[16]:
                self.Player2Score += 10
                flag[16] = 1
            elif Player2.yPos + Player2.height >= 316 and not flag[17]:
                self.Player2Score += 10
                flag[17] = 1
            elif Player2.yPos + Player2.height >= 149 and not flag[18]:
                self.Player2Score += 10
                flag[18] = 1
            elif Player2.yPos == self.height - Player2.height:
                self.Player2Cross = 1
                break

            if self.timeLimit2 == seconds:
                text = FONT.render(TLE, True, BLACK_COLOR)
                self.game_screen.blit(text, (825, 350))
                pygame.display.update()
                CLOCK.tick(1)
                break

            text = FONT1.render(
                TLEFT2 + str(self.timeLimit2 - seconds),
                True,
                BLACK_COLOR
                )
            self.game_screen.blit(text, (1540, 18))
            text = FONT1.render(
                SCOREMSG + str(math.floor(self.Player2Score)),
                True,
                BLACK_COLOR
                )
            self.game_screen.blit(text, (25, 18))
            pygame.display.update()
            CLOCK.tick(REFRESH_RATE)

        self.Player2Time = seconds
        # Checking if Game is over or not
        if self.gameOver:
            self.gameOver = 0
            return
        else:

            self.levelOver = 1
            self.getWinner()
            if self.winner == '1':
                self.speedIncrease1 += 10
            if self.winner == '2':
                self.speedIncrease2 += 10
            self.game_screen.fill((110, 159, 211))
            background.objDraw(self.game_screen)

# Putting everything back in place if game is not over
            Player2.move(direction, self.height, self.width)
            Player2.objDraw(self.game_screen)
            enemy1.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy1.objDraw(self.game_screen)
            enemy2.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy2.objDraw(self.game_screen)
            enemy3.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy3.objDraw(self.game_screen)
            enemy4.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy4.objDraw(self.game_screen)
            enemy5.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy5.objDraw(self.game_screen)
            enemy6.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy6.objDraw(self.game_screen)
            enemy7.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy7.objDraw(self.game_screen)
            enemy8.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy8.objDraw(self.game_screen)
            enemy9.move(self.width, '2', self.speedIncrease1,
                        self.speedIncrease2)
            enemy9.objDraw(self.game_screen)
            enemy10.move(self.width, '2', self.speedIncrease1,
                         self.speedIncrease2)
            enemy10.objDraw(self.game_screen)
            coin1.objDraw(self.game_screen)
            coin2.objDraw(self.game_screen)
            coin3.objDraw(self.game_screen)
            coin4.objDraw(self.game_screen)
            coin5.objDraw(self.game_screen)
            coin6.objDraw(self.game_screen)
            coin7.objDraw(self.game_screen)
            coin8.objDraw(self.game_screen)
            coin9.objDraw(self.game_screen)
            coin10.objDraw(self.game_screen)
            coin11.objDraw(self.game_screen)
            coin12.objDraw(self.game_screen)
            coin13.objDraw(self.game_screen)
            coin14.objDraw(self.game_screen)
            coin15.objDraw(self.game_screen)
            coin16.objDraw(self.game_screen)
            coin17.objDraw(self.game_screen)
            fence1.objDraw(self.game_screen)
            fence2.objDraw(self.game_screen)
            fence3.objDraw(self.game_screen)
            fence4.objDraw(self.game_screen)
            fence5.objDraw(self.game_screen)
            fence6.objDraw(self.game_screen)
            rock1.objDraw(self.game_screen)
            rock2.objDraw(self.game_screen)
            rock3.objDraw(self.game_screen)
            rock4.objDraw(self.game_screen)
            rock5.objDraw(self.game_screen)
            life1.objDraw(self.game_screen)
            life2.objDraw(self.game_screen)
            life3.objDraw(self.game_screen)
            life4.objDraw(self.game_screen)
            bomb1.objDraw(self.game_screen)
            bomb2.objDraw(self.game_screen)
            bomb3.objDraw(self.game_screen)
            bomb4.objDraw(self.game_screen)
            text = FONT1.render(MSG2, True, BLACK_COLOR)
            self.game_screen.blit(text, (1300, 912))
            text = FONT1.render(MSG1, True, BLACK_COLOR)
            self.game_screen.blit(text, (1300, 14))
            Player2.objDraw(self.game_screen)
            self.endlevel()
            self.run_level_loop()
