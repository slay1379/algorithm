import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

H,W = map(int,input().split())
board = [list(map(str,input().strip())) for _ in range(H)]
result = [[-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if j == 0:
            if board[i][j] == 'c':
                result[i][j] = 0
        else:
            if board[i][j] == 'c':
                result[i][j] = 0
            elif result[i][j-1] == -1:
                result[i][j] = -1
            else:
                result[i][j] = result[i][j-1]+1

for row in result:
    print(*row)
