# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:20:41 2020

@author: mvemuri6642
"""


def quickSort(arr,lb,ub):
    if(lb<ub):
        loc=partition(arr,lb,ub)
        quickSort(arr,lb,loc-1)
        quickSort(arr,loc+1,ub)
        

def partition(arr,lb,ub):
    pivot=arr[lb]
    start,end=lb+1,ub
    while(start<end):
        while(arr[start]<=pivot and start<ub):
            start+=1
        while(arr[end]>pivot):
            end-=1
        if(start<end):
            arr[start],arr[end]=arr[end],arr[start]
    arr[lb],arr[end]=arr[end],arr[lb]
    return end

arr=list(map(int,input().split()))
n=len(arr)
quickSort(arr,0,n-1)
print(arr)