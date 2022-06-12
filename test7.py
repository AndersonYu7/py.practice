from math import pi
from random import randint
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
points = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type == pygame.KEYDOWN:
        # 按任意鍵可清屏，並把點恢復到原始狀態
        points = []
        pygame.srceen.fill((255, 255, 255))      # 用白色填充視窗背景
    if event.type == pygame.MOUSEBUTTONDOWN:	# 滑鼠按下
        screen.fill((255, 255, 255))
        # 畫隨機矩形
        rc = (255, 0, 0)	# 紅色
        rp = (randint(0, 639), randint(0, 479))
        rs = (639 - randint(rp[0], 639), 479 - randint(rp[1], 479))
        pygame.draw.rect(screen, rc, pygame.Rect(rp, rs))
        # 畫隨機圓形
        rc = (0, 255, 0)	# 綠色
        rp = (randint(0, 639), randint(0, 479))
        rr = randint(1, 200)
        pygame.draw.circle(screen, rc, rp, rr)
        # 獲取當前滑鼠單擊位置
        x, y = pygame.mouse.get_pos()
        points.append((x, y))
        # 根據單擊位置畫弧線
        angle = (x / 639) * pi * 2
        pygame.draw.arc(screen, (0, 0, 0), (0, 0, 639, 479), 0, angle, 3)
        # 根據單擊位置畫橢圓
        pygame.draw.ellipse(screen, (0, 255, 0), (0, 0, x, y))
        # 從左上和右下畫兩根連線到單擊位置
        pygame.draw.line(screen, (0, 0, 255), (0, 0), (x, y))
        pygame.draw.line(screen, (255, 0, 0), (640, 480), (x, y))
        # 畫單擊軌跡圖
        if len(points) > 1:
            pygame.draw.lines(screen, (155, 155, 0), points, False, 2)
        # 把滑鼠單擊的每個點畫明顯點
        for p in points:
            pygame.draw.circle(screen, (155, 155, 155), p, 3)
    pygame.display.update()