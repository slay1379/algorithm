import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def cantore(start,end,l):
    if l == 1:
        return
    for i in range(start+l//3,start+l//3*2):
        begin[i] = ' '
    cantore(start,l//3,l//3)
    cantore(start+l//3*2,end,l//3)



while True:
    try:
        N = int(input())
        begin = ['-'] * (3 ** N)
        cantore(0, 3 ** N - 1, 3 ** N)
        print(''.join(begin))
    except :
        break

