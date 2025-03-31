import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
for _ in range(n):
    t = int(input())
    clothes = {}
    for _ in range(t):
        name, type = input().split()
        if type not in clothes:
            clothes[type] = []
        clothes[type].append(name)
    count = 1
    for type in clothes:
        count *= (len(clothes[type])+1)
    print(count-1)