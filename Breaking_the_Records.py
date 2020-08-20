# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:23:55 2020

@author: tejav
"""


n=int(input())
m=list(map(int,input().split()))
l=[]
l1=[]
high=m[0]
low=m[0]
for i in range(1,n):
    if(m[i]>high):
        l.append(i)
        high=m[i]
    if(m[i]<low):
        l1.append(i)
        low=m[i]
print(len(l),len(l1))