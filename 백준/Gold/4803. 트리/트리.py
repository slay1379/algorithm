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
    if a_root == b_root:
        return True
    else:
        if rank[a_root] > rank[b_root]:
            parent[b_root] = a_root
        elif rank[b_root] > rank[a_root]:
            parent[a_root] = b_root
        else:
            parent[b_root] = a_root
            rank[a_root] += 1
        return False

case_number = 1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        exit()
    parent = [i for i in range(n+1)]
    rank = [0]*(n+1)
    cycle = [False]*(n+1)
    for _ in range(m):
        v,w = map(int,input().split())
        if union(v,w):
            cycle[find_root(v)] = True

    tree_count = 0
    for i in range(1,n+1):
        if find_root(i) == i and not cycle[i]:
            tree_count += 1

    if tree_count == 0:
        print(f"Case {case_number}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_number}: There is one tree.")
    else:
        print(f"Case {case_number}: A forest of {tree_count} trees.")
    case_number += 1