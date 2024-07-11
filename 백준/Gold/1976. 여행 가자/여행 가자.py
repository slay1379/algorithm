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

def union(a,b,rank):
    a_root = find_root(a)
    b_root = find_root(b)
    if a_root != b_root:
        if rank[a_root] > rank[b_root]:
            parent[b_root] = a_root
        elif rank[b_root] > rank[a_root]:
            parent[a_root] = b_root
        else:
            parent[a] = b_root
            rank[b_root] += 1


N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
rank = [0]*(N+1)
for i in range(1,N+1):
    connect = list(map(int,input().split()))
    for j in range(len(connect)):
        if connect[j] == 1:
            union(i,j+1,rank)

plan = list(map(int,input().split()))
root = find_root(plan[0])
for i in range(1,len(plan)):
    if find_root(plan[i]) != root:
        print("NO")
        break
else:
    print("YES")