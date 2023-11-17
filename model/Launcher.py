from ..enums.Number import Number

import pygame
from pygame.rect import *
import random


class Luancher:
    def __init__(self):

        self.score = 0
        self.isActive = True
        self.isGameOver = False
        self.move = Rect(0, 0, 0, 0)
        self.time500ms = 0
        self.time4Sec = 0
        self.time4SecToggle = False
        self.clock = pygame.time.Clock()


    def screen(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((Number.SCREEN_WIDTH.getValue(),Number.SCREEN_HEIGHT.getValue()))
        pygame.display.set_caption("교수님을 피해라!!!")

    def player(self):
        self.player = pygame.image.load("/utils/player/run1.png")
        self.player = pygame.transform.scale(self.player, (20, 30))
        self.rectPlayer = self.player.get_rect()
        self.rectPlayer.centerx = (Number.SCREEN_WIDTH.getValue() / 2)
        self.rectPlayer.centery = (Number.SCREEN_HEIGHT.getValue() / 2)

    def obstacle(self):
        self.star = [pygame.image.load("/utils/.png") for i in range(20)]
        self.rectStar = [None for i in range(len(self.star))]
        for i in range(len(self.star)):
            self.star[i] = pygame.transform.scale(self.star[i], (20, 20))
            self.rectStar[i] = self.star[i].get_rect()
            self.rectStar[i].y = -1

    def restart(self):
        for i in range(len(self.star)):
            self.rectStar[i].y = -1
        self.score = 0
        self.isGameOver = False

    def eventProcess(self, move):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    self.isActive = False
                if event.key == pygame.K_LEFT:
                    move.x = -1
                if event.key == pygame.K_RIGHT:
                    move.x = 1
                if event.key == pygame.K_UP:
                    move.y = -1
                if event.key == pygame.K_DOWN:
                    move.y = 1
                if event.key == pygame.K_r:
                    self.restart()

    #########################################################
    def movePlayer(self, player, current, move):
        if not self.isGameOver:
            current.x += move.x
            current.y += move.y
        #### limit
        if current.y > Number.SCREEN_HEIGHT.getValue() - current.height:
            current.y = Number.SCREEN_HEIGHT.getValue() - current.height
        if current.x > Number.SCREEN_WIDTH.getValue() - current.width:
            current.x = Number.SCREEN_WIDTH.getValue() - current.width
        if current.y < 0:
            current.y = 0
        if current.x < 0:
            current.x = 0
        self.SCREEN.blit(player, current)

    #########################################################
    def timeUpdate50ms(self):
        self.time500ms += 1
        if self.time500ms > 5:
            self.time500ms = 0
            return True
        return False

    def makeStar(self, rec):
        if self.timeUpdate50ms():
            idex = random.randint(0, len(self.star) - 1)
            if rec[idex].y == -1:
                rec[idex].x = random.randint(0, Number.SCREEN_WIDTH.getValue())
                rec[idex].y = 0

    def moveStar(self, star, current):
        for i in range(len(star)):
            if current[i].y == -1:
                continue
            if not self.isGameOver:
                current[i].y += 1
            if current[i].y > Number.SCREEN_HEIGHT.getValue():
                current[i].y = -1
            self.SCREEN.blit(star[i], current[i])

    #########################################################
    def CheckCollision(self, player, star):
        if self.isGameOver:
            return
        for rec in star:
            if rec.top < player.bottom \
                    and player.top < rec.bottom \
                    and rec.left < (player.right - 8) \
                    and (player.left + 8) < rec.right:
                self.isGameOver = True
                break
        self.score += 1

    #########################################################
    def timeUpdate4sec(self):
        if not self.isGameOver:
            return False
        self.time4Sec += 1
        if self.time4Sec > 40:
            self.time4Sec = 0
            self.time4SecToggle = (~self.time4SecToggle)
        return self.time4SecToggle

    def setText(self, isupdate=False):

        myFont = pygame.font.SysFont("arial", 20, True, False)

        self.SCREEN.blit(myFont.render(
            f'score : {self.score}', True, 'green'), (10, 10, 0, 0))

        if isupdate:
            self.SCREEN.blit(myFont.render(
                f'Game Over!!', True, 'red'), (150, 300, 0, 0))
            self.SCREEN.blit(myFont.render(
                f'press R - Restart', True, 'red'), (140, 320, 0, 0))
    #########################################################
    #########################################################
