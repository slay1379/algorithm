import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq



N,K = map(int,input().split())
jewel = []
bag = []

for _ in range(N):
    M,V = map(int,input().split())
    jewel.append((M,V))

for _ in range(K):
    C = int(input())
    bag.append(C)

jewel.sort()
bag.sort()

answer = 0
available_jewels = []
jewel_index = 0

for b in bag:
    while jewel_index < N and jewel[jewel_index][0] <= b:
        heapq.heappush(available_jewels,-jewel[jewel_index][1])
        jewel_index += 1

    if available_jewels:
        answer += -heapq.heappop(available_jewels)

print(answer)