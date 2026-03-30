import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations

N,K = map(int,input().split())
degrees = list(map(int,input().split()))

answer = sum(degrees[:K])
total = answer
left, right = 0, K-1
while left < N-K:
    total -= degrees[left]
    total += degrees[right+1]
    if answer < total:
        answer = total
    left += 1
    right += 1

print(answer)
