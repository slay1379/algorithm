import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


N = int(input())
lecture = []
room = [0]*N
for _ in range(N):
    S,T = map(int,input().split())
    lecture.append((S,T))

lecture.sort()

room = []
heapq.heappush(room,lecture[0][1])

for i in range(1,N):
    start, end = lecture[i]

    if room[0] <= start:
        heapq.heappop(room)

    heapq.heappush(room,end)

print(len(room))