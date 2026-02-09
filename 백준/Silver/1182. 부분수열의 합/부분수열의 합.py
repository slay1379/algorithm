import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N,S = map(int,input().split())
seq = list(map(int,input().split()))
answer = 0

def dfs(idx,now):
    global answer

    if idx == N:
        if now == S:
            answer += 1
        return

    dfs(idx+1, now+seq[idx])
    dfs(idx+1, now)

dfs(0,0)
if S == 0:
    answer -= 1
print(answer)