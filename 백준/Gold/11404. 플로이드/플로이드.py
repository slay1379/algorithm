import sys
input = sys.stdin.readline
from collections import deque
import heapq


n = int(input())
m = int(input())

dist = [[sys.maxsize]*n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    if dist[a - 1][b - 1] > c:
        dist[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

output = []
for i in range(n):
    row = []
    for j in range(n):
        if dist[i][j] == sys.maxsize:
            row.append("0")
        else:
            row.append(str(dist[i][j]))
    output.append(" ".join(row))
    
print("\n".join(output))