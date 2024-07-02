import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def dijkstra(V,graph,start):
    distances = [float('inf')]*(V+1)
    distances[start] = 0
    priority_queue = [(0,start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance,neighbor))
    return distances

V,E = map(int,input().split())
k = int(input())
graph = [[]for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

distances = dijkstra(V,graph,k)


for i in range(1,V+1):
    if distances[i] == float('inf'):
        print("INF")
    else:
        print(distances[i])

