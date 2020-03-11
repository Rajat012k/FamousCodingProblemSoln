#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

# Complete the biggerIsGreater function below.
def biggerIsGreater(num):
    length=len(num)
    pivot=-1
    for i in range(0,length):
        if(num[length-i-1]<=num[length-i-2]):
            pass
        else:
            pivot=length-i-2
            print(pivot)
            break
    if(pivot==-1):
        return "no answer"
    print(num[pivot])
    suffix=num[pivot+1:]
    suffix=list(suffix)
    print(suffix)
    num=list(num)
    for i in range (0,len(suffix)):
        if(num[pivot]<suffix[len(suffix)-i-1]):
            num[pivot],suffix[len(suffix)-i-1]=suffix[len(suffix)-i-1],num[pivot]
            break
    print(suffix)
    
    suffix=suffix[::-1]
    result=num[:pivot+1]+suffix
    num="".join(num)
    res=''.join(result)
    if(res>num or res==num):
        return "no answer"
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
