import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def find_root(a):
    if parent[a] != a:
        return find_root(parent[a])
    else:
        return parent[a]

def union(a,b):
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root == b_root:
        return
    if A[a_root] < A[b_root]:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root


N,M,k = map(int,input().split())
A = [0]+list(map(int,input().split()))
parent = [i for i in range(N+1)]
for _ in range(M):
    v,w = map(int,input().split())
    union(v,w)

answer = 0
for i in range(1,N+1):
    root = find_root(i)
    if find_root(0) == root:
        continue
    else:
        union(0,root)
        answer += A[root]


if answer <= k:
    print(answer)
else:
    print("Oh no")
