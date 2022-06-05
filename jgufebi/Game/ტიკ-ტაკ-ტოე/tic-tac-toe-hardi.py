a={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
insert1=[]
def PrintTable():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("-------------")
    print("|",a["1"],"|",a["2"],"|",a["3"],"|")
    print("-------------")
    print("|",a["4"],"|",a["5"],"|",a["6"],"|")
    print("-------------")
    print("|",a["7"],"|",a["8"],"|",a["9"],"|")
    print("-------------")
    
def insert():
    i=0
    while True:
        insertx(insert1)
        PrintTable()
        winx=win_X()
        i+=1
        if winx==9:
            break
        if i==9:
            print("draw !!!!!!!!!!!!!!")
            break

        inserto(insert1)
        PrintTable()
        wino=win_O()
        i+=1
        if wino==9:
            break

def insertx(insert1):
    b=input("enter x : ")
    try:
        if not(b in insert1):
            insert1+=[b]
            a[b]="X"
        else:
            1/0
    except ZeroDivisionError :
        print("This place is already valued")
        insertx(insert1)


import random

def inserto(insert1):
    if a["1"]==a["2"]=="O" and a["3"]=="3":
        q="3"
    elif a["3"]==a["2"]=="O" and a["1"]=="1":
        q="1"
    elif a["1"]==a["3"]=="O" and a["2"]=="2":
        q="2"
    elif a["4"]==a["5"]=="O" and a["6"]=="6":
        q="6"
    elif a["4"]==a["6"]=="O" and a["5"]=="5":
        q="5"
    elif a["5"]==a["6"]=="O" and a["4"]=="4":
        q="4"
    elif a["7"]==a["8"]=="O" and a["9"]=="9":
        q="9"
    elif a["7"]==a["9"]=="O" and a["8"]=="8":
        q="8"
    elif a["8"]==a["9"]=="O" and a["7"]=="7":
        q="7"
    elif a["1"]==a["4"]=="O" and a["7"]=="7":
        q="7"
    elif a["1"]==a["7"]=="O" and a["4"]=="4":
        q="4"
    elif a["4"]==a["7"]=="O" and a["1"]=="1":
        q="1"
    elif a["5"]==a["2"]=="O" and a["8"]=="8":
        q="8"
    elif a["8"]==a["2"]=="O" and a["5"]=="5":
        q="5"
    elif a["5"]==a["8"]=="O" and a["2"]=="2":
        q="2"
    elif a["3"]==a["6"]=="O" and a["9"]=="9":
        q="9"
    elif a["3"]==a["9"]=="O" and a["6"]=="6":
        q="6"
    elif a["9"]==a["6"]=="O" and a["3"]=="3":
        q="3"
    elif a["1"]==a["5"]=="O" and a["9"]=="9":
        q="9"
    elif a["1"]==a["9"]=="O" and a["5"]=="5":
        q="5"
    elif a["5"]==a["9"]=="O" and a["1"]=="1":
        q="1"
    elif a["3"]==a["5"]=="O" and a["7"]=="7":
        q="7"
    elif a["3"]==a["7"]=="O" and a["5"]=="5":
        q="5"
    elif a["5"]==a["7"]=="O" and a["3"]=="3":
        q="3"
    elif a["1"]==a["2"]=="X" and a["3"]=="3":
        q="3"
    elif a["3"]==a["2"]=="X" and a["1"]=="1":
        q="1"
    elif a["1"]==a["3"]=="X" and a["2"]=="2":
        q="2"
    elif a["4"]==a["5"]=="X" and a["6"]=="6":
        q="6"
    elif a["4"]==a["6"]=="X" and a["5"]=="5":
        q="5"
    elif a["5"]==a["6"]=="X" and a["4"]=="4":
        q="4"
    elif a["7"]==a["8"]=="X" and a["9"]=="9":
        q="9"
    elif a["7"]==a["9"]=="X" and a["8"]=="8":
        q="8"
    elif a["8"]==a["9"]=="X" and a["7"]=="7":
        q="7"
    elif a["1"]==a["4"]=="X" and a["7"]=="7":
        q="7"
    elif a["1"]==a["7"]=="X" and a["4"]=="4":
        q="4"
    elif a["4"]==a["7"]=="X" and a["1"]=="1":
        q="1"
    elif a["5"]==a["2"]=="X" and a["8"]=="8":
        q="8"
    elif a["8"]==a["2"]=="X" and a["5"]=="5":
        q="5"
    elif a["5"]==a["8"]=="X" and a["2"]=="2":
        q="2"
    elif a["3"]==a["6"]=="X" and a["9"]=="9":
        q="9"
    elif a["3"]==a["9"]=="X" and a["6"]=="6":
        q="6"
    elif a["9"]==a["6"]=="X" and a["3"]=="3":
        q="3"
    elif a["1"]==a["5"]=="X" and a["9"]=="9":
        q="9"
    elif a["1"]==a["9"]=="X" and a["5"]=="5":
        q="5"
    elif a["5"]==a["9"]=="X" and a["1"]=="1":
        q="1"
    elif a["3"]==a["5"]=="X" and a["7"]=="7":
        q="7"
    elif a["3"]==a["7"]=="X" and a["5"]=="5":
        q="5"
    elif a["5"]==a["7"]=="X" and a["3"]=="3":
        q="3"
    else: q=str(random.randint(1,9))
    try:
        if not(q in insert1):
            insert1+=[q]
            a[q]="O"
            print("compiuter choose :",q)
        else:
            1/0
    except ZeroDivisionError:
        inserto(insert1)
        


        
       
def win_X():
    if a["1"]==a["2"]==a["3"] or a["4"]==a["5"]==a["6"] or a["7"]==a["8"]==a["9"] or a["1"]==a["4"]==a["7"] or a["2"]==a["5"]==a["8"] or a["3"]==a["6"]==a["9"] or a["1"]==a["5"]==a["9"] or a["3"]==a["5"]==a["7"]:
        print("Win X !!!!!!!!!!!!!!")
        return 9
def win_O():
    if a["1"]==a["2"]==a["3"] or a["4"]==a["5"]==a["6"] or a["7"]==a["8"]==a["9"] or a["1"]==a["4"]==a["7"] or a["2"]==a["5"]==a["8"] or a["3"]==a["6"]==a["9"] or a["1"]==a["5"]==a["9"] or a["3"]==a["5"]==a["7"]:
        print("Win O !!!!!!!!!!!!!!")
        return 9



PrintTable()
insert()
   
