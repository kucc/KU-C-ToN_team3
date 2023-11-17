import pygame
from pygame.rect import *
import random

def play():
    ##1. 변수 선언
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    score = 0
    isActive = True
    isGameOver = False
    move = Rect(0, 0, 0, 0)
    time500ms = 0
    time4Sec = 0
    time4SecToggle = False
    #########################################################
    ##2. 스크린
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("CodingNow!!")
    #########################################################
    ##3. player
    player = pygame.image.load("Player.png")
    player = pygame.transform.scale(player, (20, 30))
    rectPlayer = player.get_rect()
    rectPlayer.centerx = (SCREEN_WIDTH / 2)
    rectPlayer.centery = (SCREEN_HEIGHT / 2)
    #########################################################
    ##4. 유성
    star = [pygame.image.load("star.png") for i in range(20)]
    rectStar = [None for i in range(len(star))]
    for i in range(len(star)):
        star[i] = pygame.transform.scale(star[i], (20, 20))
        rectStar[i] = star[i].get_rect()
        rectStar[i].y = -1
    #########################################################
    ##5. time
    clock = pygame.time.Clock()

    while isActive:
        # 1. 화면 검정색으로 지우기
        SCREEN.fill((0, 0, 0))
        # 2. 이번트처리
        eventProcess(move)
        # 3. 플레이어
        movePlayer(player, rectPlayer, move, isGameOver)
        # 4. 유성만들기
        makeStar(rectStar)
        moveStar(star, rectStar, isGameOver)
        # 5. 충돌
        CheckCollision(rectPlayer, rectStar)
        # 6. Text 업데이트
        setText(timeUpdate4sec(isGameOver))
        # 7.화면업데이트
        pygame.display.flip()
        clock.tick(100)