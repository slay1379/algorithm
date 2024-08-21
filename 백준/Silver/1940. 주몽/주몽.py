import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


N = int(input())
M = int(input())
nums = list(map(int,input().split()))

nums.sort()

left,right = 0,N-1
answer = 0

while left<right:
    now = nums[left]+nums[right]
    if now == M:
        answer += 1
    if now >= M:
        right -= 1
    else:
        left += 1

print(answer)
