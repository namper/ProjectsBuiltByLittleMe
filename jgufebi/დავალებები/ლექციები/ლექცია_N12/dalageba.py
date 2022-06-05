def dalegeba(a):
	return a[-1]


file=open('saxeli_da_gvari1.txt','r+')
monacemebi=file.readlines()
i=0
saxelebi=[]
gvarebi=[]
while i<len(monacemebi):
	if i%2==0:
		saxelebi+=[monacemebi[i][:-1]]
	else:
		gvarebi+=[monacemebi[i][:-1]]

	i+=1


saxelebi.sort(key=dalegeba)
gvarebi.sort(key=dalegeba)
for i in range(len(saxelebi)):
	file.write("{} {}  \n".format(saxelebi[i][:-2],gvarebi[i]))

'''
file=open('saxeli_da_gvari.txt','r+')
monacemebi=file.readlines()
k=0
saxelebi=[]
gvarebi=[]

for i in monacemebi:
	saxelebi+=[i.split(" ")[0]]	
	if "\n" in i.split(" ")[1]:
		gvarebi+=[i.split(" ")[1][:-1]]
	else:
		gvarebi+=[i.split(" ")[1]]
for i in saxelebi:
	if i =="alexandre" and k==0:
		k=1
		j=gvarebi.index("maruashvili")
	elif i=="davit":
		j=gvarebi.index("qebadze")
	elif i=="alexandre" and k==1:
		j=gvarebi.index("lortqifanidze")
	elif i =="saba":
		j=gvarebi.index("xuxunashvili")
	elif i=="mixeil":
		j=gvarebi.index("beriashvili")
	else:
		j=gvarebi.index("oqropiridze")
	i=saxelebi.index(i)
	
	file.write("{}  {} \n".format(saxelebi[i],gvarebi[j]))

'''


