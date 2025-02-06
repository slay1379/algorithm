import sys
input = sys.stdin.readline
from collections import deque

dp = [False]*10001

for i in range(1,10000):
    a = i
    while True:
        n = a
        while n > 0:
            a += n%10
            n //= 10
        if a > 10000 or dp[a] == True:
            break
        dp[a] = True

for i in range(1,10000):
    if dp[i] == False:
        print(i)
