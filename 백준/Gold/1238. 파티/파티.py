import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def dijkstra(N,start,graph,distances):
    priority_queue = [(start,0)]
    distances[start][start] = 0
    while priority_queue:
        now_node, now_distance = heapq.heappop(priority_queue)
        if now_distance > distances[start][now_node]:
            continue
        for neighbor, weight in graph[now_node]:
            dis = now_distance + weight
            if dis < distances[start][neighbor]:
                distances[start][neighbor] = dis
                heapq.heappush(priority_queue,(neighbor,dis))
    return distances

N,M,X = map(int,input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    v,u,w = map(int,input().split())
    graph[v].append((u,w))
distances = [[float('inf')]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    distances = dijkstra(N,i,graph,distances)

answer = 0

for i in range(1,N+1):
    if i == X:
        continue
    if answer < distances[X][i] + distances[i][X]:
        answer = distances[X][i] + distances[i][X]

print(answer)