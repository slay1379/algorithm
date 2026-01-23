import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    if B not in graph[A]:
        graph[A].append(B)
    if A not in graph[B]:
        graph[B].append(A)

def bfs(start_node, visited):
    q = deque([start_node])

    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if visited[next_node] == 0 or visited[next_node] > visited[now] + 1:
                visited[next_node] = visited[now] + 1
                q.append(next_node)

answer = 0
person_number = 0

for i in range(1,N+1):
    visited = [0]*(N+1)
    bfs(i,visited)
    if answer == 0 or answer > sum(visited):
        answer = sum(visited)
        person_number = i

print(person_number)