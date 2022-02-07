n=5
for i in range(1,n-1):
	if (i==1 or i==n-2):
		print(("*"+" ")*n)
	elif i==2:
		print(("*"+" "),end="")
		print(" "*(6),"*")