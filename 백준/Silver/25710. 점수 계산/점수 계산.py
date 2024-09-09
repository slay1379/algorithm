import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations
from collections import deque
from collections import defaultdict
import heapq

def cal(a):
    answer = 0
    while a > 0:
        answer += a%10
        a = a // 10
    return answer


N = int(input())
a = list(map(int,input().split()))

a_count = [0]*1000

for i in range(N-1,-1,-1):
    if a_count[a[i]] > 2:
        del a[i]
    else:
        a_count[a[i]] += 1

answer = 0

for i in range(len(a)):
    for j in range(i+1,len(a)):
        mul = a[i]*a[j]
        sum_digits = cal(mul)
        if sum_digits > answer:
            answer = sum_digits

print(answer)