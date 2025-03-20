import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq

N,C = map(int,input().split())
house = list(int(input()) for _ in range(N))

house.sort()

left, right = 1,house[-1]-house[0]

while left <= right:
    mid = (left+right)//2
    now = house[0]
    count = 1
    for i in range(1,N):
        if house[i] >= now+mid:
            count += 1
            now = house[i]
    if count >= C:
        left = mid+1
        result = mid
    else:
        right = mid-1

print(result)


