import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def dijkstra(n,start,graph):
    distances = [float('inf')]*(n+1)
    distances[start] = 0
    queue = [(start,0)]
    while queue:
        now_node, now_distance = heapq.heappop(queue)
        if now_distance > distances[now_node]:
            continue
        for neighbor, weight in graph[now_node]:
            dist = weight + now_distance
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(queue,(neighbor,dist))
    return distances

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
item = [0]+list(map(int,input().split()))
for _ in range(r):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

answer = 0
for i in range(1,n+1):
    distances = dijkstra(n,i,graph)
    getable = 0
    for j in range(1,n+1):
        if distances[j] <= m:
            getable += item[j]
    if answer < getable:
        answer = getable

print(answer)