import sys
input = sys.stdin.readline
from collections import deque
import heapq

N = int(input())

now = 665
idx = 0
while True:
    now += 1
    if '666' in str(now):
        idx += 1
    if idx == N:
        print(now)
        break
