import sys
from collections import deque

input = sys.stdin.readline

def BFS(v):
    q = deque([v])
    visit[v] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visit[i] == 0:
                visit[i] = -visit[v]
                q.append(i)
            elif visit[i] == visit[v]:
                return False
    return True

K = int(input())
for i in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visit = [0] * (V+1)
    for j in range(E):
        x,y= map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    is_bipartite = True
    for i in range(1,V+1):
        if visit[i] == 0:
            if not BFS(i):
                is_bipartite = False
                break
    print('YES' if is_bipartite else 'NO')

