#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    new_list = []
    paired_list = []
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i + 1, n, 1):
            if ar[i] == ar[j]:
                visited[j] = True
                count += 1        
        new_list.append(count)
        pair = 0
        for m in new_list:
            pairs = m/2
            pair = math.trunc(pairs)
        paired_list.append(pair)
    return(sum(paired_list))
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
