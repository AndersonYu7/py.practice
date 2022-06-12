import pygame
import random
import numpy as np

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Rebound")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

ball_x = random.randint(30,775)
ball_y = random.randint(30,575)
direction_y = np.random.choice([1, -1])
direction_x = np.random.choice([1, -1])

clock = pygame.time.Clock()

i = 0
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    ball_y += 10 * direction_y
    ball_x += 5 * direction_x

    if ball_y - 25 <= 0 :
        direction_y *= -1

    elif ball_y + 25 >= 600:
        direction_y *= -1
        
    elif ball_x + 25 >= 800:
        direction_x *= -1
    
    elif ball_x - 25 <= 0:
        direction_x *= -1

    gameDisplay.fill(WHITE)

    pygame.draw.circle(gameDisplay, GREEN, (ball_x, ball_y), 25)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()
