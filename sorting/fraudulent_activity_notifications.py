#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    count = 0
    counter = [0]*666
    n = len(expenditure)
    for exp in expenditure[:d]:
        counter[exp]+=1
    for i in range(d, n):
        new = expenditure[i]
        old = expenditure[i-d]
        median = find_median(counter, d)
        if new >= median:
            count+=1
        if new == old:
            break
        counter[new]+=1
        counter[old]-=1
    return count

def find_median(counter, d):
    count = 0
    for i in range(666):
        count+=counter[i]
        if count > d//2:
            break
    if d%2==1:
        return 2 * i
    else:
        for left in range(i, -1, -1):
            count -= counter[left]
            if count < d//2:
                return left + i
        return 2 * i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
