import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
hour = 0
answer = 0
prev = 0

cheeze = deque()
cheeze.append((0,0))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            answer += 1

while True:
    if hour != 0:
        prev = answer
        answer -= len(cheeze)
    if answer == 0:
        break
    hour += 1
    q = deque(cheeze)
    cheeze = deque()
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if board[nx][ny] == 0:
                    q.append((nx,ny))
                    board[nx][ny] = -1
                elif board[nx][ny] == 1:
                    cheeze.append((nx,ny))
                    board[nx][ny] = -1

print(hour)
print(prev)