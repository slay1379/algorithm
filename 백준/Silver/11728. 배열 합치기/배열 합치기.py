import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i in A:
    B.append(i)

B.sort()
print(' '.join(map(str,B)))    