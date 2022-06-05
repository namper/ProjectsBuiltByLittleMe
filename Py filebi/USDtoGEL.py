from tkinter import *
def kursi():
    x=dentry.get()
    k=float(x)*2.49
    converted.configure(text=str(k))
def lariskursi():
    x=lentry.get()
    k=float(x)/2.49
    converted1.configure(text=str(k))
root = Tk()
root.geometry("800x600")
'''
def fun():
    content = entry.get()
    print(content)

    

root.geometry("800x600+300+200")
lab=Label(root, text='label', fg='black')
entry=Entry(root,bd=5)
but=Button(root,text='Submit',command=fun)
lab.pack()
entry.pack()
but.pack()
root.mainloop()
'''
CheckVar1 = IntVar()
CheckVar2 = IntVar()

C1 = Checkbutton(root, text = "USD TO GEL", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 
                 width = 20, )
C1.grid(row=1,column=1)
C2 = Checkbutton(root, text = "GEL TO USD", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2.grid(row=2,column=1)
if CheckVar1.get()==1:
    #Dolaris convertacia larshi
    lab=Label(root,text='USD')
    lab.grid(row=1,column=0)
    dentry=Entry(root,bd=2)
    lab1=Label(root,text='GEL')
    lab1.grid(row=1,column=2)
    dentry.grid(row=1,column=1,rowspan=1)
    #submit
    but=Button(root,text='Submit',command=kursi)
    but.grid(row=2,column=1)
    #converted
    converted=Label(root,text="0.00")
    converted.grid(row=1,column=3,)
elif CheckVar2.get()==1:
    #Laris convertacia dolarshi
    lab1=Label(root,text='GEL')
    lab1.grid(row=3,column=0)
    lentry=Entry(root,bd=2)
    lab1=Label(root,text='USD')
    lab1.grid(row=3,column=2)
    lentry.grid(row=3,column=1,rowspan=1)
    #submit
    but1=Button(root,text='Submit',command=lariskursi)
    but1.grid(row=4,column=1)
    #converted
    converted1=Label(root,text="0.00")
    converted1.grid(row=3,column=3)

root.mainloop()

