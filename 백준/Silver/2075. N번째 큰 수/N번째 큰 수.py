import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


N = int(input())
q = []
for i in range(N):
    seq = list(map(int,input().split()))
    if not q:
        for s in seq:
            heapq.heappush(q,s)
    else:
        for s in seq:
            if s > q[0]:
                heapq.heappop(q)
                heapq.heappush(q,s)

print(q[0])
