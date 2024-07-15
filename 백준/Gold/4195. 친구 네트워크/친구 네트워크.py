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

def union(a,b):
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root != b_root:
        if rank[a_root] > rank[b_root]:
            parent[b_root] = a_root
            size[a_root] += size[b_root]
        elif rank[b_root] > rank[a_root]:
            parent[a_root] = b_root
            size[b_root] += size[a_root]
        else:
            parent[b_root] = a_root
            rank[a_root] += 1
            size[a_root] += size[b_root]



T = int(input())
for _ in range(T):
    F = int(input())
    parent = {}
    rank = {}
    size = {}
    for _ in range(F):
        v,w = input().strip().split()
        if v not in parent:
            parent[v] = v
            rank[v] = 0
            size[v] = 1
        if w not in parent:
            parent[w] = w
            rank[w] = 0
            size[w] = 1
        union(v,w)
        root = find_root(v)
        print(size[root])