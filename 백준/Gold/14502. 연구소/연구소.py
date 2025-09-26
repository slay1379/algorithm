import sys
from collections import deque
import copy

input = sys.stdin.readline

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dir = [(1,0),(-1,0),(0,1),(0,-1)]

def progress_virus(board):
    q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for nx,ny in dir:
            dx = x+nx
            dy = y+ny
            if 0<=dx<N and 0<=dy<M:
                if board[dx][dy] == 0:
                    board[dx][dy] = 2
                    q.append((dx,dy))

    return count_zero(board)

def count_zero(board):
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                count+=1
    return count

answer = 0

zeros = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            zeros.append((i,j))

for i in range(len(zeros)-2):
    for j in range(i+1,len(zeros)-1):
        for k in range(j+1,len(zeros)):
            if board[zeros[i][0]][zeros[i][1]] != 0 or board[zeros[j][0]][zeros[j][1]] != 0 or board[zeros[k][0]][zeros[k][1]] != 0:
                continue

            board[zeros[i][0]][zeros[i][1]] = 1
            board[zeros[j][0]][zeros[j][1]] = 1
            board[zeros[k][0]][zeros[k][1]] = 1
            temp_board = copy.deepcopy(board)
            cnt = progress_virus(temp_board)
            if cnt > answer:
                answer = cnt
            board[zeros[i][0]][zeros[i][1]] = 0
            board[zeros[j][0]][zeros[j][1]] = 0
            board[zeros[k][0]][zeros[k][1]] = 0

print(answer)