import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


K = int(input())
C = int(input())
for _ in range(C):
    M,N = map(int,input().split())
    diff = abs(M-N)
    if M>N:
        if diff - (K-M) <= 2:
            print(1)
        else:
            print(0)
    elif M<N:
        if diff - (K-N) <= 1:
            print(1)
        else:
            print(0)
    else:
        print(1)