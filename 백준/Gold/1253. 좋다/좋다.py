import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq



N = int(input())
A = list(map(int,input().split()))

A.sort()

answer = 0

for k in range(N):
    target = A[k]
    left, right =0,N-1

    while left < right:
        if left == k:
            left += 1
            continue
        if right == k:
            right -= 1
            continue

        sum_value = A[left] + A[right]

        if sum_value == target:
            answer += 1
            break
        elif sum_value < target:
            left += 1
        else:
            right -= 1

print(answer)