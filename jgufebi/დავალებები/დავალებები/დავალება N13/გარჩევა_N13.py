from tkinter import *
root=Tk()
root.geometry("460x320")
root.resizable(False,False)
c=Canvas(root,width=460,height=320,bg="black")
c.pack()
#ukraina
c.create_rectangle(20,20,210,80,fill="blue",outline="blue")
c.create_rectangle(20,80,210,140,fill="yellow",outline="yellow")
#iaponia
c.create_rectangle(20,180,210,300,fill="white")
r=32
c.create_oval(115-r,240-r,115+r,240+r,fill="red",outline="red")
#italia
c.create_rectangle(250,180,313,300,fill="green",outline="green")
c.create_rectangle(313,180,377,300,fill="white",outline="white")
c.create_rectangle(377,180,440,300,fill="red",outline="red")
#saqartvelo
c.create_rectangle(250,20,440,140,fill="white",outline="white")
c.create_line(250,80,440,80,fill="red",width=17)
c.create_line(345,20,345,140,fill="red",width=17)

root.mainloop()