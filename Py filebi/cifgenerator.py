from turtle import*
t=Pen()
t.color("green")
bgcolor("black")
def zero():
    t.left(90)
    t.fd(15)
    t.left(90)
    t.fd(10)
    t.left(90)
    t.fd(15)
    t.left(90)
    t.fd(10)
    t.up()
    t.setheading(0)
    t.fd(20)
    t.pd()
def one():
    t.pu()
    t.left(180)
    t.fd(15)
    t.pd()
    t.right(90)
    t.fd(15)
    t.left(160)
    t.fd(7.5)
    t.up()
    t.bk(7.5)
    t.setheading(0)
    t.right(90)
    t.fd(15)
    t.setheading(0)
    t.fd(20)
    t.pd()
def two():
    t.left(180)
    t.fd(15)
    t.right(90)
    t.fd(5)
    t.right(90)
    t.fd(15)
    t.left(90)
    t.fd(10)
    t.left(90)
    t.fd(15)
    t.left(90)
    t.fd(5)
    t.pu()
    t.fd(10)
    t.setheading(0)
    t.fd(35)
    t.pd()
def three():
    t.left(90)
    t.fd(15)
    t.left(90)
    t.fd(15)
    t.left(90)
    t.pu()
    t.fd(7.5)
    t.left(90)
    t.fd(5)
    t.pd()
    t.fd(10)
    t.right(90)
    t.fd(7.5)
    t.right(90)
    t.fd(15)
    t.setheading(0)
    t.pu()
    t.fd(35)
    t.pd()
def four():
    t.pu()
    t.left(180)
    t.fd(5)
    t.pd()
    t.right(90)
    t.fd(15)
    t.left(135)
    t.fd(15)
    t.setheading(0)
    t.fd(12)
    t.pu()
    t.right(90)
    t.fd(5)
    t.setheading(0)
    t.fd(20)
    t.pd()
def five():
    t.pu()
    t.left(180)
    t.fd(15)
    t.pd()
    t.bk(10)
    t.right(90)
    t.fd(7)
    t.left(90)
    t.fd(10)
    t.right(90)
    t.fd(8)
    t.right(90)
    t.fd(10)
    t.pu()
    t.bk(15)
    t.right(90)
    t.fd(12)
    t.pd()
    t.fd(4)
    t.setheading(0)
    t.pu()
    t.fd(35)
    t.pd()
def six():
    t.left(180)
    t.fd(15)
    t.right(90)
    t.fd(15)
    t.right(90)
    t.fd(15)
    t.bk(15)
    t.right(90)
    t.fd(10)
    t.left(90)
    t.fd(15)
    t.right(90)
    t.fd(5)
    t.setheading(0)
    t.up()
    t.fd(20)
    t.pd()
def seven():
    t.up()
    t.left(180)
    t.fd(15)
    t.pd()
    t.right(135)
    t.fd(21)
    t.left(135)
    t.fd(15)
    t.pu()
    t.bk(15)
    t.left(90)
    t.fd(15)
    t.setheading(0)
    t.fd(15)
    t.pd()
def eight():
    t.left(90)
    t.fd(15)
    t.left(90)
    t.fd(10)
    t.left(90)
    t.fd(7.5)
    t.left(90)
    t.fd(10)
    t.bk(10)
    t.right(90)
    t.fd(7.5)
    t.setheading(0)
    t.fd(10)
    t.up()
    t.fd(20)
    t.pd()
def nine():
    t.left(90)
    t.fd(15)
    t.left(90)
    t.fd(10)
    t.left(90)
    t.fd(5)
    t.left(90)
    t.fd(10)
    t.bk(10)
    t.right(90)
    t.up()
    t.fd(7)
    t.pd()
    t.fd(3)
    t.setheading(0)
    t.fd(10)
    t.pu()
    t.fd(20)
    t.pd()
user=input("a: ")
for i in range(len(user)):
    if user[i]=="1":
        one()

    elif user[i]=="2":
        two()

    elif user[i]=="3":
        three()

    elif user[i]=="4":
        four()

    elif user[i]=="5":
        five()

    elif user[i]=="6":
        six()

    elif user[i]=="7":
        seven()

    elif user[i]=="8":
        eight()

    elif user[i]=="9":
        nine()

    elif user[i]=="0":
        zero()

    else:
        print("Hmm rogorchans tkven miutitet stringi cifrebis magivrad")





