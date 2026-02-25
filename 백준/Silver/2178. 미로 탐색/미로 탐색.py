import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
miro = [list(map(int,input().strip())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
q = deque()
q.append((0,0))
visit[0][0] = True
dir = [(1,0),(-1,0),(0,1),(0,-1)]

while q:
    x,y = q.popleft()
    for dx,dy in dir:
        nx,ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<M:
            if miro[nx][ny] == 1 and not visit[nx][ny]:
                q.append((nx,ny))
                visit[nx][ny] = True
                miro[nx][ny] = miro[x][y] + 1

print(miro[-1][-1])

