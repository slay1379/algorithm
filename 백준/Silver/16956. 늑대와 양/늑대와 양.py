import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def check_wolf(x,y):
    for dx,dy in directions:
        nx = x+dx
        ny = y+dy
        if 0<=nx<R and 0<=ny<C:
            if pasture[nx][ny] == 'W':
                return False
            if pasture[nx][ny] == 'S':
                continue
            pasture[nx][ny] = 'D'
    return True


R,C = map(int,input().split())
pasture = [list(map(str,input().strip())) for _ in range(R)]

directions = [(-1,0),(0,1),(1,0),(0,-1)]

for i in range(R):
    for j in range(C):
        if pasture[i][j] == 'S':
            if not check_wolf(i,j):
                print(0)
                exit()

print(1)
for row in pasture:
    print(''.join(row))
