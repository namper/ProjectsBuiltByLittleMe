import pygame,sys 
from random import randint

#Attributes
class soundbutton:
	def __init__(self, xcord , ycord ,color,sound):
		self.x = xcord
		self.y = ycord
		self.color = color
		self.w = 100
		self.h = 100
		self.button = pygame.draw.rect(root,self.color,(self.x,self.y,self.w,self.h))
		self.sound = sound
	def playing(self):
		pygame.mixer.Sound.play(self.sound)





#Display
w=400
h=510

#Color
bgcolor = (48, 46, 41)

headcolor_dark = (255, 191, 0)
headcolor_light = (252, 255, 94)

green = (64, 206, 4)
lightgreen = (114, 255, 0)

blue = (40, 72, 255)
lightblue = (62, 221, 249)

purple = (171, 22, 201)
lightpurple = (218, 62, 249)

white = (255,255,255)


#message display
def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def message_display(text,x,y):
	largeText = pygame.font.Font('freesansbold.ttf',50)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = (x,y)
	root.blit(TextSurf, TextRect)


#Initalisation
pygame.init()
pygame.mixer.init()
root = pygame.display.set_mode((w,h))
pygame.display.set_caption('Drum Pads 24')




#Sprites
record = pygame.image.load('rec.png').convert_alpha()
left = pygame.image.load('three.png').convert_alpha()
notleft = pygame.image.load('notthree.png').convert_alpha()
title = pygame.image.load('title.jpg').convert()

clock = pygame.time.Clock()
#Functions

def mainloop():
	#Sprites sqrt = 35

	colorG = green ; colorG1 = green ; colorG2 = green ; colorG3 = green

	colorB = blue ;colorB1 = blue ;colorB2 = blue ;colorB3 = blue ;colorB4 = blue ;colorB5 = blue ;colorB6 = blue ;colorB7 = blue ;colorB8 = blue 

	colorP = purple ; colorP1 = purple ; colorP2 = purple ; colorP3 = purple

	headcolor1 = headcolor_dark ; headcolor2 = headcolor_dark ; headcolor3 = headcolor_dark

	#Sounds
	s1 = pygame.mixer.Sound('1.wav')
	s2 = pygame.mixer.Sound('2.wav')
	s3 = pygame.mixer.Sound('3.wav')
	s4 = pygame.mixer.Sound('4.wav')
	s5 = pygame.mixer.Sound('5.wav')
	s6 = pygame.mixer.Sound('6.wav')
	s7 = pygame.mixer.Sound('7.wav')
	s8 = pygame.mixer.Sound('8.wav')
	s9 = pygame.mixer.Sound('9.wav')
	s10 = pygame.mixer.Sound('10.wav')
	s11 = pygame.mixer.Sound('11.wav')
	s12 = pygame.mixer.Sound('12.wav')


	active = True
	while  active:
		#mouse trick
		mouse = pygame.mouse.get_pos()
		mouserect = pygame.draw.rect(root,white,(mouse[0],mouse[1],1,1))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				#greeen
				if event.key == pygame.K_1:
					colorG = lightgreen
					G1.playing()
				if event.key == pygame.K_2:
					colorG1 = lightgreen
					G2.playing()
				if event.key == pygame.K_3:
					colorG2 = lightgreen
					G3.playing()
				if event.key == pygame.K_4:
					colorG3 = lightgreen
					G4.playing()
				#blue
				if event.key == pygame.K_q:
					colorB = lightblue
					B1.playing()
				if event.key == pygame.K_w:
					colorB1 = lightblue
					B2.playing()
				if event.key == pygame.K_e:
					colorB2 = lightblue
					B3.playing()
				if event.key == pygame.K_r:
					colorB3 = lightblue
					B4.playing()
				if event.key == pygame.K_z:
					colorB4 = lightblue
					B5.playing()
				if event.key == pygame.K_x:
					colorB5 = lightblue
					B6.playing()
				if event.key == pygame.K_c:
					colorB6 = lightblue
					B7.playing()
				if event.key == pygame.K_v:
					colorB7 = lightblue
					B8.playing()
				#purple
				if event.key == pygame.K_a:
					colorP = lightpurple
					P1.playing()
				if event.key == pygame.K_s:
					colorP1 = lightpurple
					P2.playing()
				if event.key == pygame.K_d:
					colorP2 = lightpurple
					P3.playing()
				if event.key == pygame.K_f:
					colorP3 = lightpurple
					P4.playing()
			elif event.type == pygame.KEYUP:
				#greeen
				if event.key == pygame.K_1:
					colorG = green
				if event.key == pygame.K_2:
					colorG1 = green
				if event.key == pygame.K_3:
					colorG2 = green
				if event.key == pygame.K_4:
					colorG3 = green
				#blue
				if event.key == pygame.K_q:
					colorB = blue
				if event.key == pygame.K_w:
					colorB1 = blue
				if event.key == pygame.K_e:
					colorB2 = blue
				if event.key == pygame.K_r:
					colorB3 = blue
				if event.key == pygame.K_z:
					colorB4 = blue
				if event.key == pygame.K_x:
					colorB5 = blue
				if event.key == pygame.K_c:
					colorB6 = blue
				if event.key == pygame.K_v:
					colorB7 = blue
				#purple
				if event.key == pygame.K_a:
					colorP = purple
				if event.key == pygame.K_s:
					colorP1 = purple
				if event.key == pygame.K_d:
					colorP2 = purple
				if event.key == pygame.K_f:
					colorP3 = purple


		#background
		root.fill(bgcolor)
		#head
		pygame.draw.rect(root,headcolor_dark,(0,0,400,50))

		#bottom
		root.blit(title, (0,450))
		#Buttons
		mbutton1 = pygame.draw.rect(root,headcolor1,(2,0,120,50))
		mbutton2 = pygame.draw.rect(root,headcolor2,(140,0,120,50))
		mbutton3 = pygame.draw.rect(root,headcolor3,(275,0,120,50))
		#Bimage
		root.blit(record,(155,7))
		root.blit(left,(-5,-20))
		root.blit(notleft,(253,-20))


		#Mouse detecion
		if mouserect.colliderect(mbutton1):
			headcolor1 = headcolor_light
			if pygame.mouse.get_pressed()[0] == 1:
				pass
		else :
			headcolor1 = headcolor_dark

		if mouserect.colliderect(mbutton2):
			headcolor2 = headcolor_light
			if pygame.mouse.get_pressed()[0] == 1:
				pass
		else :
			headcolor2 = headcolor_dark

		if mouserect.colliderect(mbutton3):
			headcolor3 = headcolor_light
			if pygame.mouse.get_pressed()[0] == 1:
				pass
		else:
			headcolor3 = headcolor_dark


		#sound buttons(xcord , ycord ,color,sound)
		G1 = soundbutton(0,50,colorG,s1)
		B1 = soundbutton(0,152,colorB,s2)
		P1 = soundbutton(0,254, colorP,s3)
		B5 = soundbutton(0,356,colorB4,s4)
		G2 = soundbutton(102,50,colorG1,s5)
		B2 = soundbutton(102,152,colorB1,s6)
		P2 = soundbutton(102,254,colorP1,s7)
		B6 = soundbutton(102,356,colorB5,s8)
		G3 = soundbutton(204,50,colorG2,s9)
		B3 = soundbutton(204,152,colorB2,s10)
		P3 = soundbutton(204,254,colorP2,s11)
		B7 = soundbutton(204,356,colorB6,s12)
		G4 = soundbutton(306,50,colorG3,s12)
		B4 = soundbutton(306,152,colorB3,s12)
		P4 = soundbutton(306,254,colorP3,s12)
		B8 = soundbutton(306,356,colorB7,s12)



		#msg text,x,y
		message_display('1',45,100)
		message_display('2',150,100)
		message_display('3',255,100)
		message_display('4',360,100)

		message_display('Q',45,205)
		message_display('W',150,205)
		message_display('E',255,205)
		message_display('R',360,205)

		message_display('A',45,310)
		message_display('S',150,310)
		message_display('D',255,310)
		message_display('F',360,310)

		message_display('Z',45,415)
		message_display('X',150,415)
		message_display('C',255,415)
		message_display('V',360,415)
		pygame.display.update()
	clock.tick(200)
mainloop()