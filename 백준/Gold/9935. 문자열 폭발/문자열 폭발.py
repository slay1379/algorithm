import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


string = input().strip()
bomb = input().strip()

stack = []
bomb_len = len(bomb)

for c in string:
    stack.append(c)
    if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')