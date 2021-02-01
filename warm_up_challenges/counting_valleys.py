#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valleyCount = 0
    currentStep = 0
    for i in range(steps):
        previousStep = currentStep
        if path[i] == 'U':
            currentStep+=1
        if path[i] == 'D':
            currentStep-=1
        if currentStep == 0 and i!=0:
            if previousStep==-1:
                valleyCount+=1
    return valleyCount
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
