import sys
input = sys.stdin.readline
from collections import deque
import heapq

N,M,x,y,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
opers = list(map(int,input().split()))
dice = [[0]*3 for _ in range(4)]
dice_x,dice_y = 1,1

move = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]

for oper in opers:
    dx,dy = move[oper]
    nx = x+dx
    ny = y+dy
    if 0<=nx<N and 0<=ny<M:
        if oper == 1:
            dice[1][0],dice[1][1],dice[1][2],dice[3][1] = dice[3][1],dice[1][0],dice[1][1],dice[1][2]
        if oper == 2:
            dice[1][0],dice[1][1],dice[1][2],dice[3][1] = dice[1][1],dice[1][2],dice[3][1],dice[1][0]
        if oper == 3:
            dice[0][1],dice[1][1],dice[2][1],dice[3][1] = dice[1][1],dice[2][1],dice[3][1],dice[0][1]
        if oper == 4:
            dice[0][1],dice[1][1],dice[2][1],dice[3][1] = dice[3][1],dice[0][1],dice[1][1],dice[2][1]
        if board[nx][ny] == 0:
            board[nx][ny] = dice[3][1]
        else:
            dice[3][1] = board[nx][ny]
            board[nx][ny] = 0
        print(dice[1][1])
        x,y = nx,ny