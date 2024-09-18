import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def tomato():
    q = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append((i,j))

    dir = [(-1,0),(1,0),(0,1),(0,-1)]

    while q:
        x,y = q.popleft()
        for dx,dy in dir:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M:
                if box[nx][ny] == 0:
                    box[nx][ny] = box[x][y]+1
                    q.append((nx,ny))



M,N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]
answer = 0

tomato()

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()

for row in box:
    if max(row) > answer:
        answer = max(row)

print(answer-1)
