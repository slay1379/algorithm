import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def topology():
    q = deque()
    answer = [0]*(N+1)
    current_time = 0

    for i in range(1,N+1):
        if degree[i] == 0:
            q.append(i)
            answer[i] = cost[i]

    while q:
        now = q.popleft()
        max_cost = 0
        for i in graph2[now]:
            if max_cost < answer[i]:
                max_cost = answer[i]
        answer[now] = max_cost + cost[now]
        for next in graph[now]:
            degree[next] -= 1
            if degree[next] == 0:
                q.append(next)

    return answer


N = int(input())
cost = [0]
graph = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
degree = [0]*(N+1)
for i in range(1,N+1):
    building = list(map(int,input().split()))
    cost.append(building[0])
    for j in range(1,len(building)-1):
        graph[building[j]].append(i)
        graph2[i].append(building[j])
        degree[i] += 1


answer = topology()

for i in range(1,len(answer)):
    print(answer[i])
