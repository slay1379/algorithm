import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

N,M = map(int,input().split())
table = [[0]*(N+1)]+[[0]+list(map(int,input().split()))for _ in range(N)]
accum = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        accum[i][j] = accum[i-1][j] + accum[i][j-1] + table[i][j] - accum[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = accum[x2][y2] - accum[x1-1][y2]-accum[x2][y1-1]+accum[x1-1][y1-1]
    print(result)
