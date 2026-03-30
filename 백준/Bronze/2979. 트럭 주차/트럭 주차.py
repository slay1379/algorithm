import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations

A,B,C = map(int,input().split())
cost = [0,A,B,C]
events = []
for _ in range(3):
    start,end = map(int,input().split())
    events.append((start,1))
    events.append((end,-1))

events.sort()

total = 0
answer = 0
for i in range(len(events)-1):
    total += events[i][1]
    answer += (events[i+1][0] - events[i][0]) * cost[total] * total

print(answer)