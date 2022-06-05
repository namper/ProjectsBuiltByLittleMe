#Platform game
import pygame as pg
import random
from settings import *

class Game:
	def __init__(self):
		# Initilize game window
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((WIDTH,HEIGHT))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.running = True

	def new(self):
		# Start a new game
		self.all_sprites = pg.sprite.Group()
		self.run()# every time new game start run Game loop
	def run(self):
		# Game loop
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def update(self):
		# Update
		self.all_sprites.update()

	def events(self):
		# Event Handling
		for event in pg.event.get():
			#check for closing window
			if event.type == pg.QUIT:
				#Exiting run loop
				if self.playing:
					self.playing = False
			#Exiting non-class loop
			self.running = False

	def  draw(self):
		# Drawwing
		self.screen.fill(BLACK)
		self.all_sprites.draw(self.screen)
		# After Drawwing update everything
		pg.display.update()


	def show_start_screen(self):
		# Game Splash/Start Screeb
		pass

	def show_end_screen(self):
		# Game Over
		pass
g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_end_screen()
pg.quit()