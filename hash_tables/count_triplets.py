#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    d1 = defaultdict(int) #right side
    d2 = defaultdict(int) #left side
    c = 0
    for i in reversed(arr):
        if i * r in d2:
            c+=d2[i*r]
        if i * r in d1:
            d2[i]+=d1[i*r]
        d1[i]+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
