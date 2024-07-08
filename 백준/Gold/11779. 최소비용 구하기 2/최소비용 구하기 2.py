import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def dijkstra(n,start,graph):
    costs= [float('inf')]*(n+1)
    path = [[] for _ in range(n+1)]
    costs[start] = 0
    path[start].append(start)
    priority_queue = [(start,0)]
    while priority_queue:
        now_node, now_cost = heapq.heappop(priority_queue)
        if now_cost > costs[now_node]:
            continue
        for neighbor, weight in graph[now_node]:
            cost = weight + now_cost
            if cost < costs[neighbor]:
                costs[neighbor] = cost
                heapq.heappush(priority_queue,(neighbor,cost))
                path[neighbor] = path[now_node] + [neighbor]
    return costs,path


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))
wantStart,wantEnd = map(int,input().split())
costs,path = dijkstra(n,wantStart,graph)
print(costs[wantEnd])
print(len(path[wantEnd]))
print(' '.join(map(str,path[wantEnd])))