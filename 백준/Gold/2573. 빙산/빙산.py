import sys
input = sys.stdin.readline
from collections import deque
import heapq

N,M = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(N)]
dir = [(1,0),(-1,0),(0,1),(0,-1)]
year = 0

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visit[i][j] = True
    while q:
        x,y = q.popleft()
        count = 0
        for dx,dy in dir:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M and visit[nx][ny] == False:
                if ice[nx][ny] == 0:
                    count += 1
                if ice[nx][ny] > 0:
                    q.append((nx,ny))
                    visit[nx][ny] = True
        if ice[x][y] - count < 0:
            ice[x][y] = 0
        if ice[x][y] - count >= 0:
            ice[x][y] -= count

while True:
    changed = False
    visit = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0 and not visit[i][j]:
                if changed:
                    print(year)
                    exit()
                bfs(i, j)
                changed = True
    if not changed:
        print(0)
        break
    year += 1

