#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
count=0

for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            temp=a[j+1]
            a[j+1]=a[j]
            a[j]=temp
            count+=1

        else:
           count==0

print('Array is sorted in '+ str(count)+ ' swaps.')
print('First Element: '+ str(a[0]))
print('Last Element: '+ str(a[n-1]))


