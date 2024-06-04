import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq

def Z(N,r,c):
    if N == 0:
        return 0
    cur_count = 2*(r%2)+(c%2)
    return 4*Z(N-1,r//2,c//2)+cur_count


N,r,c = map(int,input().split())
print(Z(N,r,c))