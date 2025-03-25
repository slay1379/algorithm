import sys
input = sys.stdin.readline
from collections import Counter

board = [list(map(int,input().split())) for _ in range(9)]

empties = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empties.append((i,j))

def check_row(x,num):
    for i in range(9):
        if board[x][i] == num:
            return False
    return True

def check_col(y,num):
    for i in range(9):
        if board[i][y] == num:
            return False
    return True

def check_box(x,y,num):
    new_x,new_y = x//3*3,y//3*3
    for i in range(new_x,new_x+3):
        for j in range(new_y,new_y+3):
            if board[i][j] == num:
                return False
    return True

def fill(idx):
    x,y = empties[idx]
    for i in range(1,10):
        if check_row(x,i) and check_col(y,i) and check_box(x,y,i):
            board[x][y] = i
            if idx == len(empties)-1:
                for row in board:
                    print(*row)
                exit()
            fill(idx+1)
            board[x][y] = 0

fill(0)
