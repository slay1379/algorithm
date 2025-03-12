import sys
input = sys.stdin.readline
from collections import deque
import heapq

board = [list(map(int,input().split())) for _ in range(9)]
zeros = []

rowUsed = [[False]*10 for _ in range(9)]
colUsed = [[False]*10 for _ in range(9)]
boxUsed = [[False]*10 for _ in range(9)]

def box_index(x,y):
    return (x//3)*3 + (y//3)

for i in range(9):
    for j in range(9):
        val = board[i][j]
        if val != 0:
            rowUsed[i][val] = True
            colUsed[j][val] = True
            boxUsed[box_index(i,j)][val] = True
        else:
            zeros.append((i,j))

def backtrack(idx):
    if idx == len(zeros):
        for row in board:
            print(*row)
        sys.exit(0)

    x,y = zeros[idx]
    b = box_index(x,y)
    for val in range(1,10):
        if not rowUsed[x][val] and not colUsed[y][val] and not boxUsed[b][val]:
            rowUsed[x][val] = True
            colUsed[y][val] = True
            boxUsed[b][val] = True
            board[x][y] = val

            backtrack(idx + 1)

            board[x][y] = 0
            rowUsed[x][val] = False
            colUsed[y][val] = False
            boxUsed[b][val] = False

backtrack(0)