x,k=input().split()
x1=list(x)
z=int(k)
for i in range(len(x1)):
	if z>0:
		if(x1[i]!='9'):
			x1[i]='9'
			z-=1
	else:	
		break
print(''.join(x1))