#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    i=len(c)-1
    sum=0
    m=1
    
    while i >=0:
        j=k
        while j >0 and i>=0:
            sum+= m*c[i]
            print(i)
            i-=1
            j-=1
        m+=1
    return sum
                
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
