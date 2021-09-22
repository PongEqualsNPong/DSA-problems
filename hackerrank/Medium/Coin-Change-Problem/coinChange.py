#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    
    table = []

    for row in range(len(c) +1):
        table.append([1])
        for col in range(n):
            table[row].append(0)
    for row in range(1, len(c) +1):
        for col in range(1, n +1):
            if col - c[row -1] < 0:
                table[row][col]= table[row-1][col]
            else:
                table[row][col] = table[row][col-c[row-1]] + table[row-1][col]    
    for row in table:
        print(*row)
    
    return table[len(c)][n]
            
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
