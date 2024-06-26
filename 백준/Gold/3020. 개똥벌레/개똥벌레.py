import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

N,H = map(int,input().split())
stalagmite = []
stalactite = []
for i in range(N):
    if i % 2 == 0:
        stalagmite.append(int(input()))
    else:
        stalactite.append(int(input()))

stalagmite_count = [0]*(H+1)
stalactite_count = [0]*(H+1)

for height in stalagmite:
    stalagmite_count[height] += 1

for height in stalactite:
    stalactite_count[height] += 1

for i in range(H-1,0,-1):
    stalagmite_count[i] += stalagmite_count[i+1]
    stalactite_count[i] += stalactite_count[i+1]

min_obstacle = N
min_count = 0

for i in range(1,H+1):
    obstacles = stalagmite_count[i] + stalactite_count[H-i+1]
    if obstacles < min_obstacle:
        min_obstacle = obstacles
        min_count = 1
    elif obstacles == min_obstacle:
        min_count += 1

print(min_obstacle,min_count)


