import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

virus = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i,j))

def bfs():
    q = deque()
    for i,j in virus:
        q.append((i,j))

    new_board = [row[:] for row in board]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and new_board[nx][ny] == 0:
                q.append((nx,ny))
                new_board[nx][ny] = 2

    result = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 0:
                result += 1

    return result

def dfs(x,y,cnt):
    if cnt == 3:
        answer.append(bfs())
        return
    i,j = x,y
    while True:
        if i == N-1 and j == M-1:
            break
        j += 1
        if j == M:
            i += 1
            j = 0
        if board[i][j] == 0:
            board[i][j] = 1
            dfs(i,j,cnt+1)
            board[i][j] = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            board[i][j] = 1
            dfs(i,j,1)
            board[i][j] = 0

print(max(answer))
