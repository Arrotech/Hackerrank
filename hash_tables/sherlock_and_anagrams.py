#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n = len(s)
    res=0
    for i in range(1,n): #length of the substring
        d={}
        for j in range(n-i+1):
            subs = ''.join(sorted(s[j:j+i]))
            if subs not in d:
                d[subs]=1
            else:
                d[subs]+=1
            
            res +=d[subs]-1
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
