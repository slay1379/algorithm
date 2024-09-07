import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()
connectA = []

for i in a[:4]:
    for j in a[:4]:
        if i != j:
            x = str(i)+str(j)
            connectA.append(int(x))

connectA.sort()
print(connectA[2])