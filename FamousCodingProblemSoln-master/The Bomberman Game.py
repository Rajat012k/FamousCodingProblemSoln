#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bomberMan function below.
def createGrid(r, c,previousgrid):
    nexti = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            current_cell = previousgrid[i][j]
            if current_cell == 'O':
                nexti[i][j] = '.'
                if i - 1 >= 0:
                    nexti[i - 1][j] = '.'
                if i + 1 <= r - 1:
                    nexti[i + 1][j] = '.'
                if j - 1 >= 0:
                    nexti[i][j - 1] = '.'
                if j + 1 <= c - 1:
                    nexti[i][j + 1] = '.'
    return nexti

def bomberMan(r,c,n, initial_grid):
    firstdec = createGrid(r, c, initial_grid)
    if n % 2 == 0:
        return [['O'] * c for _ in range(r)]
    elif n < 4:
        if n == 1:
            return initial_grid 
        else:
            return firstdec
    else:
        secdec = createGrid(r,c,firstdec)
        if n % 4 == 1:
            return secdec 
        else:
            return firstdec
    
            
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(r,c,n, grid)
    dp=["".join(i) for i in result]
    fptr.write('\n'.join(dp))
    fptr.write('\n')

    fptr.close()
