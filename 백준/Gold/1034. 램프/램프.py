import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

N,M = map(int,input().split())
lamp = [list(map(str,input().strip()))for _ in range(N)]
K = int(input())

lamp_dict = {}

for row in lamp:
    lamp_row = ''
    zero_count = 0
    for l in row:
        lamp_row += l
        if l == '0':
            zero_count += 1
    if zero_count % 2 == K % 2 and zero_count <= K:
        if lamp_row in lamp_dict:
            lamp_dict[lamp_row] += 1
        else:
            lamp_dict[lamp_row] = 1

if not lamp_dict:
    print(0)
else:
    print(max(lamp_dict.values()))
