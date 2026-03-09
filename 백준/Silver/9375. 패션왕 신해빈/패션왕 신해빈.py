import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = defaultdict(list)
    for _ in range(n):
        name, category = map(str,input().split())
        clothes[category].append(name)

    answer = 1
    for key in clothes:
        answer *= (len(clothes[key]) + 1)
    print(answer - 1)