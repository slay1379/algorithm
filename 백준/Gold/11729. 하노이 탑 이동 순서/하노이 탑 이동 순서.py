import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq

def hanoi(n,start,end):
    if n == 1:
        print(start,end)
        return
    else:
        hanoi(n-1,start,6-start-end)
        print(start,end)
        hanoi(n-1,6-start-end,end)

N = int(input())
dp = [0]*(N+1)
dp[1] = 1
for i in range(2,N+1):
    dp[i] = dp[i-1]*2+1
print(dp[N])
hanoi(N,1,3)