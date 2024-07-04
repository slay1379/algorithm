import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def dijkstra(N,graph,start):
    distances = [float('inf')] * (N+1)
    priority_queue = [(start,0)]
    distances[start] = 0
    while priority_queue:
        now_node, now_distance = heapq.heappop(priority_queue)
        if now_distance > distances[now_node]:
            continue
        for neighbor, weight in graph[now_node]:
            dis = now_distance + weight
            if dis < distances[neighbor]:
                distances[neighbor] = dis
                heapq.heappush(priority_queue,(neighbor,dis))
    return distances


N,E = map(int,input().split())
graph = [[]for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())

distances_1 = dijkstra(N,graph,1)
distances_v1 = dijkstra(N,graph,v1)
distances_v2 = dijkstra(N,graph,v2)

path1 = distances_1[v1] + distances_v1[v2] + distances_v2[N]
path2 = distances_1[v2] + distances_v2[v1] + distances_v1[N]

result = min(path1,path2)

if result >= float('inf'):
    print(-1)
else:
    print(result)