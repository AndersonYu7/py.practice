from asyncio import events
from distutils.util import change_root
import imp
from turtle import pos
import pygame, sys, time, random
from pygame.locals import *

red = pygame.Color(255, 0 ,0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(150, 150, 150)

def gameover(playsurface):
    gameoverfont = pygame.font.SysFont("Font/msjh.ttc", 72)
    gameoversurf = gameoverfont.render('Game Over', True, grey)
    gameoverrect = gameoversurf.get_rect()
    gameoverrect.midtop = (380, 250)
    playsurface.blit(gameoversurf, gameoverrect)
    pygame.display.flip()
    time.sleep(3)


def main():
    pygame.init()
    fpsclock = pygame.time.Clock()
    playsurface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('snake_410500176_俞博云')


    snake_x = int(random.randint(1,40))*20
    snake_y = int(random.randint(1,30))*20
    snakeposition = [snake_x, snake_y]
    snakesegment = [[snake_x, snake_y], [snake_x, snake_y-20], [snake_x, snake_y-40], [snake_x, snake_y-60]]

    rasberry_x = int(random.randrange(1, 40))*20
    rasberry_y = int(random.randrange(1, 30))*20
    raspberryposition = [rasberry_x, rasberry_y]
    raspberryspawed = 1
    direction = 'down'
    changedirection = direction

    font = pygame.font.SysFont("biome", 50)

    score = 0
    fps = 5
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            
            elif event.type == KEYDOWN:

                if event.key == K_RIGHT or event.key == ord('d'):
                    changedirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changedirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changedirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changedirection = 'down'
                if event.key == K_q:
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
            score += 1
            fps += 2
        else:
            snakesegment.pop()
        
        if raspberryspawed == 0:
            rasberry_x = int(random.randrange(1, 40))*20
            rasberry_y = int(random.randrange(1, 30))*20
            raspberryposition = [rasberry_x, rasberry_y]
            raspberryspawed = 1

        playsurface.fill(black)
        for position in snakesegment:
            pygame.draw.rect(playsurface, white, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playsurface, red, Rect(raspberryposition[0], raspberryposition[1], 20, 20))


        text = font.render("Score : %d" %score, True, blue)
        playsurface.blit(text, (10,10))
        pygame.display.flip()

        if snakeposition[0] > 800 or snakeposition[0] < 0:
            gameover(playsurface)
            playing = False
        elif snakeposition[1] > 600 or snakeposition[1] < 0:
            gameover(playsurface)
            playing = False
        else:
            for snakebody in snakesegment[1:]:
                if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                    gameover(playsurface)
                    playing = False
                    
        fpsclock.tick(fps)
                    
                
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()  






