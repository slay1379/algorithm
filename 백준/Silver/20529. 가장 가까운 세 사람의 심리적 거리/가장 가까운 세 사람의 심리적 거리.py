import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def comparison(a,b,c):
    count = 0
    for i in range(4):
        if a[i] != b[i]:
            count += 1
        if b[i] != c[i]:
            count += 1
        if c[i] != a[i]:
            count += 1

    return count


T = int(input())

for _ in range(T):
    N = int(input())
    students = list(map(str,input().split()))
    answer = 12

    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    if answer > comparison(students[i],students[j],students[k]):
                        answer = comparison(students[i],students[j],students[k])
        print(answer)