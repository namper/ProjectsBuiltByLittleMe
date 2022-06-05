import pygame as pg
from random import choice
from settings import *


class Player(pg.sprite.Sprite):
	def __init__(self,game):
		#Super Constructor/calling parent class
		super(self.__class__,self).__init__()
		self.game = game
		self.walking = False
		self.jumping = False
		self.current_frame = 0
		self.last_update = 0
		self.load_images()
		self.image = self.standing_frames[0]
		self.rect = self.image.get_rect()
		self.rect.center = (40, HEIGHT-100)
		self.pos = vec(40, HEIGHT-100)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)

	def load_images(self):
		self.standing_frames = [self.game.spritesheet.get_image(614, 1063, 120, 191),\
							   self.game.spritesheet.get_image(690, 406, 120, 201)]
		self.walking_frames_r = [self.game.spritesheet.get_image(678, 860, 120, 201),\
								 self.game.spritesheet.get_image(692, 1458, 120, 207)]
		self.walking_frames_l = [pg.transform.flip(frame, True, False) for frame in self.walking_frames_r]
		self.jump_frame = self.game.spritesheet.get_image(382, 763, 150, 181)

	def jump(self):
		#Jump only when standing on platfrom
		self.rect.x += 2
		hits = pg.sprite.spritecollide(self,self.game.platform_group,False)
		self.rect.x -= 2
		if hits:
			pg.mixer.Sound.play(self.game.jump_sound)
			self.vel.y = -abs(FG*FRICTION)

	def update(self):
		self.animate()
		self.acc = vec(0, GRAVITY) 
		keys = pg.key.get_pressed()
		if keys[pg.K_a]:
			self.acc.x = -ACCELERATION
		elif keys[pg.K_d]:
			self.acc.x = ACCELERATION
		# Apply Friction
		self.acc.x += self.vel.x * FRICTION
		self.vel += self.acc
		#Forcing velocity to drop and become 0
		if abs(self.vel.x) < 0.15:
			self.vel.x = 0 
		self.pos += self.vel + ACCELERATION * self.acc 

		# Collusion Betwen Display and Player
		if self.pos.x > WIDTH  :
			self.pos.x = ZERO  
		elif self.pos.x < ZERO :
			self.pos.x = WIDTH

		self.rect.midbottom = self.pos

	def animate(self):
		now = pg.time.get_ticks()
		if self.vel.x != 0 :
			self.walking = True
		else:
			self.walking = False

		#Walking animation
		if self.walking:
			if now - self.last_update > 200:
				self.last_update = now
				self.current_frame = (self.current_frame+1) % len(self.walking_frames_r)
				bottom = self.rect.bottom
				if self.vel.x > 0 :
					self.image = self.walking_frames_r[self.current_frame]
				else:
					self.image = self.walking_frames_l[self.current_frame]
				self.image.set_colorkey(BLACK)
				self.rect = self.image.get_rect()
				self.rect.bottom = bottom
		#Standing animation
		if not self.jumping and not self.walking:
			if now - self.last_update > 350:
				self.last_update = now
				self.current_frame = (self.current_frame+1) % len(self.standing_frames)
				bottom = self.rect.bottom
				self.image = self.standing_frames[self.current_frame]
				self.image.set_colorkey(BLACK)
				self.rect = self.image.get_rect()
				self.rect.bottom = bottom




class Platform(pg.sprite.Sprite):
	def __init__(self,game,x,y):
		super(self.__class__,self).__init__()
		self.game = game
		self.images = [self.game.spritesheet.get_image(0, 288, 380, 94),\
					   self.game.spritesheet.get_image(213, 1662, 201, 100),\
					   self.game.spritesheet.get_image(382, 204, 200, 100),\
					   self.game.spritesheet.get_image(0, 384, 380, 94)]	
		self.image = choice(self.images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Spritesheet:
	def __init__(self, filename):
		self.spritesheet = pg.image.load(filename).convert()

	def get_image(self,x,y,w,h):
		#getting specified image
		image = pg.Surface([w,h])	
		image.blit(self.spritesheet, [0,0], [x,y,w,h])
		image = pg.transform.scale(image, [w//4 , h//4])
		return image