import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())
    for n in range(0,t):
        arr = str(input()).split(" ")
        arr.reverse()

        for num in arr:
            print(num + " ", end="")
