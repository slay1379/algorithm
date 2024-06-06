import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def close(house,chicken):
    total = 0
    for hx,hy in house:
        dis = sys.maxsize
        for cx,cy in chicken:
           dis = min(dis,abs(hx-cx)+abs(hy-cy))
        total += dis
    return total

N,M = map(int,input().split())
city = [list(map(int,input().split()))for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

answer = sys.maxsize

for chicken_comb in combinations(chicken,M):
    answer = min(answer,close(house,chicken_comb))

print(answer)