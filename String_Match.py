# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:50:51 2020

@author: saima
"""


s=['0']*10
a,b=input().split()
count=0
if(len(a)<len(b)):
    a,b=b,a
for i in range(len(a)):
    if(a[i]==b[i]):
        s[i]='1'
        count+=1
for j in s:
    print(j,end='')
print('',count)