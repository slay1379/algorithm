import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque
import heapq

M,N = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(M)]

dir = [(1,0),(-1,0),(0,-1),(0,1)]
dp = [[-1]*N for _ in range(M)]

def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx,dy in dir:
        nx,ny = x+dx, y+dy
        if 0<=nx<M and 0<=ny<N and board[nx][ny] < board[x][y]:
            dp[x][y] += dfs(nx,ny)

    return dp[x][y]

print(dfs(0,0))