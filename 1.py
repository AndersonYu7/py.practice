import pygame,sys,time,random
from pygame.locals import *

redColour = pygame.Color(255,0,0)
blackColour = pygame.Color(0,0,0)
whiteColour = pygame.Color(255,255,255)
greyColour = pygame.Color(150,150,150)
playSurface = pygame.display.set_mode((800,600)) 
score = 0
def gameOver(playSurface):
    gameOverFont = pygame.font.SysFont("Fonts/msjh.ttc",72)
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (400, 110)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(50)
    pygame.quit()
    sys.exit()

def Your_Score(score):
    score_font = pygame.font.SysFont("Fonts/msjh.ttc",36)
    value = score_font.render("Score: "+ str(score),True,redColour)
    score_rect = value.get_rect()
    score_rect.midtop = (400,500)
    playSurface.blit(value,score_rect)

def main():
    global score 
    pygame.init()
    fpsClock = pygame.time.Clock() 
    pygame.display.set_caption('Snake_410500077_鍾淳奕')
    x= random.randrange(1,40)
    y= random.randrange(1,30)
    snakePosition = [int (x*20),int (y*20)]
    snakeSegments = [[x,y],[x,y-20],[x,y-40],[x,y-60]]
    a = random.randrange(1,40)
    b = random.randrange(1,30)
    raspberryPosition = [int(a*20),int(b*20)]
    raspberrySpawned = 1
    direction = 'down'
    changeDirection = direction
    playing = True
    while playing :
        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
                Your_Score(score)
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection= 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection= 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection= 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection= 'down'
                if event.key == ord('q'):
                    pygame.event.post(pygame.event.Event(QUIT))
                    
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left'and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up'and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down'and not direction == 'up':
            direction = changeDirection

        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        snakeSegments.insert(0,list(snakePosition))

        if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
            raspberrySpawned = 0
            score += 1
        else:
            snakeSegments.pop()    
        
        
        if raspberrySpawned == 0:
            x= random.randrange(1,40)
            y= random.randrange(1,30)
            raspberryPosition = [int(x*20),int(y*20)]
            raspberrySpawned = 1
        playSurface.fill(blackColour)
        for position in snakeSegments:
            pygame.draw.rect(playSurface,whiteColour,Rect(position[0],position[1],20,20))
            pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1],20,20))
        
        
        if snakePosition[0] > 800 or snakePosition[0] < 0:
            gameOver(playSurface)
        elif snakePosition[1] > 600 or snakePosition[1] < 0:
            gameOver(playSurface)
        else:
            for snakeBody in snakeSegments[1:]:
                if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                    gameOver(playSurface)
        Your_Score(score)
        pygame.display.flip()
        fpsClock.tick(5)
main()        