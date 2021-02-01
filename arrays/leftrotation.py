#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    
    b = a[d:]+a[:d]
    return (b)

a = [1, 2, 3, 4, 5]
d = 2
print(rotLeft(a,d))
