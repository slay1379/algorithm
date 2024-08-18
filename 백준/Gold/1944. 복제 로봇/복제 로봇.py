import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def bfs(i,j,now_count):
    q = deque()
    q.append((i,j,0))
    miro[i][j] = '0'
    visit = [[False]*N for _ in range(N)]
    direction = [(-1,0),(0,1),(1,0),(0,-1)]
    dist = 0
    visit[i][j] = True

    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            dx,dy = direction[i]
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == False:
                if miro[nx][ny] == '0':
                    q.append((nx,ny,dist+1))
                    visit[nx][ny] = True
                if miro[nx][ny] == 'K':
                    for kx,ky,count in key:
                        if kx == nx and ky == ny:
                            graph[now_count].append(count)
                            edges.append((dist+1,now_count,count))
                            q.append((nx,ny,dist+1))
                            visit[nx][ny] = True


def find_root(a):
    if parent[a] != a:
        parent[a] = find_root(parent[a])
    return parent[a]

def union(a,b):
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root != b_root:
        parent[b_root] = a_root
        return True
    else:
        return False

def mst():
    answer = 0
    for dist,a,b in edges:
        if union(a,b):
            answer += dist
    return answer



N,M = map(int,input().split())
miro = [list(map(str,input().strip())) for _ in range(N)]
key = []
graph = [[] for _ in range(M+2)]
edges = []

count = 2

for i in range(N):
    for j in range(N):
        if miro[i][j] == 'S':
            start = (i,j)
        if miro[i][j] == 'K':
            key.append((i,j,count))
            count += 1


bfs(start[0],start[1],1)
if len(graph[1]) < M:
    print(-1)
    exit()

for i,j,count in key:
    bfs(i,j,count)

edges.sort()

parent = [i for i in range(M+2)]
print(mst())
