import sys
input = sys.stdin.readline
from collections import deque

R,C = map(int,input().split())
cheeze = [list(map(int,input().split())) for _ in range(R)]

dir = [(1,0),(-1,0),(0,1),(0,-1)]

q = deque()
cheezeQ = deque()
day = 0
answer = 0

for i in range(R):
    for j in range(C):
        if i == 0 or i == R-1 or j == 0 or j == C-1:
            cheeze[i][j] = -1
            q.append((i,j))

while q:
    x,y = q.popleft()
    for dx,dy in dir:
        nx,ny = x+dx,y+dy
        if 0<=nx<R and 0<=ny<C:
            if cheeze[nx][ny] == 0:
                q.append((nx,ny))
                cheeze[nx][ny] = -1
            if cheeze[nx][ny] == 1:
                cheezeQ.append((nx,ny))
                cheeze[nx][ny] = -1

while cheezeQ:
    day += 1
    answer = len(cheezeQ)
    for _ in range(len(cheezeQ)):
        x,y = cheezeQ.popleft()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0<=nx<R and 0<=ny<C:
                if cheeze[nx][ny] == 1:
                    cheezeQ.append((nx,ny))
                    cheeze[nx][ny] = -1
                if cheeze[nx][ny] == 0:
                    q.append((nx,ny))
                    cheeze[nx][ny] = -1
    while q:
        x,y = q.popleft()
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if 0<=nx<R and 0<=ny<C:
                if cheeze[nx][ny] == 0:
                    q.append((nx,ny))
                    cheeze[nx][ny] = -1
                if cheeze[nx][ny] == 1:
                    cheezeQ.append((nx,ny))
                    cheeze[nx][ny] = -1

print(day)
print(answer)




