import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

while True:
    line = input().rstrip()
    if line == '.':
        break
    stack = []
    flag = True
    for ch in line:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
    if not flag or stack:
        print("no")
    else:
        print("yes")