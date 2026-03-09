import sys
input = sys.stdin.readline
from collections import deque
import heapq

K,N = map(int,input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

left, right = 1,max(lines)

while True:
    cnt = 0
    mid = (left + right) // 2
    for line in lines:
        cnt += line//mid
    if cnt >= N:
        left = mid+1
    else:
        right = mid-1

    if left>right:
        break

print(right)