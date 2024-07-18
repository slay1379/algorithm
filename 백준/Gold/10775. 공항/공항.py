import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def find_root(a):
    if parent[a] != a:
        parent[a] = find_root(parent[a])
    return parent[a]


G = int(input())
P = int(input())

parent = [i for i in range(G+1)]
answer = 0

for _ in range(P):
    g = int(input())
    g_root = find_root(g)
    if parent[g_root] != 0:
        parent[g_root] -= 1
        answer += 1
        continue
    break
print(answer)


