S=input()
r=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,len(S)):
	if(S[i]=='0'):
		r[0]=r[0]+1
	if(S[i]=='1'):
		r[1]=r[1]+1
	if(S[i]=='2'):
		r[2]=r[2]+1
	if(S[i]=='3'):
		r[3]=r[3]+1
	if(S[i]=='4'):
		r[4]=r[4]+1
	if(S[i]=='5'):
		r[5]=r[5]+1
	if(S[i]=='6'):
		r[6]=r[6]+1
	if(S[i]=='7'):
		r[7]=r[7]+1
	if(S[i]=='8'):
		r[8]=r[8]+1
	if(S[i]=='9'):
		r[9]=r[9]+1 
for j in range(0,10):
	print('{} {}'.format(j,r[j]))