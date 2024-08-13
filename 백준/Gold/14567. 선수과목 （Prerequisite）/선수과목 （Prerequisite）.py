import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def topology():
    dp = [0]*(N+1)
    q = deque()
    for i in range(1,N+1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            degree[next] -= 1
            if degree[next] == 0:
                q.append(next)
                dp[next] = dp[now] + 1

    return dp


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
degree = [0]*(N+1)
for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    degree[B] += 1

dp = topology()
dp.remove(0)
print(' '.join(map(str,dp)))