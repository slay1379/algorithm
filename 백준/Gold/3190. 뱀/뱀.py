import sys
input = sys.stdin.readline
from collections import deque
import heapq

N = int(input())
board = [[0]*N for _ in range(N)]
board[0][0] = -1
K = int(input())
for _ in range(K):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1
L = int(input())
moves = deque()
for _ in range(L):
    X,C = map(str,input().split())
    moves.append((int(X),C))

now = 1
dir = [(0,1),(1,0),(0,-1),(-1,0)]
idx = 0
head_x,head_y = 0,0
tail_x,tail_y = 0,0
sneak_route = deque()
while True:
    x,y = dir[idx]
    head_x,head_y = head_x+x, head_y+y
    sneak_route.append((head_x,head_y))
    if head_x < 0 or head_x >= N or head_y < 0 or head_y >= N or board[head_x][head_y] == -1:
        break
    if board[head_x][head_y] != 1:
        board[tail_x][tail_y] = 0
        tail_x, tail_y = sneak_route.popleft()
    board[head_x][head_y] = -1
    if moves and now == moves[0][0]:
        X,C = moves.popleft()
        if C == 'D':
            idx += 1
            idx %= 4
        else:
            idx -= 1
            idx %= 4
    now += 1


print(now)