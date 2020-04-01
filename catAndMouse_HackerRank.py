def catAndMouse(x,y,z):
	catA=abs(x-z)
	catB=abs(y-z)
	if(catA==catB):
		return 'Mouse C'
	else:
		return ('Cat B' if catA>catB else 'Cat A')

q=int(input())
for i in range(q):
	x,y,z=[int(i) for i in input().split()]
	result=catAndMouse(x,y,z)
	print(result)