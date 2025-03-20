import sys
input = sys.stdin.readline
from collections import deque

X,Y = map(int,input().split())
Z = int(100*Y/X)

left,right = 0,10**9

min_value = -1

while left <= right:
    mid = (left+right)//2
    new_Z = int(100*(Y+mid)/(X+mid))

    if new_Z <= Z:
        left = mid + 1
    else:
        min_value = mid
        right = mid- 1

print(min_value)