import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def part_count():
    q = deque()
    for i in range(1,N):
        if degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for next, count in graph[now]:
            if part[now].count(0) == N+1:
                part[next][now] += count
            else:
                for i in range(1,N+1):
                    part[next][i] += count*part[now][i]
            degree[next] -= 1
            if degree[next] == 0:
                q.append(next)



N = int(input())
M = int(input())
degree = [0]*(N+1)
graph = [[]for _ in range(N+1)]
part = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    X,Y,K = map(int,input().split())
    degree[X] += 1
    graph[Y].append((X,K))

part_count()
for i in range(1,N+1):
    if part[N][i] > 0:
        print(i,part[N][i])