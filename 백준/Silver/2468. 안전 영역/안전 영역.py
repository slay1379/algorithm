import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
now = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(now_x,now_y):
    q = deque()
    q.append((now_x,now_y))
    new_board[now_x][now_y] = -1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and new_board[nx][ny] != -1:
                q.append((nx,ny))
                new_board[nx][ny] = -1

for rain in range(1,101):
    new_board = [row[:] for row in board]
    count = 0
    for i in range(N):
        for j in range(N):
            if new_board[i][j] < rain:
                new_board[i][j] = -1
    for i in range(N):
        for j in range(N):
            if new_board[i][j] != -1:
                bfs(i,j)
                count += 1

    if now <= count:
        now = count

print(now)


