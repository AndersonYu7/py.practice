import pygame
from pygame.locals import QUIT
pygame.init()
color_dic = {'R':(255,0,0),'G':(0,255,0),'B':(0,0,255),'Y':(255,255,0),'P':(204,0,204),'O':(255,128,0)}
x=10
y=0
WHITE = (255,255,255)
Enter = input("color order:")

print("============= 統計 ===============")
for k in range(len(Enter)):
    counter = Enter.count(Enter[k])
    id=0
    if k==0:
        print(f"{Enter[k]}: {counter}")
    else:
        for j in range(k):
            if(Enter[k]==Enter[j]):
                id+=1
        if id==0:
           print(f"{Enter[k]}: {counter}") 
print("==================================")

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
gameDisplay= pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
font = pygame.font.SysFont("simhei", 50)
font0 = pygame.font.SysFont("simhei", 30)
pygame.display.set_caption("410500218 GAME")
clock= pygame.time.Clock()


i=0
running = True
while running: 
    for event in pygame.event.get(): 
        if event.type== QUIT: 
            running = False
            pygame.quit()

    if y >= DISPLAY_HEIGHT:
        y=0
    else:
        y=y+30  
    if i == len(Enter):
        i=0      
    gameDisplay.fill(WHITE)

    text0 = font0.render("Press the SPACE (keyboard event)", True, (0,0,255), (255,255,255))
    gameDisplay.blit(text0, (300,10))

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        text = font.render("Made by 410500218", True, (255,128,0), (255,255,255))
        gameDisplay.blit(text, (320,240))
    
    pygame.draw.ellipse(gameDisplay,color_dic[Enter[i]],[x, y, 100, 60], 0) #線寬0為實心
    pygame.display.update()
    clock.tick(3)
    i+=1

pygame.quit
quit()
