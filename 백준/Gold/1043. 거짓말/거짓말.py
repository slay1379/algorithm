import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
truth = list(map(int,input().split()))[1:]
party = [list(map(int,input().split()))[1:] for _ in range(m)]
graph = [set([]) for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for i in truth:
    visit[i] = True

for i in range(m):
    for person in party[i]:
        for j in party[i]:
            if person != j:
                graph[person].add(j)

q = deque(truth)
while q:
    now = q.popleft()
    for i in graph[now]:
        if not visit[i]:
            visit[i] = True
            q.append(i)

cnt = 0
for i in range(m):
    for person in party[i]:
        if visit[person]:
            cnt += 1
            break

print(m-cnt)



