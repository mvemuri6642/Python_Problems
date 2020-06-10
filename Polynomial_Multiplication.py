# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:43:03 2020

@author: mvemuri6642
"""
def poly(a,b):
    m=len(a)
    n=len(b)
    prod=[0]*(m+n-1)
    for i in range(m):
        for j in range(n):
            prod[i+j]+=a[i]*b[j]
    return prod
def printpoly(prod):
    for i in range(len(prod)):
        print(prod[i],end='')
        if(i!=0):
            print('x^',i,end='')
        if(i!=len(prod)-1):
            print(' + ',end='')
            
a=[5, 0, 10, 6]
b=[1, 2, 4]
prod=poly(a,b)
printpoly(prod)

