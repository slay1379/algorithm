import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N = int(input())
S = list(map(int,input().split()))
visit = [False]*2000000

def dfs(idx, now):
    if idx == N:
        visit[now] = True
        return
    dfs(idx+1, now+S[idx])
    dfs(idx+1, now)

dfs(0,0)

for i in range(1,len(visit)):
    if not visit[i]:
        print(i)
        break