import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


N = int(input())
heap = []
for _ in range(N):
    card_count = int(input())
    heapq.heappush(heap,card_count)

answer = 0

while len(heap) > 1:
    card1 = heapq.heappop(heap)
    card2 = heapq.heappop(heap)
    answer += (card1+card2)
    heapq.heappush(heap,(card1+card2))

print(answer)