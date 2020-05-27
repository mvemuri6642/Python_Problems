def betw(a,b,x):
	for t in a:
		if(x%t!=0):
			return False
	for t in b:
		if(t%x!=0):
			return False
	return True

pq=input().split()
count=0
p,q=(int(pq[0]),int(pq[1]))
a=[int(i) for i in input().split()]
b=[int(j) for j in input().split()]
for x in range(max(a),min(b)+1):
	if betw(a,b,x):
		count+=1
print(count)