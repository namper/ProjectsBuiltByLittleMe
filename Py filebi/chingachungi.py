import random
#welcome
print("Welcome to most popular game rock paper scissor")
while True:
	
	#players
	x=input("choose wisely rock paper or scissor? : ")
	lst=["rock","paper","scissor"]
	y=random.choice(lst)
	#print choice
	print("computer chooose :",y)
	print("user chooose : ",x)
	z = y+x;
	if z == "paperrock" or z== "scissorpaper" or z== "rockscissor" :
		
		print("computer won !!!")
	elif y == x:
		print("draw!")
	else:
		print("user won !!!")

