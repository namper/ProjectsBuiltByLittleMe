import pygame,sys,random
from pygame.locals import*
from selenium import webdriver

pygame.init()
pygame.mixer.init()
#Coding below










#Atributes
WHITE = (211,211,211)
BLACK = (0,0,0)

BLUE = (0, 102, 150)
LIGHTBLUE = (2, 147, 214)
w = 800;h = 400


#initilizing
root=pygame.display.set_mode((w,h))
rootrect=root.get_rect()
pygame.display.set_caption('Air Glow Hokey')


#message display
def text_objects(text, font):
	textSurface = font.render(text, True, WHITE)
	return textSurface, textSurface.get_rect()

def message_display(text,x,y):
	largeText = pygame.font.Font('freesansbold.ttf',50)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = (x,y)
	root.blit(TextSurf, TextRect)

def credit():
	driver = webdriver.Chrome("C:\\Users\\user\Desktop\\glowhokey\\chromedriver.exe")
	driver.set_page_load_timeout(30)
	driver.get('https://www.instagram.com/mishikookropiridze/')
	driver.maximize_window()
	driver.implicitly_wait(20)
#menue 
def menue():
	#atributes
	menueimg = pygame.image.load('menue.png').convert()
	logo = pygame.image.load('logo.png').convert_alpha()
	color = BLUE

	color1 = BLUE

	color2 = BLUE
	menueactive=True
	while menueactive:
		#mouse trick
		mouse=pygame.mouse.get_pos()
		m = pygame.draw.rect(root,BLACK,(mouse[0],mouse[1],100,100))
		#background
		root.blit(menueimg,(0,0))
		root.blit(logo,(300,50))
		#object
		r1 = pygame.draw.rect(root,color,(60,200,200,80))
		r3 = pygame.draw.rect(root,color2,(550,200,200,80))
		r2 = pygame.draw.rect(root,color1,(307,200,200,80))

		#Text Display
		message_display('START',155,240)
		message_display('CREDIT',406,240)
		message_display('EXIT',650,240)

		# event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if m.colliderect(r1):
				color = LIGHTBLUE
				if pygame.mouse.get_pressed()[0] == 1 :
					menueactive = False
			else:
				color = BLUE
			if m.colliderect(r2):
				color1 = LIGHTBLUE
				if pygame.mouse.get_pressed()[0] == 1 :
					credit()				
			else:
				color1 = BLUE 
			if m.colliderect(r3):
				color2 = LIGHTBLUE
				if pygame.mouse.get_pressed()[0] == 1 :
					pygame.quit()
					sys.exit()
			else:
				color2 = BLUE

		pygame.display.update()


#Pause
def paused():
	#atributes
	pausedimg = pygame.image.load('paused.png')
	pygame.mixer.music.pause()
	goback = pygame.image.load('back.png')
	gobackrect = goback.get_rect()
	pausedalive = True

	while pausedalive:
		#trick
		mouse=pygame.mouse.get_pos()
		m = pygame.draw.rect(root,BLACK,(mouse[0],mouse[1],100,100))


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					pausedalive = False
					pygame.mixer.music.unpause()
			if m.colliderect(gobackrect):
				if pygame.mouse.get_pressed()[0] == 1:
					pausedalive = False
					menue()
		#background
		root.blit(pausedimg,(0,0))
		root.blit(goback,gobackrect)
		pygame.display.update()





#Gameloop
def gameloop():
	#Loading Sprites
	pad1image = pygame.image.load('pad1.png').convert_alpha()
	pad1 = pad1image.get_rect()
	pad2image = pygame.image.load('pad2.png').convert_alpha()
	pad2 = pad2image.get_rect()
	background = pygame.image.load('background.png').convert()
	ballimage = pygame.image.load('ball.png').convert_alpha()
	ball = ballimage.get_rect()
	goback = pygame.image.load('back.png')
	gobackrect = goback.get_rect()


	#Music
	collusion = pygame.mixer.Sound('collusion.mp3')
	#ndgame=pygame.mixer.Sound('collusion.wav')
	pygame.mixer.music.load('bg.mp3')
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(-1)


	#setting images to the places
	pad1.left = rootrect.left + 6
	pad1.centery = rootrect.centery

	pad2.right = rootrect.right -6
	pad2.centery = rootrect.centery

	ball.right = w//2 + 10
	ball.centery = rootrect.centery
	#Game Junks
	FPS=120
	clock = pygame.time.Clock()



	xchange = 0
	ychange = 0
	x1change = 0
	y1change = 0
	ballxchange = 2
	ballychange = 2
	greenpoints = 0
	redpoints = 0
	active=True
	while active:
		#mouse trick
		mouse=pygame.mouse.get_pos()
		m = pygame.draw.rect(root,BLACK,(mouse[0],mouse[1],100,100))



		# event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					xchange = -1
				elif event.key == pygame.K_d:
					xchange = 1
				elif event.key == pygame.K_w:
					ychange = -1
				elif event.key == pygame.K_s:
					ychange = 1
				elif event.key == pygame.K_UP:
					y1change = -1
				elif event.key == pygame.K_DOWN:
					y1change = 1
				elif event.key == pygame.K_LEFT:
					x1change = -1
				elif event.key == pygame.K_RIGHT:
					x1change = 1
				elif event.key == pygame.K_p:
					paused()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					xchange = 0
				elif event.key == pygame.K_d:
					xchange = 0
				elif event.key == pygame.K_w:
					ychange = 0
				elif event.key == pygame.K_s:
					ychange = 0
				elif event.key == pygame.K_UP:
					y1change = 0
				elif event.key == pygame.K_DOWN:
					y1change = 0
				elif event.key == pygame.K_LEFT:
					x1change = 0
				elif event.key == pygame.K_RIGHT:
					x1change = 0			
		#Boundery Checking
		#RECTS
		topleft = pygame.draw.rect(root,BLACK,(0,99,35,1))
		botleft = pygame.draw.rect(root,BLACK,(0,298,40,1))
		topright = pygame.draw.rect(root,BLACK,(760,103,45,1))
		botright = pygame.draw.rect(root,BLACK,(752,297,49,1))

		topleft_left = pygame.draw.rect(root,BLACK,(40,24,1,75))
		botleft_left = pygame.draw.rect(root,BLACK,(42,300,1,73))

		topright_right = pygame.draw.rect(root,BLACK,(758,23,1,82))
		botright_right = pygame.draw.rect(root,BLACK,(751,298,1,74))

		bottom = pygame.draw.rect(root,BLACK,(37,372,717,10))
		top = pygame.draw.rect(root,BLACK,(37,17,717,10))



		#Checking
		if pad1.colliderect(topleft):
			pad1.y = 100
			pygame.mixer.Sound.play(collusion)
		if pad1.colliderect(botleft):
			pad1.y = 255
			pygame.mixer.Sound.play(collusion)
		if pad2.colliderect(topright):
			pad2.y = 104
			pygame.mixer.Sound.play(collusion)
		if pad2.colliderect(botright):
			pad2.y = 254
			pygame.mixer.Sound.play(collusion)
		if pad1.colliderect(topleft_left):
			pad1.x = 40
			pygame.mixer.Sound.play(collusion)
		if pad1.colliderect(botleft_left):
			pad1.x = 42
			pygame.mixer.Sound.play(collusion)
		if pad2.colliderect(topright_right):
			pad2.x = 718
			pygame.mixer.Sound.play(collusion)
		if pad2.colliderect(botright_right):
			pad2.x = 711
			pygame.mixer.Sound.play(collusion)

		if ball.colliderect(pad1):
			ballxchange = 2
			pygame.mixer.Sound.play(collusion)
		if ball.colliderect(pad2):
			ballxchange = -2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(bottom):
			ballychange = -2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(top):
			ballychange = 2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(topleft):
			ballychange = 2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(topleft_left):
			ballxchange = 2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(botleft):
			ballychange = -2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(botleft_left):
			ballxchange = 2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(topright):
			ballychange = 2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(topright_right):
			ballxchange = -2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(botright):
			ballychange = -2
			pygame.mixer.Sound.play(collusion)
		elif ball.colliderect(botright_right):
			ballxchange = -2
			pygame.mixer.Sound.play(collusion)
		elif ball.x > w-10:
			ball.right = w//2 + 10
			ball.centery = rootrect.centery
			ballxchange = -2 
			ballychane = 2
			greenpoints += 1
			pygame.mixer.Sound.play(collusion)
		elif ball.x < 10 :
			ball.right = w//2 + 10
			ball.centery = rootrect.centery
			ballxchange = 2 
			ballychane = 2
			redpoints += 1
			pygame.mixer.Sound.play(collusion)
		if m.colliderect(gobackrect):
			if pygame.mouse.get_pressed()[0] == 1:
				pygame.mixer.music.stop()
				active = False
				menue()
				gameloop()
		#pad1
		if pad1.y < 18:
			pad1.y=19
		if pad1.y > 333:
			pad1.y=332
		if pad1.x < 0:
			pad1.x=1
		if pad1.x > 355:
			pad1.x=354


		#pad2
		
		if pad2.y < 18:
			pad2.y= 19
		if pad2.y > 333:
			pad2.y = 332
		
		if pad2.x > 760:
			pad2.x=759
		if pad2.x < 410:
			pad2.x=411

		#change
		pad1.x += xchange
		pad1.y += ychange
		pad2.x += x1change
		pad2.y += y1change

		ball.x += ballxchange
		ball.y += ballychange
		#Backgorund
		root.blit(background,[0,0])
		message_display('{} - {}'.format(greenpoints,redpoints),400,35)
		#Object
		root.blit(goback,gobackrect)
		root.blit(ballimage,ball)
		root.blit(pad1image,pad1)
		root.blit(pad2image,pad2)
		pygame.display.update()
	clock.tick(FPS)




#Call
menue()
gameloop()
