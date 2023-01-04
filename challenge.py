import sys
import os
from functools import reduce
import operator
''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here
def get_diff(lists,N, M):
    # lists = sorted(lists)
    lists.sort()
    print(lists)
    print(N,M)
    if M <= N//2:
        grp1 = reduce(operator.add, lists[:M])
        grp2 = reduce(operator.add, lists[M:])
    else:
        grp1 = reduce(operator.add, lists[:(N-M)])
        grp2 = reduce(operator.add, lists[(N-M):])

    print(grp1)
    print(grp2)
    return abs(grp1-grp2)

def main():
    count = eval(input())
    for i in range(count):
        N,M = input().split(' ')
        lists = [int(i) for i in input().split(' ')]
        print(get_diff(lists,int(N), int(M)))



if __name__ == '__main__':
    main()