first = "croatia.txt"
second = "singapore.txt"
gasulebi=[]
saerto=[]
count1=count2=0
croatia=open(first,'r')
cro=croatia.read().split(" ")
croatia.close()
singapore=open(second,"r")
sing=singapore.read().split(" ")
singapore.close()
def dalegaba(a):
    return a[-3:]


for i in cro:
    if i in gasulebi:
        continue
    else:

        gasulebi+=[i]
    for j in sing:

        if i==j:
            count1=cro.count(i)
            count2=sing.count(i)
            saerto+=[i+"      |||||||| croatia : {} ------ singapure :{}  jami=   {}\n".format(count1,count2,count2+count1)]
            break

print(saerto)
saerto.sort(key=dalegaba)
file=open("shedegebi.txt","w")
file.writelines(saerto)
file.close()

