#!/bin/python3

import math
import os
import random
import sys
import re
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def TimeConversion(s):
    '''

    Sample Input

    07:05:45PM
    
    Sample Output

    19:05:45

    '''
    val = s.split(":")
    hr=val[0]
    TZ = val[-1][-2:]
    if TZ == 'PM' and not (int(hr) >= 12):
            hr = int(hr) +12
    elif TZ == 'AM' and hr =='12':
            hr = '00'
    
    print(f'{hr}:{val[1]}:{val[-1][:2]}')




def findMedian(arr):
    arr = sorted(arr)
    print(arr)
    length = len(arr)
    if len(arr)%2:
        return arr[length//2]
    else:
        return arr[length//2]
        



def main():
    # time = input("Enter time : ")
    # TimeConversion(time)

    print(findMedian([0,1,2,4,6,5,3]))

if __name__ == '__main__':
    main()
