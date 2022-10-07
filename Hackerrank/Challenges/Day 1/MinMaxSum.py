#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    '''
        Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are , , , , and . Calculate the following sums using four of the five integers:

Sum everything except , the sum is 2+3+4+5=14.
Sum everything except , the sum is 1+3+4+5=13.
Sum everything except , the sum is 1+2+3+5=12.
Sum everything except , the sum is 1+2+3+5=11.
Sum everything except , the sum is 1+2+3+4=10.
    '''
    temp=[]
    for index, i in enumerate(arr):
        temp.append(sum(arr) - i)
    temp.sort()
    print(temp[0], temp[-1])


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
