import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


N = int(input())
tower = list(map(int,input().split()))
stack = []
answer = [0]*(N)

for i in range(N-1,-1,-1):
    while stack and tower[stack[-1]] < tower[i]:
        answer[stack.pop()] = i+1
    stack.append(i)

print(' '.join(map(str,answer)))

