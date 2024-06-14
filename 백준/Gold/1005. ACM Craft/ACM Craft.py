import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque

def tpsort():
    dp = [0]*(N+1)
    q = deque()
    for i in range(1,N+1):
        if depth[i] == 0:
            q.append(i)
            dp[i] = cost[i]
    while q:
        now = q.popleft()
        for i in graph[now]:
            dp[i] = max(dp[i],dp[now]+cost[i])
            depth[i] -= 1
            if depth[i] == 0:
                q.append(i)
    return dp

T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    cost = [0]+list(map(int,input().split()))
    depth = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        before,after = map(int,input().split())
        graph[before].append(after)
        depth[after] += 1
    W = int(input())
    dp = tpsort()
    print(dp[W])