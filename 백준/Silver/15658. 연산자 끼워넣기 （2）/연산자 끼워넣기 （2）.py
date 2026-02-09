import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
oper = list(map(int,input().split()))

results = []

def dfs(idx, now):
    if idx == N-1:
        results.append(now)
        return

    for i in range(4):
        if i == 0 and oper[i] > 0:
            oper[i] -= 1
            dfs(idx+1, now+A[idx+1])
            oper[i] += 1
        elif i == 1 and oper[i] > 0:
            oper[i] -= 1
            dfs(idx+1, now-A[idx+1])
            oper[i] += 1
        elif i == 2 and oper[i] > 0:
            oper[i] -= 1
            dfs(idx+1, now*A[idx+1])
            oper[i] += 1
        elif i == 3 and oper[i] > 0:
            oper[i] -= 1
            dfs(idx+1, int(now/A[idx+1]))
            oper[i] += 1

dfs(0,A[0])

print(max(results))
print(min(results))