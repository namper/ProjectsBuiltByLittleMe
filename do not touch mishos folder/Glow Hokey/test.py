
import pygame

# --- constants --- (UPPER_CASE names)

WIDTH = 400
HEIGHT = 400

BLACK = ( 0, 0, 0)

FPS = 25

# --- main --- (lower_case names)

# - init -

pygame.init()

root = pygame.display.set_mode((WIDTH, HEIGHT))
root_rect = root.get_rect()

# - objects -

thing1 = pygame.image.load('pad1.png')
thing1_rect = thing1.get_rect()

thing2 = pygame.image.load('pad2.png')
thing2_rect = thing2.get_rect()

# move things
thing1_rect.left = root_rect.left
thing1_rect.centery = root_rect.centery

thing2_rect.right = root_rect.right
thing2_rect.centery = root_rect.centery

# - mainloop -

clock = pygame.time.Clock()
xchange=0
while True:
	global xchange

	# - events -

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	# - updates (without draws) -
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				xchange = 5
			
	# move objects
	print(xchange)
	thing1_rect.x += xchange
	thing2_rect.x -= 5

	# check collisions
	if thing1_rect.colliderect(thing2_rect):
		print('Collision')

	# - draws (without updates) -

	root.fill(BLACK)
	root.blit(thing1, thing1_rect)
	root.blit(thing2, thing2_rect)

	pygame.display.update()

	# - FPS -

	clock.tick(FPS)
 