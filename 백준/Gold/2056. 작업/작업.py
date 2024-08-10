import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def topology():
    q = deque()
    dp = [0]*(N+1)

    for i in range(1,N+1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = cost[i]

    while q:
        max_cost = 0
        now = q.popleft()
        for next in graph[now]:
            degree[next] -= 1
            if degree[next] == 0:
                q.append(next)
                max_cost = 0
                for reverse_next in graph2[next]:
                    if max_cost < dp[reverse_next]:
                        max_cost = dp[reverse_next]
                dp[next] = cost[next] + max_cost

    return dp


N = int(input())
cost = [0]
graph = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
degree = [0]*(N+1)
for i in range(1,N+1):
    seq = list(map(int,input().split()))
    cost.append(seq[0])
    for j in range(2,len(seq)):
        graph[seq[j]].append(i)
        graph2[i].append(seq[j])
        degree[i] += 1


dp = topology()
print(max(dp))
