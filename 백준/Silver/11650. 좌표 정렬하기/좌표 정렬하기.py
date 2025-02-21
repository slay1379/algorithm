import sys
input = sys.stdin.readline
from collections import deque
import heapq

N = int(input())
dots = []
for _ in range(N):
    x,y = map(int,input().split())
    dots.append((x,y))

dots.sort()
for x,y in dots:
    print(x,y)