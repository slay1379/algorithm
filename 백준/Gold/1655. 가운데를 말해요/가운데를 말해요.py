import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


N = int(input())
min_heap = []
max_heap = []
for _ in range(N):
    a = int(input())
    if len(min_heap)==0 and len(max_heap)==0:
        p = a
        heapq.heappush(max_heap,(-a,a))
    else:
        if a > p:
            heapq.heappush(min_heap,a)
        else:
            heapq.heappush(max_heap,(-a,a))

        if len(max_heap) > len(min_heap)+1:
            heapq.heappush(min_heap,heapq.heappop(max_heap)[1])
        elif len(min_heap) > len(max_heap):
            b = heapq.heappop(min_heap)
            heapq.heappush(max_heap,(-b,b))

        p = max_heap[0][1]
    print(p)




