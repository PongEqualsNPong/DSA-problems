#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    sorted=[]
    for i in range(len(arr)):
        sorted.append(list())
    j= len(arr)//2
    for i in range(j):
        arr[i][1]= '-'
    for e in arr:
        i = int(e[0])
        sorted[i].append(e[1])
    final= []
    for e in sorted:
        for ee in e:
            final.append(ee)
    print(*final)
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
