import sys
input = sys.stdin.readline
from collections import deque
import heapq


N,M = map(int,input().split())
board = [list(map(str,input().strip())) for _ in range(N)]
count = [[[-1]*2 for _ in range(M)] for _ in range(N)]
count[0][0][0] = 1

q = deque()
q.append((0,0,0))

dir = [(1,0),(-1,0),(0,1),(0,-1)]

while q:
    x,y,wall = q.popleft()

    for dx,dy in dir:
        nx,ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == '0' and count[nx][ny][wall] == -1:
                count[nx][ny][wall] = count[x][y][wall] + 1
                q.append((nx,ny,wall))
                continue
            if board[nx][ny] == '1' and wall == 0 and count[nx][ny][1] == -1:
                count[nx][ny][1] = count[x][y][0] + 1
                q.append((nx,ny,1))

res1 = count[N-1][M-1][0]
res2 = count[N-1][M-1][1]

if res1 == -1 and res2 == -1:
    print(-1)
else:
    print(min(v for v in [res1,res2] if v!= -1))