import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())

miro = [list(map(int,input().strip()))for _ in range(N)]
byuk = [[-1]*M for _ in range(N)]

nx = [-1,0,1,0]
ny = [0,1,0,-1]

def BFS():
    q = deque()
    q.append((0,0))
    byuk[0][0] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx < 0 or dy < 0 or dx >= N or dy >= M:
                continue
            if miro[dx][dy] == 0:
                if byuk[dx][dy] == -1:
                    byuk[dx][dy] = byuk[x][y]
                    q.append((dx, dy))
                else:
                    if byuk[dx][dy] > byuk[x][y]:
                        byuk[dx][dy] = min(byuk[dx][dy], byuk[x][y])
                        q.append((dx, dy))
            elif miro[dx][dy] == 1:
                if byuk[dx][dy] == -1:
                    byuk[dx][dy] = byuk[x][y]+1
                    q.append((dx, dy))
                else:
                    if byuk[dx][dy] > byuk[x][y] + 1:
                        byuk[dx][dy] = min(byuk[dx][dy], byuk[x][y]+1)
                        q.append((dx, dy))

BFS()
print(byuk[N-1][M-1])


