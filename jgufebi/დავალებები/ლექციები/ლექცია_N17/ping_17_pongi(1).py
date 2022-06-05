from tkinter import*
w=600
h=300
padis_sigane=10
padis_sigrdze=75
padis_sichqare=5
ball_r=20
fps=30
a=3
b=4
win_L=0
win_R=0
main_active=True
root=Tk()
root.geometry("{}x{}".format(w,h))
root.resizable(False,False)
c=Canvas(root,width=w,height=h,bg="green")
c.pack()
c.create_line(w//2,0,w//2,h,width=10,fill="white")
c.create_line(padis_sigane,0,padis_sigane,h,width=2,fill="white")
c.create_line(w-padis_sigane,0,w-padis_sigane,h,width=2,fill="white")
c.create_oval(w//2-w//30,h//2-w//30,w//2+w//30,h//2+w//30,fill="white",outline="white")
ball=c.create_oval(w//2-ball_r,h//2-ball_r,w//2+ball_r,h//2+ball_r,fill="red",outline="red")
lab_info1=Label(root,text="resume : p" ,font="bold 10",bg="green")
lab_info2=Label(root,text="restart :   r" ,font="bold 10",bg="green")
lab_pause=Label(root,text="PAUSE" ,font="Arial 40",bg="green")
lab_restart=Label(root,text="PRESS : R" ,font="Arial 40",bg="green")
lab_tablo=Label(root,text="{} : {}".format(win_L,win_R),bg="green",font="Arial 20")
lab_tablo.place(relx=0.45,rely=0)

d=ball_r-(padis_sigane*(2*ball_r-padis_sigane))**(1/2)
class chogani:
	def __init__(self,x,y,speed):
		self.x=x
		self.y=y
		self.pad=c.create_rectangle(self.x,self.y,self.x+padis_sigane,self.y+padis_sigrdze,fill="lightblue",outline="white")
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

def keypress(event):
	global main_active
	e=event.keysym
	if e =="w" or e=="W":
		pad1.speed=-abs(pad1.speed)
		pad1.active=True
	elif e=="s" or e=="S":
		pad1.speed=abs(pad1.speed)
		pad1.active=True
	elif e=="Up":
		pad2.speed=-abs(pad2.speed)
		pad2.active=True
	elif e=="Down":
		pad2.speed=abs(pad2.speed)
		pad2.active=True
	elif e=="p" or e=="P":
		game_pause()
	elif e=="r" or e=="R":
		main_active=False



def keyrelease(event):
	e1=event.keysym
	if e1=="w" or e1=="s" or e1=="S" or e1=="W":
		pad1.active=False
	elif e1=="Down" or e1=="Up":
		pad2.active=False
	elif e1=="r" or e1=="R":
		game_restart()


def move_ball():
	global a,b
	pos_ball=c.coords(ball)
	if pos_ball[1]<=0 or pos_ball[3]>=h:
		b=-b


	# padebtan shexeba
	pos_pad_L=c.coords(pad1.pad)
	pos_pad_R=c.coords(pad2.pad)
	moxvda_marcxniv=(pos_pad_L[0]<=pos_ball[0]<=pos_pad_L[2]) and ((pos_pad_L[1] <= pos_ball[3]-d<= pos_pad_L[3]) or (pos_pad_L[1] <= pos_ball[1]+d<= pos_pad_L[3]))
	moxvda_marjvniv=(pos_pad_R[0]<=pos_ball[2]<=pos_pad_R[2]) and ((pos_pad_R[1] <= pos_ball[3]-d<= pos_pad_R[3]) or (pos_pad_R[1] <= pos_ball[1]+d<= pos_pad_R[3]))
	if moxvda_marcxniv or moxvda_marjvniv:
		a=-a
	c.move(ball,a,b)
	if pos_ball[0]<=0 or pos_ball[2]>=w:
		game_end()

def game_restart():
	global main_active
	c.coords(ball,w//2-w//30,h//2-w//30,w//2+w//30,h//2+w//30)
	main_active=True
	main()
	lab_pause.place_forget()
	lab_info1.place_forget()
	lab_info2.place_forget()
	lab_restart.place_forget()

def game_pause():
	global main_active
	if main_active==False:
		main_active=True
		main()
		lab_pause.place_forget()
		lab_info1.place_forget()
		lab_info2.place_forget()
	else :
		main_active=False
		lab_pause.place(relx=0.35,rely=0.4)
		lab_info1.place(relx=0.8,rely=0.7)
		lab_info2.place(relx=0.8,rely=0.8)

def game_end():
	global main_active,win_R,win_L
	main_active=False
	lab_restart.place(relx=0.3,rely=0.4)
	if a>0:
		win_L+=1
	else:
		win_R+=1
	lab_tablo.config(text="{} : {}".format(win_L,win_R))


def main():
	pad1.shxuili()
	pad2.shxuili()
	move_ball()
	if main_active:
		root.after(fps,main)

c.bind("<KeyPress>",keypress)
c.bind("<KeyRelease>",keyrelease)
c.focus_set()




main()
root.mainloop()