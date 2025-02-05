import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
parent = list(map(int,input().split()))
node = int(input())

graph = [[]for _ in range(N)]
q = deque()

for i in range(N):
    if parent[i] == -1:
        if i != node:
            q.append(i)
        continue
    graph[parent[i]].append(i)

answer = 0

while q:
    now = q.popleft()
    if node in graph[now]:
        if len(graph[now])-1 == 0:
            answer += 1
    else:
        if len(graph[now]) == 0:
            answer += 1
    for next in graph[now]:
        if next != node:
            q.append(next)

print(answer)