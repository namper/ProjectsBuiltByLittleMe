import pygame,sys,random

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load('ball1.png').convert_alpha()
		self.rect = self.image.get_rect()

class Block(pygame.sprite.Sprite):
	def __init__(self,image,color,size):
		super().__init__()
		self.image = pygame.image.load(image).convert_alpha()
		self.image.set_colorkey(color)
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image,size)

	def movement(self):
		self.rect.x = random.randint(10,w-10);self.rect.y = random.randint(10,h-10)		



pygame.init()
w = 400;h = 400;white=(255,255,255)
root = pygame.display.set_mode([w,h])
surface = root.get_rect()
pygame.display.set_caption('Sprite_class_test')

block_list = pygame.sprite.Group()
every_sprite_list = pygame.sprite.Group()

ball = Ball()
block = Block('wall.jpg',white,(20,20))
block_list.add(block)
every_sprite_list.add(ball,block)


def main():
	#working on game shittery
	custom = 10
	movement = 2
	zero = 0
	ballxchange = 0
	ballychange = 0
	FPS = 90
	clock = pygame.time.Clock()
	active = True
	#woring on ball
	ball.rect.x = 50;ball.rect.y=surface.centery-custom
	block.rect.x = random.randint(zero+custom,w-custom);block.rect.y = random.randint(zero+custom,h-custom)












	#Gamelooop
	while active:
		root.fill(white)#background
		for hit in pygame.sprite.spritecollide(ball,block_list,False,pygame.sprite.collide_mask):
			block.movement()



		#Key Handling
		for event in pygame.event.get():
			#Quit
			if event.type == pygame.QUIT:
				active = False
				sys.exit()
			#Keydown Expression
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:
					ballxchange = movement
				elif event.key == pygame.K_a:
					ballxchange = -movement
				elif event.key == pygame.K_w:
					ballychange = -movement
				elif event.key == pygame.K_s:
					ballychange = movement
			#Keyup exrpresion
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_d:
					ballxchange = zero
				elif event.key == pygame.K_a:
					ballxchange = zero
				elif event.key == pygame.K_w:
					ballychange = zero
				elif event.key == pygame.K_s:
					ballychange = zero
		#Boundary Checing
		if ball.rect.x < zero :
			ball.rect.x = zero
		if ball.rect.y < zero :
			ball.rect.y = zero
		if ball.rect.x > w-2*custom:
			ball.rect.x = w-2*custom
		if ball.rect.y > h-2*custom:
			ball.rect.y = h-2*custom


		#intilitizing
		ball.rect.x += ballxchange;ball.rect.y += ballychange
		every_sprite_list.draw(root)
		every_sprite_list.update()
		pygame.display.update()
		clock.tick(FPS)

if __name__ == '__main__':
	main()