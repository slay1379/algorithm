import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def change_number(i,j,current_number):
    q = deque()
    q.append((i,j))
    visit[i][j] = True
    board[i][j] = current_number
    direction = [(-1,0),(0,1),(1,0),(0,-1)]
    while q:
        x,y = q.popleft()
        for nx,ny in direction:
            dx = x+nx
            dy = y+ny
            if 0<=dx<N and 0<=dy<M:
                if board[dx][dy] == 1 and not visit[dx][dy]:
                    q.append((dx,dy))
                    visit[dx][dy] = True
                    board[dx][dy] = current_number

def find_edge(i,j):
    direction = [(-1,0),(1,0),(0,1),(0,-1)]
    for nx,ny in direction:
        dx = i+nx
        dy = j+ny
        if 0<=dx<N and 0<=dy<M:
            if board[dx][dy] == 0:
                length, destination = go_straight(nx,ny,i,j)
                if length >= 2 and board[i][j] < destination:
                    edges.append((length,board[i][j],destination))


def go_straight(nx,ny,i,j):
    length = 0
    while True:
        i += nx
        j += ny
        if i<0 or i>=N or j<0 or j>=M:
            return -1,-1
        if board[i][j] != 0:
            return length,board[i][j]
        length += 1

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
    return False

def cal_min_length(current_number):
    answer = 0
    edge_count = 0
    for cost,a,b in edges:
        if union(a,b):
            answer += cost
            edge_count += 1
    if edge_count == current_number-2:
        return answer
    else:
        return -1

def every_link(current_number):
    root = find_root(1)
    for i in range(2,current_number):
        if root != find_root(i):
            return False
    return True


N,M = map(int,input().split())
board = [list(map(int,input().split()))for _ in range(N)]
visit = [[False]*M for _ in range(N)]
current_number = 1
edges = []

for i in range(N):
    for j in range(M):
        if not visit[i][j] and board[i][j] == 1:
            change_number(i,j,current_number)
            current_number += 1

parent = [i for i in range(current_number)]

for i in range(N):
    for j in range(M):
        if board[i][j] >= 1:
            find_edge(i,j)


edges.sort()
answer = cal_min_length(current_number)
if every_link(current_number):
    print(answer)
else:
    print(-1)


