import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def turn_over():
    for i in range(H):
        for j in range(W//2):
            boolpan[i][j],boolpan[i][W-1-j] = boolpan[i][W-1-j],boolpan[i][j]


T = int(input())
for _ in range(T):
    H,W = map(int,input().split())
    boolpan = [list(map(str,input().strip())) for _ in range(H)]
    turn_over()
    for row in boolpan:
        print(''.join(row))




