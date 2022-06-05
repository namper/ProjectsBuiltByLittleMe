import pygame,sys
from pygame.locals import*
#attributes
w = 800;h = 200
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
display = pygame.display.set_mode((w,h))
surface = display.get_rect()
pygame.display.set_caption('Y ve to be balled to play this game')

def main():
	#working on game shittery
	custom = 10
	movement = 1
	zero = 0
	ballxchange = 0
	ballychange = 0
	FPS = 60
	clock = pygame.time.Clock()
	active = True
	#woring on ball
	ballimage = pygame.image.load('ball1.png').convert_alpha()
	ball = ballimage.get_rect()
	ball.x = 50;ball.y=surface.centery-custom















	#Gamelooop
	while active:
		display.fill(white)#background



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
		if ball.x < zero :
			ball.x = zero
		elif ball.y < zero :
			ball.y = zero
		elif ball.x > w-2*custom:
			ball.x = w-2*custom
		elif ball.y > h-2*custom:
			ball.y = h-2*custom


		#intilitizing
		ball.x += ballxchange;ball.y += ballychange
		display.blit(ballimage,ball)
		#print('x: {}  y: {}'.format(ball.x,ball.y))
		pygame.display.update()
		clock.tick(FPS)
if __name__ == '__main__':
	main()