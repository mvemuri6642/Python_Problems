def kangaroo(x1,x2,v1,v2):
	for n in range(10000):
		if((x1+v1)==(x2+v2)):
			return 'YES'
		x1+=v1
		x2+=v2
	return 'NO'
xv=input().split()
x1=int(xv[0])
v1=int(xv[1])
x2=int(xv[2])
v2=int(xv[3])
print(kangaroo(x1,x2,v1,v2))