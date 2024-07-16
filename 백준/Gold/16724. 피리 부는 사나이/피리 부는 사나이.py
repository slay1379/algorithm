import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq

N,M = map(int,input().split())
map = [list(map(str,input().strip()))for _ in range(N)]


def find_safe_zones(N,M):
    safe_zone = 0
    visit = [[False]*M for _ in range(N)]

    def DFS(x,y):
        path = set()
        q = deque()
        q.append((x,y))
        while q:
            nx,ny = q.popleft()

            if (nx,ny) in path:
                return 1
            if visit[nx][ny]:
                return 0

            visit[nx][ny] = True

            if map[nx][ny] == 'D':
                q.append((nx+1,ny))
            elif map[nx][ny] == 'U':
                q.append((nx-1,ny))
            elif map[nx][ny] == 'L':
                q.append((nx,ny-1))
            elif map[nx][ny] == 'R':
                q.append((nx,ny+1))

            path.add((nx,ny))

    for i in range(N):
        for j in range(M):
            if not visit[i][j]:
                safe_zone += DFS(i,j)

    return safe_zone

print(find_safe_zones(N,M))