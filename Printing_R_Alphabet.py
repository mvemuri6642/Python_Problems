# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:36:43 2020

@author: tejav
"""

print()
for i in range(7):
    for j in range(5):
        if j==0 or (j==4 and (i!=0 and i!=3)) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
             