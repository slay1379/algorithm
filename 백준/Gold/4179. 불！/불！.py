import sys
input = sys.stdin.readline
from collections import deque

R,C = map(int,input().split())
miro = [list(input().strip()) for _ in range(R)]

jihoon = deque()
fire = deque()

for i in range(R):
    for j in range(C):
        if miro[i][j] == 'J':
            jihoon.append((i,j,0))
        if miro[i][j] == 'F':
            fire.append((i,j))

dir = [(1,0),(-1,0),(0,1),(0,-1)]

while jihoon:
    for _ in range(len(fire)):
        x,y = fire.popleft()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0<=nx<R and 0<=ny<C and miro[nx][ny] != '#' and miro[nx][ny] != 'F':
                miro[nx][ny] = 'F'
                fire.append((nx,ny))
    for _ in range(len(jihoon)):
        x,y,day = jihoon.popleft()
        if x == 0 or x == R-1 or y == 0 or y == C-1:
            print(day+1)
            exit()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0<=nx<R and 0<=ny<C and miro[nx][ny] == '.':
                jihoon.append((nx,ny,day+1))
                miro[nx][ny] = 'J'

print('IMPOSSIBLE')
