import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def bfs(N,cave):
    rupee = [[float('inf')]*N for _ in range(N)]
    rupee[0][0] = cave[0][0]
    q = deque()
    q.append((0,0))
    x = [0,-1,0,1]
    y = [-1,0,1,0]
    while q:
        nx,ny = q.popleft()
        for i in range(4):
            dx = nx+x[i]
            dy = ny+y[i]
            if 0<=dx<N and 0<=dy<N:
                if rupee[nx][ny] + cave[dx][dy] < rupee[dx][dy]:
                    rupee[dx][dy] = rupee[nx][ny] + cave[dx][dy]
                    q.append((dx,dy))
    return rupee

depth = 0
while True:
    depth += 1
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int,input().split())) for _ in range(N)]
    rupee = bfs(N,cave)
    print("Problem %d: %d" %(depth,rupee[N-1][N-1]))