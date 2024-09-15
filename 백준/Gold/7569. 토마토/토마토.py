import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def tomato(box):
    answer = 0
    q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    q.append((i,j,k))

    dir = [(0,0,1),(0,0,-1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]

    while q:
        x,y,z = q.popleft()
        for dx,dy,dz in dir:
            nx = x+dx
            ny = y+dy
            nz = z+dz
            if 0<=nx<H and 0<=ny<N and 0<=nz<M:
                if box[nx][ny][nz] == 0:
                    q.append((nx,ny,nz))
                    box[nx][ny][nz] = box[x][y][z] + 1

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    return -1
                if box[i][j][k] > answer:
                    answer = box[i][j][k]

    return answer-1



M,N,H = map(int,input().split())

box = [[] for _ in range(H)]
answer = 0
for i in range(H):
    box[i] = [list(map(int,input().split())) for _ in range(N)]

print(tomato(box))

