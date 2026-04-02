import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N, M = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(N)]

q = deque()
q.append((0,0))
nx = [-1,1,0,0]
ny = [0,0,1,-1]
visit = [[-1] * M for _ in range(N)]
visit[0][0] = 1

while q:
    x,y = q.popleft()
    for i in range(4):
        dx = x+nx[i]
        dy = y+ny[i]
        if 0<=dx<N and 0<=dy<M and board[dx][dy] == 1 and visit[dx][dy] == -1:
            q.append((dx,dy))
            visit[dx][dy] = visit[x][y] + 1

print(visit[N-1][M-1])