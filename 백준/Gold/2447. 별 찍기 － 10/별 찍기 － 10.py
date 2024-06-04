import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq

def star(N):
    if N==3:
        return ["***","* *","***"]
    else:
        stars = star(N//3)
        result = []
        for i in range(3):
            for s in stars:
                if i == 1:
                    result.append(s + " "*(N//3) + s)
                else:
                    result.append(s*3)
        return result

N = int(input())
result = star(N)
for row in result:
    print(''.join(row))