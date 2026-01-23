import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    oper = input().split()
    if oper[0] == 'push':
        q.append(oper[1])
    if oper[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    if oper[0] == 'size':
        print(len(q))
    if oper[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    if oper[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    if oper[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)