import sys
input = sys.stdin.readline
from collections import deque
import heapq

N,K = map(int,input().split())
dp = [0]*(K+1)
for _ in range(N):
    W,V = map(int,input().split())
    for i in range(K,W-1,-1):
        if dp[i] < V + dp[i-W]:
            dp[i] = V + dp[i-W]

print(max(dp))