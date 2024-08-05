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
        parent[b_root] = a_root
        return True
    return False

def cal_min_cost():
    min_cost = 0
    edge_count = 0
    for cost,x,y in edges:
        if union(x,y):
            min_cost += cost
            edge_count += 1
            if edge_count == m-1:
                return min_cost

while True:
    m, n = map(int, input().split())
    if m==0 and n==0:
        exit()
    edges = []
    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        edges.append((z, x, y))
        total += z

    parent = [i for i in range(m)]
    edges.sort()

    min_cost = cal_min_cost()
    print(total - min_cost)


