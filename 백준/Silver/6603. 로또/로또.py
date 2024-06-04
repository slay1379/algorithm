import sys
input = sys.stdin.readline
from itertools import combinations

while True:
    value = list(map(int,input().split()))
    if value[0] == 0:
        break
    seq = value[1:]
    combs = list(combinations(seq,6))
    for i in combs:
        print(' '.join(map(str,i)))
    print()