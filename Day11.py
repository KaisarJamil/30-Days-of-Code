#!/bin/python3

import math
import os
import random
import re
import sys

def cal_hourglass(arr,row,col):
    sum=0
    sum+=arr[row-1][col-1]
    sum+=arr[row-1][col]
    sum+=arr[row-1][col+1]
    sum+=arr[row][col]
    sum+=arr[row+1][col-1]
    sum+=arr[row+1][col]
    sum+=arr[row+1][col+1]
    return sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

max_hourGlass_sum=-3134
for i in range(1,5):
    for j in range(1,5):
        hourGlass_sum= cal_hourglass(arr,i,j)

        if hourGlass_sum>max_hourGlass_sum:
            max_hourGlass_sum=hourGlass_sum
print(max_hourGlass_sum)
