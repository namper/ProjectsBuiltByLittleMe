class Flakes:
	def __init__(self,radiusi,cvlileba,x):
		self.r=radiusi
		self.c=cvlileba
		self.x=x
		self.y=0
		self.f=c.create_oval(self.x,self.y,self.x+self.r*2,self.y+self.r*2,fill='#%02x%02x%02x' % (int("{}".format(random.randint(1,216))), int("{}".format(random.randint(1,216))), int("{}".format(random.randint(1,216)))),outline='#%02x%02x%02x' % (int("{}".format(random.randint(1,216))), int("{}".format(random.randint(1,216))), int("{}".format(random.randint(1,216)))))

	def gazaoba(self):
		#modzraoba/shemocmeba
		c.move(self.f,0,self.c)
		pos=c.coords(self.f)
		if pos[1] >= h :
			#dabruneba
			self.x=random.randint(0,w)
			self.c=random.randint(0,5)#0 dan siganemde..
			c.coords(self.f,self.x,-self.r*2,self.x+2*self.r,0)

from tkinter import *
import random
#Logika
fifkebi=[]
w=400
h=300
fps=24
root=Tk()
root.geometry('{}x{}'.format(w,h))
c=Canvas(root,width=w,height=h,bg= "blue")
c.pack()
n=600#fifkebis raodenoba
for i in range(n+1):
	rad=random.randint(1,5)
	speed=random.randint(1,4)
	x0=random.randint(1,w)
	#self,radiusi,cvlileba,x,y
	qwer=Flakes(rad,speed,x0)
	fifkebi.append(qwer)
def putin():
	#def gazaoba
	for q in fifkebi:
		q.gazaoba()
	root.after(fps,putin)
putin()	
root.mainloop()
