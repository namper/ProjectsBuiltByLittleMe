class vulcano:
	def __init__(self,saxeli,simagle):
		self.saxeli=saxeli
		self.simagle=simagle
	def mbechdavi(self):

		print(self.saxeli)	



def dalageba(a):
	return a.simagle


saxelebi=["krakato","etna","pele"]
simagleebi=[813,3350,1397]
vulcanebi=[]

axali_vulkani=vulcano("qebadze",150)

for i in range(len(saxelebi)):
	vulcanebi.append(vulcano(saxelebi[i],simagleebi[i]))

vulcanebi.sort(key=dalageba,reverse=True)

for i in vulcanebi:
 	print(i.simagle)








