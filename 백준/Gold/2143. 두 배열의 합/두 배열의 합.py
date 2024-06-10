import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

As = defaultdict(int)
for start in range(n):
    subtotal = 0
    for end in range(start,n):
        subtotal += A[end]
        As[subtotal] += 1
answer = 0
for start in range(m):
    subtotal = 0
    for end in range(start,m):
        subtotal += B[end]
        if T - subtotal in As:
            answer += As[T-subtotal]

print(answer)