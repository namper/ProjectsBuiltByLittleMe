from tkinter import * 
import time
root=Tk()
pos=[]
width=600
height=400
r=40
x0=30
y0=40
root.geometry("{}x{}".format(width,height))
c=Canvas(root,bg="pink",width=width,height=height)
c.pack()
ball=c.create_oval(width//2-r,height//2-r,width//2+r,height//2+r,fill="brown",outline="brown")
def app():
	global x0,y0
	pos=c.coords(ball)
	if pos[1]<=0 or pos[3]>=height:
		y0=-y0
	if pos[0]<=0 or pos[2]>=width:
		x0=-x0

	c.move(ball,x0,y0)
	root.after(20,app)





app()
root.mainloop()
