import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


while True:
    square = list(map(int,input().split()))
    if square[0] == 0:
        break
    n = square[0]
    histogram = square[1:]

    stack = []
    max_area = 0

    for i in range(len(histogram)):
        while stack and histogram[stack[-1]] > histogram[i]:
            height = histogram[stack.pop()]
            width = i if not stack else i - stack[-1] -1
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack:
        height = histogram[stack.pop()]
        width = n if not stack else n - stack[-1]-1
        max_area = max(max_area,height * width)

    print(max_area)
