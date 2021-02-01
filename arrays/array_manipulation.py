#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    
    # initialize the array with zeros
    arr = [0] * (n+2)
    
    # perform the queries
    for a,b,k in queries:
        
        # update starting index
        arr[a] += k
        
        # update final index
        arr[b+1] -= k
        
    # find maximum value from the array
    maximum = temp = 0
    for value in arr:
        temp += value
        maximum = max(maximum, temp)
        
    return maximum
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
