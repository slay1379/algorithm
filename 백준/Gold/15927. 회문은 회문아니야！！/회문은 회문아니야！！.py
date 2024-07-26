import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def palindrome():
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def all_same():
    test = s[0]
    if len(s)%2 == 1:
        for i in range(len(s)//2+1):
            if test != s[i]:
                return False
    else:
        for i in range(len(s)//2):
            if test != s[i]:
                return False

    return True


s = list(map(str,input().strip()))
if palindrome():
    if all_same():
        print(-1)
    else:
        print(len(s)-1)
else:
    print(len(s))
