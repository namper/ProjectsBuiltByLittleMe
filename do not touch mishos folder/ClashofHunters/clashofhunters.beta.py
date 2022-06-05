import pygame,sys
import math
from pygame.locals import*
pygame.init()

black=(0,0,0)
white=(255,255,255)
w=500
h=500
root=pygame.display.set_mode((w+50,h),0,32)
pygame.display.set_caption('Clash of Hunters')
clock = pygame.time.Clock()

def distance(firstob,secondob,thirdmouse):
    d=math.sqrt(math.pow(thirdmouse[0]-firstob,2)+ math.pow(thirdmouse[1]-secondob,2))
    return d
def mainloop():
    
    running=False
    marksman=pygame.image.load('resized.png').convert_alpha()
    background=pygame.image.load('board.png').convert()
    dael=pygame.image.load('dael.png').convert_alpha()
    x=14;y=457;z=55;k=10;x1=240;y1=17
    root.blit(marksman,(x,y))
    root.blit(dael,(x1,y1))
    while not running:
        for event in pygame.event.get():
            mouse=pygame.mouse.get_pos()
            if event.type== pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif x>w:
                x-=2*z
            elif x<0:
                x+=2*z
            elif  y<=30:
                root.blit(marksman,(514,466))
            else:
                if pygame.mouse.get_pressed()[0]==1:
                    if distance(x,y,mouse):
                        x=mouse[0]
                        y=mouse[1]
                root.blit(background,(0,0))
                root.blit(marksman,(x,y))
                root.blit(dael,(x1,y1))
        pygame.display.update()
mainloop()
