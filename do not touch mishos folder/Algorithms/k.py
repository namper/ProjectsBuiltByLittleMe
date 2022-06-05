from tkinter import*
import time
w=600
h=300
padis_sigane=10
padis_sigrdze=75
padis_sichqare=8
fps=25
root=Tk()
root.geometry("{}x{}".format(w,h))
root.resizable(False,False)
c=Canvas(root,width=w,height=h,bg="Black")
c.pack()
ball_r=20
c.create_line(w//2,0,w//2,h,width=10,fill="lightblue")
c.create_line(padis_sigane,0,padis_sigane,h,width=2,fill="lightblue")
c.create_line(w-padis_sigane,0,w-padis_sigane,h,width=2,fill="lightblue")
c.create_oval(w//2-w//ball_r,h//2-w//ball_r,w//2+w//ball_r,h//2+w//ball_r,fill="red",outline="red")
class chogani:
	def __init__(self,x,y,speed):
		self.x=x
		self.y=y
		self.pad=c.create_rectangle(self.x,self.y,self.x+padis_sigane,self.y+padis_sigrdze,fill="blue",outline="blue")
		self.speed=speed
		self.active=False
	def shxuili(self):
		if self.active:
			c.move(self.pad,0,self.speed)
			if c.coords(self.pad)[3]>=h:
				c.coords(self.pad,self.x,h-padis_sigrdze,self.x+padis_sigane,h)
			elif c.coords(self.pad)[1]<=0:
				c.coords(self.pad,self.x,0,self.x+padis_sigane,padis_sigrdze)


pad1=chogani(0,1,padis_sichqare)
pad2=chogani(w-padis_sigane,1,padis_sichqare)
ball=c.create_oval(w//2-w//40,h//2-w//40,w//2+w//40,h//2+w//40,fill="Green",outline="Green")
def keypress(event):
	global main_active
	e=event.keysym
	if e=="w" or e=="W":
		pad1.speed=-abs(pad1.speed)
		pad1.shxuili()
		pad1.active=True
	elif e=="s" or e=="S":
		pad1.speed=abs(pad1.speed)
		pad1.shxuili()
		pad1.active=True
	elif e=="Up":
		pad2.speed=-abs(pad1.speed)
		pad2.shxuili()
		pad2.active=True
	elif e=="Down":
		pad2.speed=abs(pad2.speed)
		pad2.shxuili()
		pad2.active=True
		
def keyrelease(event):
	e1=event.keysym
	if e1=="w" or e1=="W" or e1=="S" or e1=="s":
		pad1.active=False
	elif e1=="Up" or e1=="Down":
		pad2.active=False
def pauza(event):
	if event.keysym=='p' or event.keysym=='P':
		main_active=False
	elif event.keysym=="c" or event.keysym=='C':
		main_active=True

d=ball_r-((padis_sigane*(2*ball_r-padis_sigane))**(1/2))
a=-10
b=10
main_active=True
def main():
	pad1.shxuili()
	pad2.shxuili()
	moveball()
	if main_active:
		root.after(fps,main)
def game_end():
	global main_active
	main_active=False
	print("Tamashi Morcha")
def retry():
	global main_active
	main_active=True
def moveball():
	global a,b
	posball=c.coords(ball)
	if posball[3]>=h or posball[1]<=0:
		b=-b
	pospad1=c.coords(pad1.pad)
	pospad2=c.coords(pad2.pad)
	moxvda_marcxniv=pospad1[0]<=posball[0]<=pospad1[2] and ((pospad1[1]<=posball[3]-d<=pospad1[3]) or (pospad1[1]<=posball[1]+d<=pospad1[3]))
	moxvda_marjvniv=pospad2[2]>= posball[2]>=pospad2[0] and ((pospad2[1]<=posball[3]-d<=pospad2[3]) or (pospad2[1]<=posball[1]+d<=pospad2[3]))
	if moxvda_marjvniv or moxvda_marcxniv:
		a=-a
	c.move(ball,a,b)
	if posball[0]<=0 or posball[2]>=w:
		game_end()
c.bind("<KeyPress>",keypress,pauza)
c.bind("<KeyRelease>",keyrelease)
c.focus_set()
main()
root.mainloop()