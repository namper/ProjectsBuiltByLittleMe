import pygame
import random
black=(0,0,0)
white=(255,255,255)
w=600
h=600
root=pygame.display.set_mode((w,h))
pygame.display.set_caption('snow')
pygame.init()
n=100
SnowFlakes=[]
for q in range(n+1):
    x=random.randrange(0,600)
    y=random.randrange(0,600)
    SnowFlakes.append([x,y])
clock= pygame.time.Clock()
Exit= False
while not Exit:
    background=pygame.image.load('1.png').convert()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    root.blit(background,[0,0])    
    for i in SnowFlakes:
        i[1]+=1
        pygame.draw.circle(root,white,i,9)
        
        if i[1] > h:
            i[1] = random.randrange(-50,-5)
            i[0] = random.randrange(w)

    pygame.display.update()

    clock.tick(600)

