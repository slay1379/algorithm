import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def cal_distance(X,Y):
    return (X**2+Y**2)**(1/2)

X,Y,D,T = map(int,input().split())
dis = cal_distance(X,Y)
if dis >= D:
    ans = min(T*(dis//D)+dis%D, T*(dis//D+1), dis)
else:
    ans = min(T+(D-dis),2*T,dis)
print(ans)