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
        elif rank[a_root] < rank[b_root]:
            parent[a_root] = b_root
        else:
            parent[b_root] = a_root
            rank[a_root] += 1

def check_union(a,b):
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root == b_root:
        print('YES')
    else:
        print('NO')


n,m = map(int,input().split())
parent = [i for i in range(n+1)]
rank = [0] * (n+1)
for _ in range(m):
    oper,a,b = map(int,input().split())
    if oper == 0:
        union(a,b)
    else:
        check_union(a,b)
