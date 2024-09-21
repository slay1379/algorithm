import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def is_empty(x,y):
    for dx,dy in dir:
        nx = x+dx
        ny = y+dy
        if room[nx][ny] == 0:
            return True
    return False


N,M = map(int,input().split())
r,c,d = map(int,input().split())

room = [list(map(int,input().split())) for _ in range(N)]
dir = [(-1,0),(0,1),(1,0),(0,-1)]
answer = 0

q = deque()
q.append((r,c))

while q:
    x,y = q.popleft()
    if room[x][y] == 0:
        room[x][y] = -1
        answer += 1
    if is_empty(x,y):
        while True:
            if d == 0:
                d = 3
            else:
                d -= 1
            dx,dy = dir[d]
            nx = x+dx
            ny = y+dy
            if room[nx][ny] == 0:
                q.append((nx,ny))
                break
    else:
        nx,ny = dir[(d+2)%4]
        if room[x+nx][y+ny] != 1:
            q.append((x+nx,y+ny))
        else:
            break

print(answer)
