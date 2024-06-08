import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

N,M = map(int,input().split())
A = list(map(int,input().split()))

left, right = 0,0
total = A[right]
answer = 0

while True:
    if total == M:
        answer += 1
    if left == right:
        right += 1
        if right >= N:
            break
        total += A[right]
    else:
        if total < M:
            right += 1
            if right >= N:
                break
            total += A[right]
        else:
            total -= A[left]
            left += 1

print(answer)


