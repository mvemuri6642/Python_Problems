import operator
n=int(input())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
m=int(input())
l=[]
for i in range(n):
    l.append([val[i],wt[i],val[i]*1.0/wt[i]])
l=sorted(l,reverse=True,key=operator.itemgetter(2))
max=0
frac=0
for i in range(n):
    if m>0 and l[i][1]<m:
        m-=l[i][1]
        max+=l[i][0]
    else:
        frac=i
        break
if m>0:
    max+=m*l[frac][0]/l[frac][1]
print(max)