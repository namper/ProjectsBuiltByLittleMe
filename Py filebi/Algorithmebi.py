#globaluri x
x=4
def name():
	global x
	x+=2
	return x
print(name())

#islower function
x=input("Enter : ")
def my_islower(str):
	for i in str :
		if "A"<=i<="Z":
			return True
	return False
print(my_islower(x))

#len fuction
while True :
	x=input("Enter : ")
	def my_len(str):
		s=0
		for i in str :
			s+=1
		return s 
	print(my_len(x))

#Find

#find
x="Mecha Python"
y="Python"
def my_find(s1,s2):
	if s2 in s1:
		i=0
		while i<len(s1) :
			if s1[i]==s2[0] and s1[i:i+len(s2)]==s2:
				return i
			i+=1
	return False
print(my_find(x,y))
