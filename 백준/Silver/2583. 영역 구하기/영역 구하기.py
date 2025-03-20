import sys
input = sys.stdin.readline
from collections import deque

M,N,K = map(int,input().split())
board = [[0]*N for _ in range(M)]

for _ in range(K):
    y1,x1,y2,x2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = 1

count = 0
dir = [(1,0),(-1,0),(0,1),(0,-1)]
areas = []

def bfs(i,j):
    area = 1
    q = deque()
    q.append((i,j))
    board[i][j] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0<=nx<M and 0<=ny<N:
                if board[nx][ny] == 0:
                    q.append((nx,ny))
                    board[nx][ny] = 1
                    area += 1
    return area

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            count += 1
            areas.append(bfs(i,j))

areas.sort()
print(count)
print(*areas)
