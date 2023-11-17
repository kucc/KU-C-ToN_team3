import pygame
from pygame.rect import *

from model.Launcher import Launcher


def play():
    newGame = Launcher()
    newGame.screen()
    newGame.player()
    newGame.obstacle()

    while newGame.isActive:
        # 1. 화면 검정색으로 지우기
        newGame.SCREEN.fill((0, 0, 0))
        # 2. 이번트처리
        newGame.eventProcess(newGame.move)
        # 3. 플레이어
        newGame.movePlayer(newGame.player, newGame.rectPlayer, newGame.move)
        # 4. 유성만들기
        newGame.makeStar(newGame.rectStar)
        newGame.moveStar(newGame.star, newGame.rectStar)
        # 5. 충돌
        newGame.CheckCollision(newGame.rectPlayer, newGame.rectStar)
        # 6. Text 업데이트
        newGame.setText(newGame.timeUpdate4sec())
        # 7.화면업데이트
        pygame.display.flip()
        newGame.clock.tick(100)