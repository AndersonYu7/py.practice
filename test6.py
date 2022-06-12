from ast import While
from asyncio.windows_events import NULL
import random
import numpy as np
import pygame
from pygame.locals import QUIT

#====================================初始化並宣告各個變數====================================
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
light_GREY = (230, 230, 230)
dark_GREY = (180, 180, 180)
color_dic = {'R':(255,0,0), 'G':(0,255,0), 'B':(0,0,255), 'Y':(255,255,0), 'P':(204,0,204), 'O':(255,128,0)}

clock = pygame.time.Clock()
#========================================================================================

print("color : red = 'R', green = 'G', blue = 'B', yellow = 'Y', purple = 'P', orange = 'O'")
word = input("color order:")    #使用者輸入顏色並記錄在word

#====================================統計顏色數量並輸出====================================
counter = {'R':0, 'G':0, 'B':0, 'Y':0, 'P':0, 'O':0}
print("-----------------------------------")
for i in range(len(word)):
    counter[word[i]] += 1

for color,value in counter.items():
    if value!=0 :
        print(color,":",value)
print("-----------------------------------")
#=====================================================================


gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("410500176 hw")  #顯示遊戲視窗並檔案名稱為410500176 hw

#===============================球球的初始位置與初始方向(隨機)===============================
ball_x = random.randint(50,700)
ball_y = random.randint(60,500)
direction_y = np.random.choice([1, -1])
direction_x = np.random.choice([1, -1])
font = pygame.font.SysFont("biome", 50) #設定字體為biome 大小為 50
font2 = pygame.font.SysFont("biome", 80) #設定字體為biome 大小為80
#==========================================================================================

#球球動畫主程式
i = 0
j = 0
start = 0
wait = 1
playing = True
while playing:
    for event in pygame.event.get():    #當關閉視窗時 程式停止
        if event.type == pygame.QUIT:
            playing = False

#========================================滑鼠事件:開始畫面========================================
    mouse_press = pygame.mouse.get_pressed()
    if wait == 1:
        gameDisplay.fill(dark_GREY)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if (mouse_x < 340 or mouse_x > 460) or (mouse_y < 250 or mouse_y > 300):
            text2 = font2.render("start", True, color_dic['B'], WHITE)
            gameDisplay.blit(text2, (340,250))

        else:   
            text3 = font2.render("start", True, color_dic['B'], light_GREY)
            gameDisplay.blit(text3, (340,250))

            if mouse_press[0] == 1:
                start = 1
                wait = 0

        pygame.display.update()
#=============================================================================================

#=======================================動畫開始:球球反彈=======================================
    if start == 1:
        ball_y += 10 * direction_y
        ball_x += 5 * direction_x

        if ball_y - 25 <= 0 or ball_y + 60 >= 600:  #如果球球到達邊界 方向改變
            direction_y *= -1
            
        elif ball_x + 100 >= 800 or ball_x -5 <= 0:
            direction_x *= -1

        gameDisplay.fill(WHITE) #遊戲視窗白色


        if i>10:    #讓顏色重複跑10次後才改變顏色
            i=0
            j+=1

        if j == len(word) :
            j = 0

        text = font.render("Press the ESC to end", True, color_dic['B'], WHITE)
        gameDisplay.blit(text, (250,10))

        pygame.draw.ellipse(gameDisplay, color_dic[word[j]], [ball_x, ball_y, 100, 60], 0)
        pygame.display.update()
        clock.tick(60)
        i += 1

    keys_pressed = pygame.key.get_pressed() #鍵盤事件:當按下esc鍵 程式停止
    if keys_pressed[pygame.K_ESCAPE]==1:
        playing = False
#=============================================================================================
        
pygame.quit()
quit()

