# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:49:56 2020

@author: saima
"""



'''num=[7,9,-3,5,-2,-8,-6,1,3]'''
num1=input()
n=num1[0]
num=num1[2::]
num=list(num.split(','))
num=[int(i) for i in num]
m=[]
for i in num:
    if(i<0):
        m.append(i)
for j in  num:
    if(j>0):
        m.append(j)
        
print(*m,sep=',')