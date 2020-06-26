# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:21:53 2020

@author: saima
"""


l=[10,68,97,9,21,12]
n=6
for i in range(0,n):
    for j in range(i+1,n):
        a=int(str(l[i])+str(l[j]))
        b=int(str(l[j])+str(l[i]))
        if(a<b):
            l[i],l[j]=l[j],l[i]
            
for m in l:
    print(m,end='')