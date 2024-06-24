import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

N,M = map(int,input().split())
arr = [[0]*(M+1)]+[[0]+list(map(int,input().split())) for _ in range(N)]

accum = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        accum[i][j] = accum[i-1][j] + accum[i][j-1] + arr[i][j] - accum[i-1][j-1]

K = int(input())
for _ in range(K):
    i,j,x,y = map(int,input().split())
    print(accum[x][y]-accum[i-1][y] - accum[x][j-1] + accum[i-1][j-1])

