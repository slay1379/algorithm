import sys
input = sys.stdin.readline
from collections import deque
import heapq

def rotation(w,d):
    if d == 1:
        return w[-1:] + w[:-1]
    if d == -1:
        return w[1:] + w[:1]
    return w


wheels = [[]] + [list(map(int,input().strip())) for _ in range(4)]
K = int(input())
for _ in range(K):
    n,d = map(int,input().split())
    dir = [0]*5
    dir[n] = d
    for i in range(n+1,5):
        if wheels[i-1][2] != wheels[i][6]:
            dir[i] = -dir[i-1]
        else:
            break
    for i in range(n-1,0,-1):
        if wheels[i+1][6] != wheels[i][2]:
            dir[i] = -dir[i+1]
        else:
            break
    for i in range(1,5):
        wheels[i] = rotation(wheels[i],dir[i])

answer = 0
if wheels[1][0] == 1:
    answer += 1
if wheels[2][0] == 1:
    answer += 2
if wheels[3][0] == 1:
    answer += 4
if wheels[4][0] == 1:
    answer += 8
print(answer)