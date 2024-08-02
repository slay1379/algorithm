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
        elif rank[b_root] > rank[a_root]:
            parent[a_root] = b_root
        else:
            parent[b_root] = a_root
            rank[a_root] += 1
        return True
    else:
        return False


def connect():
    answer = 0
    edge_count = 0
    for cost,a,b in edges:
        if union(a,b):
            answer += cost
            edge_count += 1
            if edge_count == N-1:
                return answer

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]
rank = [0]*(N+1)
edges = []
cycle = []
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()
answer = connect()
print(answer)
