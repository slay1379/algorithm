import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

N,M = map(int,input().split())
seq = [0]+list(map(int,input().split()))
accum = [0]*(N+1)
for i in range(1,N+1):
    accum[i] = accum[i-1]+seq[i]

for _ in range(M):
    i,j = map(int,input().split())
    print(accum[j]-accum[i-1])