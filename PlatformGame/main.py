# x`!/usr/bin/python3
#Platform game
#Background music: IZECOLD ft. Molly Ann - Close (Brooks Remix)
import pygame as pg
import random , ctypes
from settings import *
from sprites import *
from os import path

class Game:
	def __init__(self):
		# Initilize game window
		pg.init()
		pg.mixer.init()
		try:
			raise  TypeError
			user32 = ctypes.windll.user32
			screenSize =  user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
			size = (screenSize)
			self.screen = pg.display.set_mode((size) , pg.FULLSCREEN)
		except:
			self.screen = pg.display.set_mode((WIDTH,HEIGHT),pg.RESIZABLE)
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.running = True
		self.font_name = pg.font.match_font(FONT_NAME)
		self.load_data()

	def load_data(self):
		#Loading high score
		self.dir = path.dirname(__file__)
		with open(path.join(self.dir,HS_FILE), 'r+') as f:
			try:
				self.highscore = int(f.read())
			except :
				self.highscore = 0
		#Loading spirte sheet
		img_dir = path.join(self.dir, 'Spritesheets')
		self.spritesheet = Spritesheet(path.join(img_dir,SPRITE_FILENAME))
		self.sound_dir = path.join(self.dir,'sounds')
		self.jump_sound = pg.mixer.Sound(path.join(self.sound_dir,'jump37.wav'))

	def new(self):
		pg.mixer.music.load(path.join(self.sound_dir,'izecold.mp3'))
		pg.mixer.music.play(loops=-1)
		# Start a new game
		self.score = 0
		self.all_sprites = pg.sprite.Group()
		self.platform_group = pg.sprite.Group()
		self.player = Player(self)
		self.all_sprites.add(self.player)
		for plat in PLATFORM_LIST:
			p = Platform(self,*plat)
			self.all_sprites.add(p)
			self.platform_group.add(p)
		self.run()# every time new game start run Game loop
	def run(self):
		# Game loop
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()#Logic
			self.draw()
	def update(self):
		# Update
		self.all_sprites.update()
		if self.player.vel.y > 0:
			hits = pg.sprite.spritecollide(self.player,self.platform_group,False)
			if hits:
				lowest = hits[0]
				for hit in hits:
					if hit.rect.bottom > lowest.rect.bottom:
						lowest = hit
				if self.player.pos.y < lowest.rect.bottom:
					self.player.pos.y = lowest.rect.top + 1
					self.player.vel.y = 0 #Dening Gravity
		#Camera
		if self.player.rect.top <= HEIGHT/4:
			self.player.pos.y += max(abs(self.player.vel.y),2)
			for plat in self.platform_group:
				plat.rect.y += max(abs(self.player.vel.y),2)
				if plat.rect.top >= HEIGHT:
					plat.kill()
					self.score += 10

		#Die
		if self.player.rect.bottom > HEIGHT:
			for sprite in self.all_sprites:
				sprite.rect.y -= max(self.player.vel.y,10)
				if sprite.rect.bottom < 0:
					sprite.kill()
		if len(self.platform_group) == 0:
			self.playing = False

		#Spawning new platforms
		while len(self.platform_group) < 6:
			width = random.randrange(20,110)
			p = Platform(self,random.randrange(0,WIDTH-width),random.randrange(-50,-10))
			self.platform_group.add(p)
			self.all_sprites.add(p)

	def events(self):
		# Event Handling
		for event in pg.event.get():
			#check for closing window
			if event.type == pg.QUIT:
				#Exiting run loop
				if self.playing:
					self.playing = False
			#Exiting non-class loopdd
				self.running = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_w:
					self.player.jump()
				elif event.key == pg.K_q:
					self.playing = False
					self.running = False


	def  draw(self):
		# Drawwing
		self.screen.fill(BGCOLOR)#Background
		self.all_sprites.draw(self.screen)
		self.screen.blit(self.player.image,self.player.rect)
		self.render_text(str(self.score), 22, WHITE, WIDTH/2, 15)
		# After Drawwing update everything
		pg.display.update()


	def show_start_screen(self):
		pg.mixer.music.load(path.join(self.sound_dir,'openning.mp3'))
		pg.mixer.music.play(loops=-1)
		# Game Splash/Start Screen
		self.screen.fill(BGCOLOR)
		self.render_text(TITLE, 48, BLACK, WIDTH/2, HEIGHT/4)
		self.render_text('AD for move and W for jump', 22, BLACK, WIDTH/2, HEIGHT/2)
		self.render_text('Press any key to play', 22, BLACK, WIDTH/2, HEIGHT*3/4)
		self.render_text('High Score : '+str(self.highscore), 22, YELLOW, WIDTH/2, HEIGHT/6)
		pg.display.update()
		self.wait_for_key()
		pg.mixer.music.fadeout(500)

	def show_end_screen(self):
		# Game 
		pg.mixer.music.fadeout(500)
		pg.mixer.music.load(path.join(self.sound_dir,'ending.mp3'))
		pg.mixer.music.play(loops=-1)
		if not self.running:
			return None
		self.screen.fill(BGCOLOR)
		self.render_text('GAME OVER', 48, BLACK, WIDTH/2, HEIGHT/4)
		self.render_text('Score:'+str(self.score), 22, BLACK, WIDTH/2, HEIGHT/2)
		self.render_text('Press any key to play', 22, BLACK, WIDTH/2, HEIGHT*3/4)
		if self.score > self.highscore:
			self.highscore = self.score
			self.render_text("New High Score: "+str(self.highscore), 22, RED, WIDTH/2 , HEIGHT/2+50)
			with open(path.join(self.dir,HS_FILE), 'w') as f:
				f.write(str(self.highscore))
		else:
			self.render_text("High Score: "+str(self.highscore), 22, RED, WIDTH/2 , HEIGHT/2+50)
		pg.display.update()
		self.wait_for_key()
		pg.mixer.music.fadeout(500)
	def wait_for_key(self):
		waiting = True
		while waiting:
			self.clock.tick(FPS/2)
			for event in pg.event.get():
				if event.type == pg.QUIT:
					waiting = False
					self.running = False
				if event.type == pg.KEYUP:
					waiting = False
				if event.type == pg.KEYDOWN and event.key == pg.K_q:
					self.running = False
					self.playing = False		


	def render_text(self, text, size, color, x, y):
		font = pg.font.Font(self.font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		self.screen.blit(text_surface, text_rect)
g = Game()#Object
g.show_start_screen()
while g.running:
	g.new()
	g.show_end_screen()
pg.quit()