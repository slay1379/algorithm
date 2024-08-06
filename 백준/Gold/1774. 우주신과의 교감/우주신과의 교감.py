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

def cal_min():
    total_cost = 0.0
    edge_count = 0

    for a, b in connect:
        if union(a, b):
            edge_count += 1

    for cost,a,b in edges:
        if union(a,b):
            total_cost += cost
            edge_count += 1
            if edge_count == N-1:
                return total_cost


N,M = map(int,input().split())
space_god = []
connect = []

for i in range(N):
    X,Y = map(int,input().split())
    space_god.append((X,Y,i+1))

for _ in range(M):
    a,b = map(int,input().split())
    connect.append((a,b))

parent = [i for i in range(N+1)]
edges = []

for i in range(N):
    for j in range(i+1,N):
        cost = ((space_god[i][0] - space_god[j][0]) ** 2 + (space_god[i][1] - space_god[j][1]) ** 2) ** 0.5
        edges.append((cost, space_god[i][2], space_god[j][2]))

edges.sort()

min_cost = cal_min()

print(f"{min_cost:.2f}")