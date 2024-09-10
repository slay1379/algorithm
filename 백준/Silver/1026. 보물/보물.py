import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

S = 0

B.sort(reverse=True)
A.sort()

for i in range(N):
    S += A[i]*B[i]

print(S)
