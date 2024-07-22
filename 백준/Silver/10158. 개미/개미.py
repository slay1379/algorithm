import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

w,h = map(int,input().split())
p,q = map(int,input().split())
t = int(input())

horizon_share = (p+t)//w
horizon_remain = (p+t)%w
perpen_share = (q+t)//h
perpen_remain = (q+t)%h

if horizon_share % 2 == 0:
    horizon = horizon_remain
else:
    horizon = w-horizon_remain
if perpen_share % 2 == 0:
    perpen = perpen_remain
else:
    perpen = h-perpen_remain

print(horizon, perpen)