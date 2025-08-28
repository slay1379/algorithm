import sys
from collections import deque
import copy

input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(input().strip()) for _ in range(N)]

rx,ry,bx,by = 0,0,0,0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = set()
visited.add((rx,ry,bx,by))

q = deque([(rx,ry,bx,by,0)])

def move(x,y,dx,dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x,y,count

def solve():
    while q:
        crx,cry,cbx,cby,count = q.popleft()

        if count >= 10:
            continue

        for i in range(4):
            nrx,nry,r_move_count = move(crx,cry,dx[i],dy[i])
            nbx,nby,b_move_count = move(cbx,cby,dx[i],dy[i])

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                print(count+1)
                return

            if nrx == nbx and nry == nby:
                if r_move_count > b_move_count:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx,nry,nbx,nby) not in visited:
                visited.add((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,count+1))

    print(-1)

solve()

