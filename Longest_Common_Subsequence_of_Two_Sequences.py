# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 18:08:10 2020

@author: saima
"""
import math
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=[[0]*(m+1) for i in range(n+1)]
for i in range(n):
    for j in range(m):
        if(a[i]==b[j]):
            c[i][j]=1+c[i-1][j-1]
        else:
            c[i][j]=max(c[i-1][j],c[i][j-1])
print(c[i][j])
    