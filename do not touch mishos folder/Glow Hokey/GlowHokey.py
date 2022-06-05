import pygame,sys,random
from pygame.locals import*

pygame.init()
#Coding below










#Atributes
WHITE = (211,211,211)
BLACK = (0,0,0)
w = 800;h = 400


#initilizing
root=pygame.display.set_mode((w,h))
rootrect=root.get_rect()
pygame.display.set_caption('Air Glow Hokey')




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



	#setting images to the places
	pad1.left = rootrect.left + 6
	pad1.centery = rootrect.centery

	pad2.right = rootrect.right -6
	pad2.centery = rootrect.centery

	ball.right = w//2 + 10
	ball.centery = rootrect.centery
	#Game Junks
	FPS=60
	clock = pygame.time.Clock()



	xchange=0
	ychange=0
	x1change=0
	y1change=0
	ballxchange=random.randint(-1,2)
	ballychange=random.randint(-1,2)
	active=True
	while active:



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

		if pad1.colliderect(botleft):
			pad1.y = 255
		if pad2.colliderect(topright):
			pad2.y = 104
		if pad2.colliderect(botright):
			pad2.y = 254
		if pad1.colliderect(topleft_left):
			pad1.x = 40
		if pad1.colliderect(botleft_left):
			pad1.x = 42
		if pad2.colliderect(topright_right):
			pad2.x = 718
		if pad2.colliderect(botright_right):
			pad2.x = 711

		if ball.colliderect(pad1):
			ballxchange = 1
		if ball.colliderect(pad2):
			ballxchange = -1
		elif ball.colliderect(bottom):
			ballychange = -1
		elif ball.colliderect(top):
			ballychange = 1
		elif ball.colliderect(topleft):
			ballychange = 1
		elif ball.colliderect(topleft_left):
			ballxchange = 1
		elif ball.colliderect(botleft):
			ballychange = -1
		elif ball.colliderect(botleft_left):
			ballxchange = 1
		elif ball.colliderect(topright):
			ballychange = 1
		elif ball.colliderect(topright_right):
			ballxchange = -1
		elif ball.colliderect(topleft):
			ballychange = 1
		elif ball.colliderect(topleft_left):
			ballxchange = 1
			

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
		'''
		
		if not ball.colliderect(bottom):
			#ball_move
			ballxmove = ball.x + random.randint(1,2)
			ballymove = ball.y + random.randint(1,2)
		
		if ball.colliderect(bottom):
			ballxmove = ball.x + random.randint(1,2)
			ballymove = ball.y + -(random.randint(1,2))
		ball.x = ballxmove
		ball.y = ballymove 
		'''
		#change
		pad1.x += xchange
		pad1.y += ychange
		pad2.x += x1change
		pad2.y += y1change

		ball.x += ballxchange
		ball.y += ballychange
		#Backgorund
		root.blit(background,[0,0])
		#Object
		root.blit(ballimage,ball)
		root.blit(pad1image,pad1)
		root.blit(pad2image,pad2)
		pygame.display.update()
	clock.tick(FPS)




#Call
gameloop()
