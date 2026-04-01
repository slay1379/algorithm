import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations
from collections import Counter

while True:
    try:
        n = int(input())
    except:
        break

    remainder = 0
    count = 0
    while True:
        remainder = (remainder * 10 + 1)%n
        count += 1
        if remainder == 0:
            print(count)
            break