def move(m,x,p,q):
	for i in m[p:x]:
		if(i!='.'):
			return True
	for i in m[x+1:q+1]:
		if(i!='.'):
			return True
	else:
		return False

t=int(input())
h=[input() for i in range(t)]
for o in h:
	r=list(o)
	m=r[:]
	for i in range(len(r)):
		if(r[i]!='.'):
			p=i-int(r[i])
			q=i+int(r[i])
			if(p<0):
				p=0
			if(q>=len(r)):
				q=len(r)-1
			if move(m,i,p,q):
				print('unsafe')
				break
			else:
				m[p:q+1]=['1']*len(m[p:q+1])
	else:
		print('safe')
