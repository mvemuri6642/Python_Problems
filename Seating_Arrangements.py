T=int(input())
for i in range(T):
	n=int(input())
	a=n%12
	if a==1:
		print(n+11,'WS')
	if a==2:
		print(n+9,'MS')
	if a==3:
		print(n+7,'AS')
	if a==4:
		print(n+5,'AS')
	if a==5:
		print(n+3,'MS')
	if a==6:
		print(n+1,'WS')
	if a==7:
		print(n-1,'WS')
	if a==8:
		print(n-3,'MS')
	if a==9:
		print(n-5,'AS')
	if a==10:
		print(n-7,'AS')
	if a==11:
		print(n-9,'MS')
	if a==0:
		print(n-11,'WS')
	