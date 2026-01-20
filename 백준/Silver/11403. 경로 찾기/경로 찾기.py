import sys
input = sys.stdin.readline

N = int(input())
edges = [list(map(int,input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if edges[i][j] == 1:
            graph[i].append(j)

def dfs(node, visited):
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, visited)

for i in range(N):
    visited =[0]*N
    dfs(i,visited)
    print(*visited)





