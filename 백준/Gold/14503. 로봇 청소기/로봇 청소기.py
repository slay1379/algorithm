import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq

N,M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer = 0

nx = [-1,0,1,0]
ny = [0,1,0,-1]

q = deque()
q.append((r,c,d))

def check_cleanable_room(x,y):
    for i in range(4):
        dx = x+nx[i]
        dy = y+ny[i]
        if 0<=dx<N and 0<=dy<M and board[dx][dy] == 0:
            return True
    return False

while q:
    x,y,d = q.popleft()
    if board[x][y] == 0:
        answer += 1
        board[x][y] = 2
    if check_cleanable_room(x,y):
        while True:
            d -= 1
            if d == -1:
                d = 3
            dx = x + nx[d]
            dy = y + ny[d]
            if 0 <= dx < N and 0 <= dy < M and board[dx][dy] == 0:
                q.append((dx, dy, d))
                break
    else:
        bd = (d+2) % 4
        dx = x+nx[bd]
        dy = y+ny[bd]
        if 0<=dx<N and 0<=dy<M and board[dx][dy] != 1:
            q.append((dx,dy,d))
        else:
            break

print(answer)
