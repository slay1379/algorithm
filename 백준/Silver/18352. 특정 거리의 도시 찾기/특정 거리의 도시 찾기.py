import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def bfs(start,K,graph):
    q = deque()
    q.append(start)
    distances = [-1]*(N+1)
    distances[start] = 0
    while q:
        now = q.popleft()
        for neighbor in graph[now]:
            if distances[neighbor] == -1:
                q.append(neighbor)
                distances[neighbor] = distances[now] + 1
    return distances

N,M,K,X = map(int,input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)

distances = bfs(X,K,graph)
answer = []
for i in range(1,N+1):
    if K == distances[i]:
        answer.append(i)
if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)