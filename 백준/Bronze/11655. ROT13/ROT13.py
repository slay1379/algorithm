import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict
import heapq
from itertools import combinations

S = input()
result = ''
for c in S:
    if c.isupper():
        result += chr((ord(c) - ord('A') + 13)%26 + ord('A'))
    elif c.islower():
        result += chr((ord(c) - ord('a') + 13)%26 + ord('a'))
    else:
        result += c

print(result)