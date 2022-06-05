from tkinter import*
import random
root=Tk()
black='#000000'
white='#ffffff'
blue='#cce3f9'
w=600
h=600
root.geometry(('{}x{}').format(w,h))
n=100
SnowFlakes=[]
for q in range(n+1):
    x=random.randrange(0,w)
    y=random.randrange(0,h)
    SnowFlakes.append([x,y])
    
c=Canvas(root,bg=black,width=w,height=h)
r=9
c.pack()       
for i in SnowFlakes:
    i[1]+=1
    ball=c.create_oval(x//2-r,y//2-r,x//2+r,y//2+r,fill=white,outline=blue)
    if i[1] > h:
        i[1] = random.randrange(-50,-5)
        i[0] = random.randrange(w)
mainloop()
