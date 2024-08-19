import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

n = int(input())
seq = list(map(int,input().split()))
x = int(input())

seq.sort()

left,right = 0,n-1
answer = 0

while left < right:
    now = seq[left] + seq[right]
    if now == x:
        answer += 1
    if now <= x:
        left += 1
    elif now > x:
        right -= 1

print(answer)

