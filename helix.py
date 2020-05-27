def mul(a,b):
	c,d=0,0
	count=0
	for i in range(1,b//2):
		c=i*a
		for j in range(1,b+1):
			d=c/i
			if(d==b):
				break
	count=i+j
def div(a,b):
	c,d=0,0
	count=0
	for i in range(1,b+1):
		c=a/i
		for j in range(1,(b//2)+1):
			d=i*c
			count=i+j
	return count

t=int(input())
n=[input().split() for i in range(t)]
for x in n:
	y=list(x)
	a=int(y[0])
	b=int(y[1])
	p=mul(a,b)
	if(p==b):
		print(p)
	else:
		q=div(a,b)
		print(q)
	