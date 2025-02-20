import sys
input = sys.stdin.readline
from collections import deque
import heapq

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dir = [(1,0),(-1,0),(0,1),(0,-1)]
now_size = 2
answer = 0
stack = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            board[i][j] = 0
            x,y = i,j

def find_available(now_x,now_y,size):
    visit = [[False] * N for _ in range(N)]
    q = deque()
    q.append((now_x,now_y,0))
    movable = []
    while q:
        x,y,dis = q.popleft()
        for dx,dy in dir:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<N and board[nx][ny]<=size and visit[nx][ny] == False:
                q.append((nx,ny,dis+1))
                visit[nx][ny] = True
                if board[nx][ny] < size and board[nx][ny] != 0:
                    movable.append((dis+1,nx,ny))
    return movable

while True:
    movable = find_available(x, y, now_size)
    if not movable:
        break
    movable.sort()
    dis, x, y = movable[0]
    board[x][y] = 0
    answer += dis
    stack += 1
    if stack == now_size:
        now_size += 1
        stack = 0

print(answer)