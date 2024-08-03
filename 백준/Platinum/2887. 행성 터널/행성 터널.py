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
        parent[b_root] = parent[a_root]
        return True
    else:
        return False

def cal_min_cost():
    answer = 0
    edges_count = 0
    for cost,a,b in edges:
        if union(a,b):
            answer += cost
            edges_count += 1
            if edges_count == N-1:
                return answer


N = int(input())
planets = []
edges = []
parent = [i for i in range(N)]
for i in range(N):
    x,y,z = map(int,input().split())
    planets.append((x,y,z,i))

planets.sort(key=lambda planet: planet[0])
for i in range(N-1):
    xa,ya,za,ia = planets[i]
    xb,yb,zb,ib = planets[i+1]
    edges.append((min(abs(xa-xb),abs(ya-yb),abs(za-zb)),ia,ib))

planets.sort(key=lambda planet: planet[1])
for i in range(N-1):
    xa,ya,za,ia = planets[i]
    xb,yb,zb,ib = planets[i+1]
    edges.append((min(abs(xa-xb),abs(ya-yb),abs(za-zb)),ia,ib))

planets.sort(key=lambda planet: planet[2])
for i in range(N-1):
    xa,ya,za,ia = planets[i]
    xb,yb,zb,ib = planets[i+1]
    edges.append((min(abs(xa-xb),abs(ya-yb),abs(za-zb)),ia,ib))

edges.sort()
print(cal_min_cost())

