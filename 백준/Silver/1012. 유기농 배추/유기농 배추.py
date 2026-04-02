import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1:
                q.append((nx,ny))
                board[nx][ny] = 0

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    board = [[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().split())
        board[y][x] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)