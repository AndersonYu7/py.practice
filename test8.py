from asyncio import events
from distutils.util import change_root
import imp
from turtle import pos
import pygame, sys, time, random
from pygame.locals import *

red = pygame.Color(255, 0 ,0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(150, 150, 150)

def gameover(playsurface):
    gameoverfont = pygame.font.SysFont("Font/msjh.ttc", 72)
    gameoversurf = gameoverfont.render('Game Over', True, grey)
    gameoverrect = gameoversurf.get_rect()
    gameoverrect.midtop = (320, 10)
    playsurface.blit(gameoversurf, gameoverrect)
    pygame.display.flip()
    time.sleep(500)
    pygame.quit()
    sys.exit

def main():
    pygame.init()
    fpsclock = pygame.time.Clock()
    playsurface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Raspberry Snake')

    snakeposition = [100, 100]
    snakesegment = [[100, 100], [80, 100], [60, 100]]
    raspberryposition = [300, 300]
    raspberryspawed = 1
    direction = 'right'
    changedirection = direction


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            keys_pressed = pygame.key.get_pressed() 
            if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
                changedirection = 'right'
            if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
                changedirection = 'left'
            if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
                changedirection = 'up'
            if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
                changedirection = 'down'
            if keys_pressed[pygame.K_ESCAPE]:
                pygame.event.post(pygame.event.Event(QUIT))

            
            if changedirection == 'right' and not direction == 'left':
                direction = changedirection
            if changedirection == 'left' and not direction == 'right':
                direction = changedirection
            if changedirection == 'up' and not direction == 'down':
                direction = changedirection
            if changedirection == 'down' and not direction == 'up':
                direction = changedirection

            
            if direction == 'right':
                snakeposition[0] += 20
            if direction == 'left':
                snakeposition[0] -= 20
            if direction == 'up':
                snakeposition[1] -= 20
            if direction == 'down':
                snakeposition[1] += 20

            snakesegment.insert(0, list(snakeposition))

            if snakeposition[0] == raspberryposition[0] and snakeposition[1] == raspberryposition[1]:
                raspberryspawed = 0
            else:
                snakesegment.pop()
            
            if raspberryspawed == 0:
                x = random.randrange(1, 32)
                y = random.randrange(1, 24)
                raspberryposition = [int(x*20), int(y*20)]
                raspberryspawed = 1

            playsurface.fill(black)
            for position in snakesegment:
                pygame.draw.rect(playsurface, white, Rect(position[0], position[1], 20, 20))
                pygame.draw.rect(playsurface, red, Rect(raspberryposition[0], raspberryposition[1], 20, 20))

            pygame.display.flip()

            if snakeposition[0] > 620 or snakeposition[0] < 0:
                gameover(playsurface)
            elif snakeposition[1] > 460 or snakeposition[1] < 0:
                gameover(playsurface)
            else:
                for snakebody in snakesegment[1:]:
                    if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                        gameover(playsurface)

            pygame.display.update()
            fpsclock.tick(5)
                

if __name__ == '__main__':
    main()  
            







