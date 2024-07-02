import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def dijkstra(N,graph,start):
    distances = [float('inf')]*(N+1)
    distances[start] = 0
    priority_queue = [(start,0)]

    while priority_queue:
        now_node, now_distance = heapq.heappop(priority_queue)
        if now_distance > distances[now_node]:
            continue
        for neighbor, weight in graph[now_node]:
            distance = now_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue,(neighbor,distance))

    return distances


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
start, end = map(int,input().split())

distances = dijkstra(N,graph,start)

print(distances[end])