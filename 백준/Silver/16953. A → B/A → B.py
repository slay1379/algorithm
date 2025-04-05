import sys
input = sys.stdin.readline
from collections import Counter

A,B = map(int,input().split())
cnt = 0

while True:
    if B < A:
        print(-1)
        exit()
    if B % 2 != 0:
        if B % 10 != 1:
            print(-1)
            exit()
    cnt += 1
    if B % 10 == 1:
        B //= 10
    else:
        B //= 2
    if B == A:
        cnt += 1
        break

print(cnt)