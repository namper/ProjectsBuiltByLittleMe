class Ball():
	def __init__(self,color,radiusi,x0,y0,cvlileba):
		self.color=color
		self.radiusi=radiusi
		self.x0=x0
		self.y0=y0
		self.cvlileba=cvlileba
		self.cvlileba1=cvlileba+3
		self.ball=c.create_oval(self.x0,self.y0,self.x0+2*self.radiusi,self.y0+2*self.radiusi,fill=self.color,outline=self.color)
	def move(self):
		c.move(self.ball,self.cvlileba,self.cvlileba1)



from tkinter import *
import random
width=800 #sigane	
height=600 #simagle
n=100 #burtebis raodenoba
fps=10
colors=["blue","#891edb","#db891e","yellow","green"]
root=Tk()
root.geometry("{}x{}".format(width,height))

c=Canvas(root,width=width,height=height,bg="red")
burtebi=[]
for i in range(n):
	color=random.choice(colors)
	radiusi=random.randint(10,40)
	x=random.randint(10,width-40)
	y=random.randint(10,height-40)
	cvlileba=random.randint(-2,5)
	burtebi.append(Ball(color,radiusi,x,y,cvlileba))

c.pack()
def modzraoba():
	for i in burtebi:
		i.move()
		pos=c.coords(i.ball)
		if pos[1]<=0 or pos[3]>=height:
			i.cvlileba1=-i.cvlileba1
		if pos[0]<=0 or pos[2]>=width:
			i.cvlileba=-i.cvlileba
	root.after(fps,modzraoba)

modzraoba()




root.mainloop()