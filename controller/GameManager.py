import pygame
from pygame.rect import *

from model.Launcher import Launcher


def play():
    newGame = Launcher()
    newGame.screen()

    while newGame.isActive:
        newGame.SCREEN.fill((0, 0, 0))  # 화면 지우기
        newGame.SCREEN.blit(newGame.background, (0, 0))  # 배경 렌더링
        newGame.update_player_animation()
        newGame.eventProcess()
        newGame.updatePlayerPosition()
        newGame.makeProsCons()
        newGame.moveProsCons()

        for idx, rect in enumerate(newGame.pros):
            scaled_image = pygame.transform.scale(newGame.pros_images[idx % len(newGame.cons_images)],
                                                  (rect.width, rect.height))
            newGame.SCREEN.blit(scaled_image, rect)
        for idx, rect in enumerate(newGame.cons):
            scaled_image = pygame.transform.scale(newGame.cons_images[idx % len(newGame.cons_images)],
                                                  (rect.width, rect.height))
            newGame.SCREEN.blit(scaled_image, rect)

        newGame.checkCollision()
        newGame.setText(newGame.timeUpdate4sec())

        newGame.SCREEN.blit(newGame.player, newGame.rectPlayer)  # 플레이어 렌더링
        pygame.display.flip()
        newGame.clock.tick(60)
