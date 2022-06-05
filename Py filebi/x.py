from tkinter import * 
class Ball:
	def __init__(self,color,x0,y0):
		self.color=color
		self.x0=x0
		self.y0=y0
		self.ball=c.create_oval(w//2-r,h//2-r,w//2+r,h//2+r,fill=self.color,outline=self.color)
		self.pos=c.coords(self.ball)
	def move(self):

		c.move(self.ball,self.x0,self.y0)



mas=[] #burtis obieqtebi
w=800
h=500
r=9 
speed=6 
n=2 # burtebis raodenoba 
root=Tk()
root.geometry("{}x{}".format(w,h))
c=Canvas(root,bg="black",width=w,height=h)
c.pack()
for i in range(1,n+1):
	colori=['#b7dae8']
	mas.append(Ball(colori,0,3))#Ball
def app():
	for j in range(len(mas)):
		mas[j].move()
	root.after(10//speed*10,app)
app()
root.mainloop()
