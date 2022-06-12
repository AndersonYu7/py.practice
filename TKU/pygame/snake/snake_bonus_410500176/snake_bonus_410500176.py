#snake_bonus_410500176
# [O] 新增背景音樂 83
# [O] 在畫面隨機位置生成3*4方塊的的綠色障礙物，並一直固定此位置直到遊戲結束 86
# [O] 樹梅不會生成在綠色障礙物的位置內 90
# [O] 貪食蛇可以穿牆不會死亡，只有撞到自己&撞到障礙物會死亡 95
# [O] 按下空白鍵，暫停遊戲 100


import pygame, sys, random,time
from pygame.locals import *

red = pygame.Color(255, 0 ,0)
blue = pygame.Color(0, 0, 255)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(150, 150, 150)
light_grey = pygame.Color(220, 221, 216)

class Button:
	def __init__(self,text,width,height,pos,elevation):
		
		self.start = True       
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

		 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = (71, 95, 119)

		 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = (53, 75, 94)
		
		self.text_surf = pygame.font.SysFont("comicsansms", 30).render(text,True,white)
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self, playsurface):
		 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(playsurface,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(playsurface,self.top_color, self.top_rect,border_radius = 12)
		playsurface.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = (215, 75, 75)
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					self.start = False
					self.pressed = False
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = (71, 95, 119)

def Words_display(playsurface,text , size, font, color, midtop_pos):
    wordsfont = pygame.font.SysFont(font, size)
    wordssurf = wordsfont.render(text, True, color)
    wordsrect = wordssurf.get_rect()
    wordsrect.midtop = midtop_pos
    playsurface.blit(wordssurf, wordsrect)

def score_dis(score, playsurface):

    font = pygame.font.SysFont("comicsansms", 35)
    text = font.render("Score : %d" %score, True, blue)
    playsurface.blit(text, (10,10))

path = 0
def sound_image_dis(playsurface):
    picture_path = [".\TKU\pygame\snake\snake_bonus_410500176\picture\MAX.png",".\TKU\pygame\snake\snake_bonus_410500176\picture\MAX_white.png",".\TKU\pygame\snake\snake_bonus_410500176\picture\\none.png",".\TKU\pygame\snake\snake_bonus_410500176\picture\\none_white.png"] 
    image = pygame.image.load(".\TKU\pygame\snake\snake_bonus_410500176\picture\MAX.png")   #生成圖片 
    image.convert()
    imagerect = image.get_rect()
    imagerect = (700, 500)
    playsurface.blit(image, imagerect)
    global path

    #當滑鼠在聲音圖片區域 按下時 靜音或音量50%
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] >= imagerect[0] and mouse_pos[0] <= imagerect[0]+90 and \
    mouse_pos[1] >= imagerect[1] and mouse_pos[1] <= imagerect[1] + 90:
        if pygame.mouse.get_pressed()[0] and path == 0:
            pygame.mixer.music.set_volume(0)
            path = 2
            time.sleep(0.1)
        elif pygame.mouse.get_pressed()[0] and path == 2:
            pygame.mixer.music.set_volume(0.5)
            path = 0
            time.sleep(0.1)

        playsurface.fill(light_grey)
        image = pygame.image.load(picture_path[path+1])
        image.convert() #讓程式在加載完圖片後 提高性能
        playsurface.blit(image, imagerect)
        
    else:
        playsurface.fill(light_grey)
        image = pygame.image.load(picture_path[path])
        image.convert() #讓程式在加載完圖片後 提高性能
        playsurface.blit(image, imagerect)
        

def main():
    pygame.init()
    pygame.mixer.init()
    fpsclock = pygame.time.Clock()
    playsurface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('snake_410500176_俞博云')
    pygame.mixer.music.load(".\TKU\pygame\snake\snake_bonus_410500176\music\snake_music.mp3")
    pygame.mixer.music.play(-1)

    global path
    if path != 2:
        pygame.mixer.music.set_volume(0.5)

    block_x = int(random.randint(1,740//80))*80     #防止綠色方塊生成區域超出800*600的範圍
    block_y = int(random.randint(1,540//60))*60

    snake_x = int(random.randint(1,40))*20      #初始化蛇的座標 如果會生在綠色方塊 則重新初始化
    snake_y = int(random.randint(1,30))*20
    while (snake_x >= block_x and snake_x < block_x + 80) or \
    (snake_x <= 0 or snake_x >= 800):
        snake_x = int(random.randint(1,40))*20
    while (snake_y >= block_y and snake_y < block_y + 60) or \
    (snake_y <=0 or snake_y >= 600):
        snake_y = int(random.randint(1,30))*20
    snakeposition = [snake_x, snake_y]
    snakesegment = [[snake_x, snake_y], [snake_x, snake_y-20], [snake_x, snake_y-40], [snake_x, snake_y-60]]

    rasberry_x = int(random.randrange(1, 40))*20    #初始化莓果座標 如果會生在綠色方塊 則重新初始化
    rasberry_y = int(random.randrange(1, 30))*20
    while (rasberry_x >= block_x and rasberry_x < block_x + 80) or (rasberry_x > 0 and rasberry_x < 200):
        rasberry_x = int(random.randrange(1, 40))*20
    while (rasberry_y >= block_y and rasberry_y < block_y + 60) or (rasberry_y > 0 and rasberry_y < 60):
        rasberry_y = int(random.randrange(1, 30))*20
    raspberryposition = [rasberry_x, rasberry_y]
    raspberryspawed = 1

    direction = 'down'  #設定起始方向為下
    changedirection = direction

    start_button = Button('start',200,40,(300,350),5)
    exit_button = Button('exit',200,40,(300,450),5)
    home_button = Button('home',200,40,(300,350),5)
    pause_home_button = Button('home',200,40,(300,450),5)
    continue_button = Button('continue',200,40,(300,350),5)

    game_faps = 15
    display_faps = 60

    pygame.mixer.music.pause()
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #當視窗關閉 退出遊戲
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:     
                if event.key == K_q:        #當按下q鍵 退出遊戲
                    pygame.quit()
                    sys.exit()

        playsurface.fill(light_grey)
        image = pygame.image.load(".\TKU\pygame\snake\snake_bonus_410500176\picture\snaketitle.png")   #生成圖片
        image.convert() #讓程式在加載完圖片後 提高性能
        imagerect = image.get_rect()
        imagerect.midtop = (400, 50)

        sound_image_dis(playsurface)
        playsurface.blit(image, imagerect)

        start_button.draw(playsurface)
        exit_button.draw(playsurface)

        if start_button.start == False:     #當開始紐被按下時 開始遊戲(停止開始畫面迴圈)
            start = False

        if exit_button.start == False:      #當結束紐被按下時 結束遊戲
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        fpsclock.tick(display_faps)

    score = 0
    playing = True
    state = True
    pause = False
    while playing:
        while pause and state:      #暫停畫面
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #當關閉視窗 退出遊戲
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:    #當按下空白鍵 繼續遊戲
                        pause = False

                    if event.key == K_q:        #當按下q鍵 退出遊戲
                        pygame.quit()
                        sys.exit()
            
            playsurface.fill(light_grey)
            sound_image_dis(playsurface)
            Words_display(playsurface, 'Pause', 100, 'comicsansms', grey, (400, 80))

            continue_button.draw(playsurface)
            pause_home_button.draw(playsurface)

            if continue_button.start == False:  #當繼續紐被按下時 繼續遊戲
                pause = False
                continue_button.start = True

            if pause_home_button.start == False:   #按鈕按下 回到主頁面
                state = False
                playing = False
                main()

            pygame.display.flip()
            fpsclock.tick(display_faps) 
            
            
        while not pause and state:     #遊戲期間
            pygame.mixer.music.unpause()    #繼續播放音樂
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #當關閉視窗 退出遊戲
                    pygame.quit()
                    sys.exit()
                
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT or event.key == ord('d'):   #方向鍵以及wasd 控制上下左右
                        changedirection = 'right'
                    if event.key == K_LEFT or event.key == ord('a'):
                        changedirection = 'left'
                    if event.key == K_UP or event.key == ord('w'):
                        changedirection = 'up'
                    if event.key == K_DOWN or event.key == ord('s'):
                        changedirection = 'down'

                    if event.key == K_q:    #當按下q鍵 退出遊戲
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE:    #當按下空白鍵 暫停遊戲且暫停音樂
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

            if snakeposition[0] == raspberryposition[0] and snakeposition[1] == raspberryposition[1]:   #當莓果被吃時 重新刷新莓果位置及加一分
                raspberryspawed = 0
                score += 1
            else:
                snakesegment.pop() #堆疊概念(先進後出) 尾巴每行走一格需pop一格
            
            if raspberryspawed == 0:    #刷新莓果座標
                rasberry_x = int(random.randrange(1, 40))*20
                rasberry_y = int(random.randrange(1, 30))*20
                while (rasberry_x >= block_x and rasberry_x < block_x + 80) or (rasberry_x > 0 and rasberry_x < 200):
                    rasberry_x = int(random.randrange(1, 40))*20
                while (rasberry_y >= block_y and rasberry_y < block_y + 60) or (rasberry_y > 0 and rasberry_y < 60):
                    rasberry_y = int(random.randrange(1, 30))*20
                raspberryposition = [rasberry_x, rasberry_y]
                raspberryspawed = 1

            playsurface.fill(black)
            for position in snakesegment:   #繪圖 snake, rasberry, green block and score_text
                pygame.draw.rect(playsurface, white, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playsurface, red, Rect(raspberryposition[0], raspberryposition[1], 20, 20))
            
            pygame.draw.rect(playsurface, green, Rect(block_x, block_y, 80, 60))
            score_dis(score, playsurface)

            #當撞到綠色方塊或撞到身體 遊戲結束
            if (snakeposition[0] >= block_x and snakeposition[0] < block_x + 80) \
            and (snakeposition[1] >= block_y and snakeposition[1] < block_y + 60):
                playing = False
                state = False
            else:
                for snakebody in snakesegment[1:]:
                    if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                        playing = False
                        state = False

            pygame.display.flip()            
            fpsclock.tick(game_faps)

    isgameover = True
    while isgameover:   #最終畫面
        pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #當關閉視窗 退出遊戲
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:        #當按下q鍵 退出遊戲
                    pygame.quit()
                    sys.exit()

        playsurface.fill(light_grey)
        Words_display(playsurface, 'Game Over', 100, 'comicsansms', grey, (400, 80))
        Words_display(playsurface, 'score : %d'%score, 30, 'comicsansms', blue, (400,220))

        home_button.draw(playsurface)
        exit_button.draw(playsurface)

        if home_button.start == False:  #按鈕按下 回到主頁面
            isgameover = False
            main()

        if exit_button.start == False:  #按鈕按下 退出遊戲
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        fpsclock.tick(display_faps)   

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()  






