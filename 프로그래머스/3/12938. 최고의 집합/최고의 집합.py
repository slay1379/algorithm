import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq


def solution(n,s):
    if n>s:
        return [-1]
    
    quotient = s // n
    remainder = s % n
    
    result = [quotient] * n
    for i in range(remainder):
        result[i] += 1
    
    return sorted(result)
