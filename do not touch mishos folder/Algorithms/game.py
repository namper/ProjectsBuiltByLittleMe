#GAME
from turtle import*
import math 
from random import randint
global x
x=2



#SCREEN
screensize(300,300)




#BORDER
border=Pen()
border.color("Blue")
border.width(12)
border.pu()
border.setpos(-250,-250)
border.pd()
for i in range(4):
    border.fd(450)
    border.left(90)
border.hideturtle()



#Player
p=Pen()
p.up()
p.shape("triangle")
p.color("orange")
p.setheading(90)
p.setpos(-20,-20)


#FUNCTIONS

#move
def Left():
    p.left(90)
def Right():
    p.right(90)

    
#Movement
listen()
onkey(Left,"a")
onkey(Right,'d')


#Goal
goal=Turtle()
goal.speed(1)
goal.shape("square")
goal.color("red")
goal.pu()
goal.setpos(randint(-220,180),randint(-220,180))




#LOOP
def loop():
    gameexit=False
    while not gameexit:
        #moving
        p.fd(x)
        #border checking
        if p.xcor()>190 or p.xcor()<-240:
            gameexit= True
        if p.ycor()>190 or p.ycor()<-240:
            gameexit= True
        #distance checking
        d=math.sqrt(math.pow(p.xcor()-goal.xcor(),2)+ math.pow(p.ycor()-goal.ycor(),2))
        if d<=20:
            goal.setpos(randint(-220,180),randint(-220,180))
loop()


exit()
mainloop()
