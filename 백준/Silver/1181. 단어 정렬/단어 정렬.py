import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq

N = int(input())
words = set()
for i in range(N):
    words.add(input().strip())

words = sorted(words,key=lambda x:(len(x),x))

for i in words:
    print(i)