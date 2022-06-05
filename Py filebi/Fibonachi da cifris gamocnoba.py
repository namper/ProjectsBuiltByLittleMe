#fibo
def fibo(n):
	if n<2:
		return n
	return (fibo(n-1)+fibo(n-2))
print(fibo(n=int(input("Qraw: "))))

#cotne mechanics 2n
def isaac(n):
	if n==1:
		return 2
	else:
		return 2*n+isaac(n-1)
print(isaac(n=int(input("Lraw: "))))

#cotne mechanics 2n-1
def isaac(n):
	if n==1:
		return 2
	else:
		return 2*(n-1)+isaac(n-1)
print(isaac(n=int(input("L-1raw: "))))


#cifris gamocnoba 7 cdashi
from random import randint
print("Kompiuteri ecdeba pythonis gamokenebit gamoicnos tkveni archeuli ricxvs")
archeuli=int(input("Airchiet Nebismieri ricxvi 1-100: "))
def shemocmeba():
	if archeuli<1 or archeuli>100:
		print("Kompiuteri ver shedzlebs tkveni ricxvis gamocnobas tu tkveni archeuli ricxvi arikenba 1-dan 100-mde")
	else:
		print("Pythons araferi gamorcheba...")
shemocmeba()
gamocnoba=randint(1,100)
print("Kompiuterma scada: "+str(gamocnoba))
def programa():
	global gamocnoba
	patara = 1
	didi = 100
	gamocnoba = 50
	while gamocnoba != archeuli:
		gamocnoba = (patara+didi)//2
		print("Kompiuterma scada ",str(gamocnoba))
		if gamocnoba > archeuli:
			didi = gamocnoba
		elif gamocnoba < archeuli:
			patara= gamocnoba + 1
	print("Kompiuterma scada ", str(gamocnoba), " da es daemtxva tkvens archevans :"+str(archeuli))
programa()

#chafikrebuli
from random import randint
print("................................................................................Pythonis es programa shedzlebs tkven mier chafikrebuli ricxis gamocnobas tkven shegidzliat chaifikrot 1 idan 100 mde nebismieri ricxvi , kuradghebit upasuxet kompiuteris shekitxvebs shegidzliat gamoikenot ki(roca programa gamoicnobs ricxvs),dabla(roca programis archeuli ricxvi aghemateba tkvensas ),da maghla(roca programis archeuli ricxvi tkven chafikrebul ricxvze pataraa) carmatebebi!!")
patara=1
didi=100
user=""
gamocnoba=randint(patara,didi)
while user != "ki":
	print("chafikrebuli ricxvi aris "+str(gamocnoba)+" ?")
	user=input()
	if user=="dabla":
		didi=gamocnoba-1
		gamocnoba=randint(patara,didi)
	elif user=="maghla":
		patara=gamocnoba+1
		gamocnoba=randint(patara,didi)
	elif user=="ki":
		print("Pythonit jadokrobac shesadzlebelia")
	else:
		print("mxolod dabla maghla da ki keywordebia shesadzlebeli gamoikenot programashi")
