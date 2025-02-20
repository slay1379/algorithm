import sys
input = sys.stdin.readline
from collections import deque

N,L,R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def check():
    moved = False
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == False:
                if adjust(i,j,visit):
                    moved = True
    return moved

def adjust(i,j,visit):
    q = deque()
    q.append((i,j))
    stack = [(i,j)]
    total = A[i][j]
    visit[i][j] = True
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x,y = q.popleft()
        for i in range(4):
            dx,dy = dir[i]
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == False:
                if L<=abs(A[x][y]-A[nx][ny])<=R:
                    q.append((nx,ny))
                    stack.append((nx,ny))
                    total += A[nx][ny]
                    visit[nx][ny] = True
    adjustNum = total//len(stack)
    for x,y in stack:
        A[x][y] = adjustNum
    if len(stack) > 1:
        return True

day = 0
while True:
    if check() == False:
        break
    day += 1

print(day)

