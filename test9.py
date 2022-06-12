import pygame, sys, time, random
from pygame.locals import *

red = pygame.Color(255, 0 ,0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
orange = pygame.Color(255, 128, 0)
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

def pause_dis(playsurface):
    pausefont = pygame.font.SysFont("Font/msjh.ttc", 72)
    pausesurf = pausefont.render('Pause', True, blue)
    pauserect = pausesurf.get_rect()
    pauserect.midtop = (380, 250)
    playsurface.blit(pausesurf, pauserect)
    pygame.display.flip()


def main():
    pygame.init()
    pygame.mixer.init()
    fpsclock = pygame.time.Clock()
    playsurface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('snake_410500176_俞博云')

    path = "./TKU/L11_pygame/snake_music.mp3"
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    block_x = int(random.randint(1,740//80))*80
    block_y = int(random.randint(1,540//60))*60

    snake_x = int(random.randint(1,40))*20
    snake_y = int(random.randint(1,30))*20
    while (snake_x >= block_x and snake_x < block_x + 80) or \
    (snake_x <= 0 or snake_x >= 800):
        snake_x = int(random.randint(1,40))*20
    while (snake_y >= block_y and snake_y < block_y + 60) or \
    (snake_y <=0 or snake_y >= 600):
        snake_y = int(random.randint(1,30))*20
    snakeposition = [snake_x, snake_y]
    snakesegment = [[snake_x, snake_y], [snake_x, snake_y-20], [snake_x, snake_y-40], [snake_x, snake_y-60]]

    rasberry_x = int(random.randrange(1, 40))*20
    rasberry_y = int(random.randrange(1, 30))*20
    while (rasberry_x >= block_x and rasberry_x < block_x + 80) or (rasberry_x > 0 and rasberry_x < 200):
        rasberry_x = int(random.randrange(1, 40))*20
    while (rasberry_y >= block_y and rasberry_y < block_y + 60) or (rasberry_y > 0 and rasberry_y < 60):
        rasberry_y = int(random.randrange(1, 30))*20
    
    raspberryposition = [rasberry_x, rasberry_y]
    raspberryspawed = 1
    direction = 'down'
    changedirection = direction

    font = pygame.font.SysFont("biome", 50)

    score = 0
    fps = 5
    playing = True
    pause = False
    state = True
    while playing:
        while pause and state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False
                    playing = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pause = False
                        pygame.mixer.music.unpause()
                    if event.key == K_q:
                        state = False
                        playing = False
            
            playsurface.fill(white)
            pause_dis(playsurface)
            pygame.display.flip() 
            
        while not pause and state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = False
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
                        state = False
                        playing = False
                    if event.key == K_SPACE:
                        pause = True
                        pygame.mixer.music.pause()

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
                if snakeposition[0] == 800:
                    snakeposition[0] = 0
            if direction == 'left':
                snakeposition[0] -= 20
                if snakeposition[0] == -20:
                    snakeposition[0] = 780
            if direction == 'up':
                snakeposition[1] -= 20
                if snakeposition[1] == -20:
                    snakeposition[1] = 580
            if direction == 'down':
                snakeposition[1] += 20
                if snakeposition[1] == 600:
                    snakeposition[1] = 0

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
                while (rasberry_x >= block_x and rasberry_x < block_x + 80) or (rasberry_x > 0 and rasberry_x < 200):
                    rasberry_x = int(random.randrange(1, 40))*20
                while (rasberry_y >= block_y and rasberry_y < block_y + 60) or (rasberry_y > 0 and rasberry_y < 60):
                    rasberry_y = int(random.randrange(1, 30))*20
                raspberryposition = [rasberry_x, rasberry_y]
                raspberryspawed = 1

            playsurface.fill(black)
            for position in snakesegment:
                pygame.draw.rect(playsurface, white, Rect(position[0], position[1], 20, 20))
                pygame.draw.rect(playsurface, red, Rect(raspberryposition[0], raspberryposition[1], 20, 20))
            
            pygame.draw.rect(playsurface, green, Rect(block_x, block_y, 80, 60))

            text = font.render("Score : %d" %score, True, blue)
            playsurface.blit(text, (10,10))
            
            #當撞到綠色方塊或撞到身體 遊戲結束
            if (snakeposition[0] >= block_x and snakeposition[0] < block_x + 80) \
            and (snakeposition[1] >= block_y and snakeposition[1] < block_y + 60):
                gameover(playsurface)
                state = False
                playing = False
            else:
                for snakebody in snakesegment[1:]:
                    if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                        gameover(playsurface)
                        state = False
                        playing = False

            pygame.display.flip()            
            fpsclock.tick(fps)
                    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()  






