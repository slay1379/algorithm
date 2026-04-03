import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

T = int(input())
for _ in range(T):
    stack = []
    line = input().strip()
    flag = True
    for ch in line:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                flag = False
                break
            else:
                stack.pop()
    if stack or not flag:
        print("NO")
    else:
        print("YES")