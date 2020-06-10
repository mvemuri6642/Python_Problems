# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:43:35 2020

@author: saima
"""


def BinarySearch(arr,low,high,key):
    if(high<low):
        return -1
    mid=low+((high-low)//2)
    if key==arr[mid]:
        return mid
    elif(key<arr[mid]):
        return BinarySearch(arr, low, mid-1, key)
    else:
        return BinarySearch(arr, mid+1, high, key)
    
    
arr=[1,3,5,7,9,10]
n=len(arr)
key=4
print(BinarySearch(arr, 0, n-1, key))