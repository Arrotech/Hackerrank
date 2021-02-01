#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    i = 0
    jumpCount = 0
    n = len(c)
    while i < n-1:
        if i+2 < n and c[i+2]==0:
            jumpCount+=1
            i+=2
        elif i+1 < n and c[i+1]==0:
            jumpCount+=1
            i+=1
    return jumpCount
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
