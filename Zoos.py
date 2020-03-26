i=input()
cz=i.split('z')
print(cz)
co=i.split('o')
print(co)
y=len(cz[-1])
print(y)
x=len(co[0])
print(x)
if(2*x==y):
	print('Yes')
else:
	print('No')
	
"""
Output
zzzoooooo
['', '', '', 'oooooo']
['zzz', '', '', '', '', '', '']
6
3
Yes

[Program finished]
"""