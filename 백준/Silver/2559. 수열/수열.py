import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

N,K = map(int,input().split())
degree = list(map(int,input().split()))

total = 0

left,right = 0,K-1
for i in range(K):
    total += degree[i]

answer = total

while right < N-1:
    total -= degree[left]
    left += 1
    right += 1
    total += degree[right]
    if answer < total:
        answer = total

print(answer)

