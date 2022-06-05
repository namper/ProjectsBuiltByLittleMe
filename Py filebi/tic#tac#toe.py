a={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}
gasulebi=[]
mogeba=((1,2,3),(2,5,8),(4,5,6),(7,8,9),(1,4,7),(3,6,9),(1,5,9),(3,5,7))
p=1
def cxrili(a):
    print("-------------")
    print("|",a["1"],"|",a["2"],"|",a["3"],"|")
    print("-------------")
    print("|",a["4"],"|",a["5"],"|",a["6"],"|")
    print("-------------")
    print("|",a["7"],"|",a["8"],"|",a["9"],"|")
    print("-------------")
 
def in_x(gasulebi):
    x=input("x-is svlaa : ")
    if not(x in gasulebi):
        gasulebi+=[x]
        a[x]="x"
    else:
        print("adgili dakavebulia")
        in_x(gasulebi)
def in_o(gasulebi):
    x=input("o-is svlaa : ")
    if not(x in gasulebi):
        gasulebi+=[x]
        a[x]="o"
    else:
        print("adgili dakavebulia")
        in_o(gasulebi)
def win(mogeba):
    global p
   
    for i in mogeba:
        count_x=0
        count_o=0
        for j in i:
           
            if "x"==a[str(j)]:
                count_x+=1
               
                if count_x==3:
                    p=0
                    return "win x"
            elif "o"==a[str(j)]:
                count_o+=1
                if count_o==3:
                    p=0
                    return "win o"
    return ""
 
cxrili(a)
i=1
while i<=9:
    in_x(gasulebi)
    cxrili(a)
    print(win(mogeba))
    if p==0:
        break
    if i==9:
        print("draw !!!!!!")
        break
    i+=1
   
    in_o(gasulebi)
    cxrili(a)
    print(win(mogeba))
    if p==0:
        break
    i+=1
