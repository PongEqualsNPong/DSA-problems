#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chiefHopper function below.
def chiefHopper(arr):
    a=0
    for i in range (len(arr)):
        a=math.ceil((a+arr[-1-i])/2)
    return a 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
