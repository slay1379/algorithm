import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N,M,K = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(N)]
visit = [[[-1] * (K+1) for _ in range(M)] for _ in range(N)]
visit[0][0][0] = 1

q = deque()
q.append((0,0,0))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    x,y,broke = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 0:
                if visit[nx][ny][broke] == -1:
                    visit[nx][ny][broke] = visit[x][y][broke] + 1
                    q.append((nx,ny,broke))
            else:
                if broke+1 <= K and visit[nx][ny][broke+1] == -1:
                    visit[nx][ny][broke+1] = visit[x][y][broke] + 1
                    q.append((nx,ny,broke+1))

answer = -1
for i in range(K+1):
    if answer == -1 or visit[-1][-1][i] != -1 and visit[-1][-1][i] < answer:
        answer = visit[-1][-1][i]

print(answer)