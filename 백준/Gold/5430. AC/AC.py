import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    x_input = input().strip()[1:-1]

    if x_input:
        x = deque(map(int, x_input.split(',')))
    else:
        x = deque()

    reverse_flag = False
    error_flag = False

    for cmd in p:
        if cmd == 'R':
            reverse_flag = not reverse_flag
        elif cmd == 'D':
            if not x:
                error_flag = True
                break
            if reverse_flag:
                x.pop()
            else:
                x.popleft()

    if error_flag:
        print('error')
    else:
        if reverse_flag:
            x.reverse()
        print(f"[{','.join(map(str, x))}]")
