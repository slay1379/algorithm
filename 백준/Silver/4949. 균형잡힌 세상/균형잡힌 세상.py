import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


while True:
    s = input().rstrip()
    stack = []
    balance = True
    if s == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balance = False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balance = False
                break
    if balance and not stack:
        print('yes')
    else:
        print('no')