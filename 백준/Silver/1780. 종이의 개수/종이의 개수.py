import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
from collections import deque
from collections import defaultdict
import heapq

def cut(x,y,N):
    global minus_one,zero,one
    num = paper[x][y]

    for i in range(x,x+N):
        for j in range(y,y+N):
            if paper[i][j] != num:
                cut(x,y,N//3)
                cut(x,y+N//3,N//3)
                cut(x,y+2*(N//3),N//3)
                cut(x+N//3,y,N//3)
                cut(x+N//3,y+N//3,N//3)
                cut(x+N//3,y+2*(N//3),N//3)
                cut(x+2*(N//3),y,N//3)
                cut(x+2*(N//3),y+N//3,N//3)
                cut(x+2*(N//3),y+2*(N//3),N//3)
                return
    if num == -1:
        minus_one += 1
    elif num == 0:
        zero += 1
    else:
        one += 1


N = int(input())
paper = [list(map(int,input().split()))for _ in range(N)]
minus_one, zero, one = 0,0,0

cut(0,0,N)
print(minus_one)
print(zero)
print(one)