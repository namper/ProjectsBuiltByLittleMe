import pygame
import time
import random

pygame.init()
pygame.mixer.init()
crashed=pygame.mixer.Sound('Crash.wav')
endgame=pygame.mixer.Sound('Endgame.wav')
pygame.mixer.music.load('BGsound.wav')
display_width = 800
display_height = 500

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow=(255, 244, 73)

b_yellow=(255, 240, 15)
car_width = 40

root = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Mario Game')
clock = pygame.time.Clock()



def paused():
	pausedimg=pygame.image.load('pausedd.png')
	pygame.mixer.music.pause()
	pauza = True
	while pauza:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			root.fill(white)
			if event.type == pygame.KEYDOWN and event.key==pygame.K_c:
				pygame.mixer.music.unpause()
				pauza = False
		root.blit(pausedimg,(0,0))
		pygame.display.update()		
	clock.tick(10)

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: "+str(count), True, red)
	root.blit(text,(0,0))

def things(thing,x, y,):
	#pygame.draw.rect(root, color, [thingx, thingy, thingw, thingh])
	root.blit(thing,[x,y,80,80])

def car(x,y,z):
	root.blit(z,(x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	root.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()
	
	

def crash():
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crashed)
	pygame.mixer.Sound.play(endgame)
	message_display('You Crashed')
def menue():
	m=pygame.image.load('menue.png').convert()
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

		root.blit(m,(0,0))
		largeText = pygame.font.Font('freesansbold.ttf',50)
		TextSurf, TextRect = text_objects('The Mario Game', largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		mouse=pygame.mouse.get_pos()
		if 140+150>mouse[0]>140 and 350+40>mouse[1]>350:
			pygame.draw.rect(root,yellow,(140,350,150,40))
			if pygame.mouse.get_pressed()[0]==1:
				intro=False
		else:
			pygame.draw.rect(root,b_yellow,(140,350,150,40))
		if 340+150>mouse[0]>340 and 350+40>mouse[1]>350:
			pygame.draw.rect(root,yellow,(340,350,150,40))
			if pygame.mouse.get_pressed()[0]==1:
				m=pygame.image.load('credits.png').convert()
		else:
			pygame.draw.rect(root,b_yellow,(340,350,150,40))
		if 540+150>mouse[0]>540 and 350+40>mouse[1]>350:
			pygame.draw.rect(root,yellow,(540,350,150,40))
			if pygame.mouse.get_pressed()[0]==1:
				pygame.quit()
				quit()
		else:
			pygame.draw.rect(root,b_yellow,(540,350,150,40))
		smallText=pygame.font.Font('freesansbold.ttf',20)
		textSurf,textRect=text_objects('New Game',smallText)
		textRect.center=(140+(150//2),350+(40//2))

		textSurf1,textRect1=text_objects('Credits',smallText)
		textRect1.center=(340+(150//2),350+(40//2))

		textSurf2,textRect2=text_objects('Exit',smallText)
		textRect2.center=(540+(150//2),350+(40//2))

		root.blit(TextSurf, TextRect)
		root.blit(textSurf,textRect)
		root.blit(textSurf1,textRect1)
		root.blit(textSurf2,textRect2)
		pygame.display.update()		
	clock.tick(10)
	
def game_loop():

	global q 
	pygame.mixer.music.play(-1)
	x = (display_width * 0.45)
	y = (display_height * 0.8)

	x_change = 0
	y_change=0

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 4
	thing_width = 60
	thing_height = 60

	thingCount = 1

	dodged = 0
	alive=True
	carImg = pygame.image.load('mario1.png').convert_alpha()
	carrect=carImg.get_rect()
	carImg1 = pygame.image.load('mario.png').convert_alpha()
	bimage = pygame.image.load('background.png').convert()
	carImg2=pygame.image.load('mario2.png').convert_alpha()
	block=pygame.image.load('mushroom.png').convert_alpha()
	thingrect=block.get_rect()
	r1=block.get_rect()
	r2=carImg.get_rect()
	while alive==True:
		mouse=pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					x_change = -5
					carImg=carImg2
				elif event.key == pygame.K_d:
					x_change = 5
					carImg=carImg1
				elif event.key==pygame.K_w:
					y_change = -7
				elif event.key == pygame.K_p:
					paused()

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d:
					x_change = 0
				if event.key==pygame.K_w:
					y_change = 4

		x += x_change
		y += y_change
		if y>display_height-90:
			y=410
			y_change=0
		elif y<300:
			y_change=4
		root.blit(bimage,(0,0))

		# things(thingx, thingy, thingw, thingh, color)
		things(block,thing_startx, thing_starty)

		#Back Button
		#pygame.draw.rect(root, color, [thingx, thingy, thingw, thingh]
		backbutton=pygame.image.load('back.png').convert_alpha()
		root.blit(backbutton,(0,20))
		if 40>mouse[0]>0 and 20+54>mouse[1]>20:
			if pygame.mouse.get_pressed()[0]==1:
				pygame.mixer.music.stop()
				alive=False
				menue()
				game_loop()
		thing_starty += thing_speed
		car(x,y,carImg)
		things_dodged(dodged)

		if x > display_width - car_width or x < 0:
			crash()


		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
			dodged += 1
			thing_speed += 0.1*dodged

		if y < thing_starty+thing_height:
			#y crossover

			if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
				#x crossover
		#if carrect.colliderect(thingrect)==1:
		#print(r1.colliderect(r2))
				crash()

		
		pygame.display.update()
		clock.tick(60)
menue()
game_loop()
