# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:05:50 2020

@author: saima
"""

a=input()
b=input()
m=len(a)
n=len(b)
c=[[0]*(n+1) for i in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if(i==0):
            c[i][j]=j
        if(j==0):
            c[i][j]=i
        if(a[i-1]==b[j-1]):
            c[i][j]=c[i-1][j-1]
        else:
            c[i][j]=1+min(c[i][j-1],c[i-1][j],c[i-1][j-1])
            
print(c[i][j])
