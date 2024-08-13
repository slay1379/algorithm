import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

n = int(input())
m = int(input())
routes = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
reversed_routes = [[] for _ in range(n + 1)]
max_time = [0] * (n + 1)

for _ in range(m):
    s, e, t = map(int, input().split())
    routes[s].append((e, t))
    degree[e] += 1
    reversed_routes[e].append((s, t))

start, end = map(int, input().split())

que = deque()
que.append(start)
while que:
    now = que.popleft()

    for t in routes[now]:
        node, value = t[0], t[1]
        max_time[node] = max(max_time[node], max_time[now] + value)
        degree[node] -= 1

        if degree[node] == 0:
            que.append(node)

print(max_time[end])

que.clear()
que.append(end)
count = 0
visited = [False] * (n + 1)
visited[end] = True
while que:
    now = que.popleft()

    for t in reversed_routes[now]:
        node, value = t[0], t[1]

        if max_time[now] == max_time[node] + value:
            count += 1

            if not visited[node]:
                visited[node] = True
                que.append(node)

print(count)