# You will be given a square chess board with one queen and a number of obstacles placed on it. Determine how many squares the queen can attack.

# A queen is standing on an  chessboard. The chess board's rows are numbered from  to , going from bottom to top. Its columns are numbered from  to , going from left to right. Each square is referenced by a tuple, , describing the row, , and column, , where the square is located.

# The queen is standing at position . In a single move, she can attack any square in any of the eight directions (left, right, up, down, and the four diagonals). In the diagram below, the green circles denote all the cells the queen can attack from :

# image

# There are obstacles on the chessboard, each preventing the queen from attacking any square beyond it on that path. For example, an obstacle at location  in the diagram above prevents the queen from attacking cells , , and :

# image

# Given the queen's position and the locations of all the obstacles, find and print the number of squares the queen can attack from her position at . In the board above, there are  such squares.

# Function Description

# Complete the queensAttack function in the editor below. It should return an integer that describes the number of squares the queen can attack.

# queensAttack has the following parameters:
# - n: an integer, the number of rows and columns in the board
# - k: an integer, the number of obstacles on the board
# - r_q: integer, the row number of the queen's position
# - c_q: integer, the column number of the queen's position
# - obstacles: a two dimensional array of integers where each element is an array of  integers, the row and column of an obstacle



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, q_r,q_c, obstacles):
    bottom=n-q_r
    up=q_r-1
    left=q_c-1
    right=n-q_c
    upleft=min(q_r,q_c)-1
    upright=min(q_r-1,n-q_c)
    bottomleft=min(n-q_r,q_c-1)
    bottomright=min(n-q_r,n-q_c)
    for i in obstacles:
        if(i[1]==q_c and i[0]>q_r):
            bottom=min(bottom,i[0]-q_r-1)
        if(i[1]==q_c and i[0]<q_r):
            up=min(up,q_r-i[0]-1)
        if(i[0]==q_r and i[1]<q_c):
            left=min(left,q_c-i[1]-1)
        if(i[0]==q_r and i[1]>q_c):
            right=min(right,i[1]-q_c-1)
        if(i[0]<q_r and i[1]<q_c) and (q_r-i[0]==q_c-i[1]):
            upleft=min(upleft,q_r-i[0]-1)
        if(i[0]>q_r and i[1]<q_c) and (i[0]-q_r==q_c-i[1]):
            bottomleft=min(bottomleft,i[0]-q_r-1)
        if(i[0]<q_r and i[1]>q_c) and (q_r-i[0]==i[1]-q_c):
            upright=min(upright,q_r-i[0]-1)
        if(i[0]>q_r and i[1]>q_c) and (i[0]-q_r==i[1]-q_c):
            bottomright=min(bottomright,i[0]-q_r-1)
        

    su=up+bottom+left+right+upleft+bottomleft+upright+bottomright
    return su
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
