import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

N = int(input())
result = []
for _ in range(N):
    word = input().strip()
    now = ''
    for ch in word:
        if ch.isdigit():
            now += ch
        else:
            if now != '':
                result.append(int(now))
                now = ''
    if now != '':
        result.append(int(now))

result.sort()
for num in result:
    print(num)