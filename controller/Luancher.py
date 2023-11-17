from enums import Number

import pygame
from pygame.rect import *
import random


class Launcher:
    def __init__(self):
        # 초기화 관련 코드
        self.setup_game()
        self.setup_score()
        self.setup_obstacles()
        self.setup_benefits()

    def restart():
        global score, isGameOver
        for i in range(len(star)):
            rectStar[i].y = -1
        score = 0
        isGameOver = False

    def setup_game(self):
        # 게임 설정 초기화
        pass

    def setup_score(self):
        # 점수 시스템 초기화
        pass

    def setup_obstacles(self):
        # 장애물 관련 설정 초기화
        pass

    def setup_benefits(self):
        # 베네핏 관련 설정 초기화
        pass

    def start_game(self):
        # 게임 시작 로직
        pass

    def update_game_state(self):
        # 게임 상태 (타이머, 국면 등) 업데이트
        pass

    def eventProcess(move):
        global isActive
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    isActive = False
                if event.key == pygame.K_LEFT:
                    move.x = -1
                if event.key == pygame.K_RIGHT:
                    move.x = 1
                if event.key == pygame.K_r:
                    restart()

    def movePlayer(player, current, move, isGameOver):
        global SCREEN_WIDTH, SCREEN_HEIGHT
        if not isGameOver:
            current.x += move.x


    def handle_player_input(self):
        # 플레이어 입력 처리
        pass

    def update_obstacles(self):
        # 장애물 업데이트
        pass

    def update_benefits(self):
        # 베네핏 업데이트
        pass

    def check_collisions(self):
        # 충돌 감지 및 처리
        pass

    def update_score(self):
        # 점수 업데이트
        pass

    def render_game(self):
        # 게임 렌더링 (그리기)
        pass

    def end_game(self):
        # 게임 종료 로직
        pass
