from tkinter import *
from PIL import ImageTk, Image

w=600
h=400
win_score=0
lose_score=0
root=Tk()
root.geometry("{}x{}".format(w,h))
#frame_______________________
frame_main=Frame(root,bg="#fff582",width=w,height=h)
frame_main.pack()
frame_choice=Frame(root,bg="#fff582",width=w,height=h)
frame_play_one=Frame(root,bg="#fff582",width=w,height=h)
#frame_play_one.pack()
#frame_choice.pack()
# main-------------------------------
#___________________________________________
def play_butt():
    frame_main.pack_forget()
    frame_choice.pack()



play_but=Button(frame_main,text="თამაშის დაწყება",height=5,width=19,bg="pink",command=play_butt)
play_but.place(relx=0.1,rely=0.1)
rules_but=Button(frame_main,text="თამაშის წესები",height=5,width=19,bg="pink")
rules_but.place(relx=0.1,rely=0.4)
static_but=Button(frame_main,text="თამაშის სტატისტიკა",height=5,width=19,bg="pink")
static_but.place(relx=0.1,rely=0.7)
img = ImageTk.PhotoImage(Image.open("Banner_TicTacToe.png"))
photo_label=Label(frame_main,image=img,bg="#fff582")
photo_label.place(relx=0.45,rely=0.1)
avtori_lab=Label(frame_main,text="ავტორის სახელი",bg="#fff582")
avtori_lab.place(relx=0.8,rely=0.9)
#_____________________________________________
#-------------------------------------------
#choice---------------------------------
#_________________________________________-

def get_main():
    frame_choice.pack_forget()
    frame_main.pack()
def one_player_button():
    frame_choice.pack_forget()
    frame_play_one.pack()
one_play_but=Button(frame_choice,text="ერთი მოთამაშე",width=20,height=5,bg="lightblue",command=one_player_button)
one_play_but.place(relx=0.15,rely=0.4)
two_play_but=Button(frame_choice,text="ორი  მოთამაშე",width=20,height=5,bg="lightblue")
two_play_but.place(relx=0.6,rely=0.4)
back_but_choice=Button(frame_choice,text="უკან",font="Arial 10",bg="red",command=get_main)
back_but_choice.place(relx=0.05,rely=0.05)

#play--------------------------
#__________ერთი მოთამაშე____________________
def get_choice():
    frame_choice.pack()
    frame_play_one.pack_forget()
lab_win=Label(frame_play_one,text="მოგება : {}".format(win_score),bg="#fff582",font="Arial 11")
lab_lose=Label(frame_play_one,text="წაგება : {}".format(lose_score),bg="#fff582",font="Arial 11")
lab_win.place(relx=0.07,rely=0.2)
lab_lose.place(relx=0.07,rely=0.25)
back_but_play=Button(frame_play_one,text="უკან",font="Arial 10",bg="red",command=get_choice)
back_but_play.place(relx=0.05,rely=0.05)






root.mainloop()
