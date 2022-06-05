def dalegeba(a):
	return int(a[-3:-1])
file=open('file_N1.txt','r')
monacemebi=file.readlines()
print(monacemebi)

file.close()
monacemebi.sort(key=dalegeba)
file2=open('file_N2.txt','w')
file2.writelines(monacemebi)
file2.close()
