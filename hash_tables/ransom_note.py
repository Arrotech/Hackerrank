#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    flag = True
    c1=Counter(magazine)
    c2=Counter(note)
    if c2-c1=={}:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
