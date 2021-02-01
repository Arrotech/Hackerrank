#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    arr=sorted(expenditure[:d])
    m=d//2
    c=0
    def med(arr,d,m):
        if d % 2 == 0:
            return sum(arr[m - 1:m + 1]) / 2
        else :
            return arr[int(m)]    
    for i in range(d,n):
        if expenditure[i] >= 2*med(arr,d,m):        
            c+=1
        del arr[bisect.bisect_left(arr,expenditure[i-d])]
        bisect.insort(arr,expenditure[i])
    return c 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
