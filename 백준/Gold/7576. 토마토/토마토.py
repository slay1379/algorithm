import sys
from collections import deque

input = sys.stdin.readline

M,N = map(int,input().split())
box = [list(map(int,input().split()))for _ in range(N)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
q=deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i,j))
def BFS():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if box[nx][ny] == 0:
                q.append((nx,ny))
                box[nx][ny] = box[x][y]+1

BFS()
max_day = 0
for row in box:
    if 0 in row:
        print('-1')
        exit(0)
    max_day = max(max_day, max(row))

print(max_day-1)
