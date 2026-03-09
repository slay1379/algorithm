import sys
input = sys.stdin.readline
from collections import deque
import heapq

N,M = map(int,input().split())
not_listen = {input().strip() for _ in range(N)}
not_see = {input().strip() for _ in range(M)}

not_listen_and_see = not_listen & not_see
result = sorted(not_listen_and_see)

print(len(result))
for name in result:
    print(name)