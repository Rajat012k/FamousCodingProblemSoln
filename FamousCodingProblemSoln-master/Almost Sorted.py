#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    pvz=0
    sor=sorted(arr)
    for i in range(len(arr)):
        if(arr[i]==sor[i]):
            continue
        else:
            pvz=i
            break
    #print(pvz)
    realvalue=sor[pvz]
    realIndex=arr.index(realvalue)
    #print(realvalue)
    #print(realIndex)
    if(1):
        arr[pvz],arr[realIndex]=arr[realIndex],arr[pvz]
        if(arr==sor):
            print("yes")
            print("swap",pvz+1,realIndex+1)
            return
        else:
            arr[realIndex],arr[pvz]=arr[pvz],arr[realIndex]
    if(1):
        sub=arr[pvz:realIndex+1]
        sub=sub[::-1]
        lol=arr[:pvz]+sub+arr[realIndex+1:]
        if(lol==sor):
            print("yes")
            print("reverse",pvz+1,realIndex+1)
            return
    print("no")
    return

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
