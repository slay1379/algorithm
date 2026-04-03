import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int,input().split())
    graph[B].append(A)

result = [0]*(N+1)

for i in range(1,N+1):
    q = deque()
    q.append(i)
    answer = 1
    visit = [False]*(N+1)
    visit[i] = True
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if not visit[next_node]:
                visit[next_node] = True
                q.append(next_node)
                answer += 1
    result[i] = answer

max_value = max(result)
for i in range(1,N+1):
    if result[i] == max_value:
        print(i,end=" ")
