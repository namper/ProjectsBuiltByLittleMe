from tkinter import * 
class Ball:
	def __init__(self,color,x0,y0):
		self.color=color
		self.x0=x0
		self.y0=y0
		self.ball=c.create_oval(width//2-r,height//2-r,width//2+r,height//2+r,fill=self.color,outline=self.color)
		self.pos=c.coords(self.ball)
	def move(self):
		self.pos=c.coords(self.ball)
		if self.pos[1]<=0 or self.pos[3]>=height:
			self.y0=-self.y0
		if self.pos[0]<=0 or self.pos[2]>=width:
			self.x0=-self.x0
		c.move(self.ball,self.x0,self.y0)
k=0
p=1
pos=[]
mas=[] # am masivshi chavyrit burtis obieqtebs
width=800#root.winfo_screenwidth()
height=500#root.winfo_screenheight()
colors=["#d42341","#64c62b","#2bc6c6","#963ab7","#e01806","#0673e0"] #ferebis masivi
r=60  #burtebis radiusi
speed=6 # 1  ---> 10
n=3 # burtebis raodenoba 1 dan 5 mde
root=Tk()
root.geometry("{}x{}".format(width,height))
c=Canvas(root,bg="pink",width=width,height=height)
c.pack()
for i in range(1,n+1):
	colori=colors[i%6] # ferebis shercheva
	mas.append(Ball(colori,i+4,0)) #vqmnit Ball-is obieqtebs da shemdeg vyrit masivshi append funqciis gamoyenebit
def app():
	global k,p
	for j in range(len(mas)):# satitaod vidzaxeb yvela obieqtistvis modzraobis funqcias
		mas[j].move()
		if j!=len(mas)-1 and k<=0:
			if ((mas[j].pos[2]>=mas[j+1].pos[0])and (mas[j+1].pos[2]>=mas[j].pos[0])) or ((mas[j+1].pos[2]>=mas[j].pos[0]) and (mas[j].pos[2]>=mas[j+1].pos[0])):
				if p==1:
					k=500
					p=0
				else:
					k=50
				mas[j].x0*=-1
				mas[j+1].x0*=-1
		k-=1
	root.after(10//speed*10,app)
app()
root.mainloop()
