import sys
input = sys.stdin.readline
from collections import deque

R,C = map(int,input().split())
n = int(input())
store = []
for i in range(n+1):
    direction, num = map(int,input().split())
    if direction == 1:
        dis = num
    if direction == 2:
        dis = R+C+R-num
    if direction == 3:
        dis = R+C+R+C-num
    if direction == 4:
        dis = R+num
    if i == n:
        now_x = dis
    else:
        store.append(dis)

answer = 0
for x in store:
    dis = abs(now_x-x)
    if dis < R+R+C+C-dis:
        answer += dis
    else:
        answer += R+R+C+C-dis

print(answer)

