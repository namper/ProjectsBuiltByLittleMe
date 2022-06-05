from pygame import math
#Constants
TITLE = 'Platform Game'
WIDTH = 800	
HEIGHT = 600
FPS = 60
ZERO = 0
FG = 200
FONT_NAME = 'arial' 
HS_FILE = 'highscore.txt'
SPRITE_FILENAME = 'spritesheet_jumper.png'

#Player properties
ACCELERATION = 0.35
FRICTION = -0.10
GRAVITY = 0.5
vec = math.Vector2

#Platform settings
PLATFORM_LIST = [\
(WIDTH/2, HEIGHT*3/4),\
(0, HEIGHT-60),\
(125, HEIGHT-350 ),\
(100, HEIGHT-200 ),\
(40, HEIGHT-300 )]

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 100)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BGCOLOR = (128, 184, 252)
