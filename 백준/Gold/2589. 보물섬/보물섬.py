import sys
input = sys.stdin.readline
from collections import deque

L,W = map(int,input().split())
map = [list(map(str,input())) for _ in range(L)]
hour = [[0]*W for _ in range(L)]

def bfs(start_x,start_y,visit):
    visit[start_x][start_y] = 0
    q = deque()
    q.append((start_x,start_y))
    dir = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        x,y = q.popleft()
        for dx,dy in dir:
            nx = x+dx
            ny = y+dy
            if 0<=nx<L and 0<=ny<W:
                if map[nx][ny] == 'L':
                    if visit[nx][ny] == -1 or visit[nx][ny] > visit[x][y]+1:
                        q.append((nx,ny))
                        visit[nx][ny] = visit[x][y] + 1

def find_max(visit):
    max_value = 0
    for i in range(L):
        for j in range(W):
            if visit[i][j] > max_value:
                max_value = visit[i][j]
    return max_value

for i in range(L):
    for j in range(W):
        if map[i][j] == 'L':
            visit = [[-1]*W for _ in range(L)]
            bfs(i,j,visit)
            hour[i][j] = find_max(visit)

answer = 0
for i in range(L):
    for j in range(W):
        if hour[i][j] > answer:
            answer = hour[i][j]

print(answer)
