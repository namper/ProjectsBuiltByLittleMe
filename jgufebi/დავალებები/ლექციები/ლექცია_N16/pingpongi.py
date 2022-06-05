from tkinter import*
w=600
h=300
padis_sigane=10
padis_sigrdze=75
padis_sichqare=5
root=Tk()
root.geometry("{}x{}".format(w,h))
root.resizable(False,False)
c=Canvas(root,width=w,height=h,bg="green")
c.pack()
c.create_line(w//2,0,w//2,h,width=10,fill="white")
c.create_line(padis_sigane,0,padis_sigane,h,width=2,fill="white")
c.create_line(w-padis_sigane,0,w-padis_sigane,h,width=2,fill="white")
c.create_oval(w//2-w//30,h//2-w//30,w//2+w//30,h//2+w//30,fill="white",outline="white")
class chogani:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.pad=c.create_rectangle(self.x,self.y,self.x+padis_sigane,self.y+padis_sigrdze,fill="lightblue",outline="white")
	def shxuili(self):
		c.move(self.pad,0,padis_sichqare)
		if c.coords(self.pad)[3]>=h:
			c.coords(self.pad,self.x,h-padis_sigrdze,self.x+padis_sigane,h)
		elif c.coords(self.pad)[1]<=0:
			c.coords(self.pad,self.x,0,self.x+padis_sigane,padis_sigrdze)

pad1=chogani(0,1)
pad2=chogani(w-padis_sigane,1)

c.bind("<KeyPress>",keypress)
c.bind("<KeyRelease>",keyrelease)






root.mainloop()