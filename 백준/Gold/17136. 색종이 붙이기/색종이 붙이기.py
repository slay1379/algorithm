import sys
import heapq
input = sys.stdin.readline
import bisect

paper = [list(map(int,input().split())) for _ in range(10)]
counts = [5]*6
answer = float('inf')

def can_place(x,y,size):
    if x+size > 10 or y+size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if paper[x+i][y+j] == 0:
                return False
    return True

def place(x,y,size,value):
    for i in range(size):
        for j in range(size):
            paper[x+i][y+j] = value

def solve(x,y,used):
    global answer

    if used >= answer:
        return

    while x< 10:
        if paper[x][y] == 1:
            break
        y += 1
        if y == 10:
            x += 1
            y = 0

    if x == 10:
        answer = min(answer,used)
        return

    for size in range(5,0,-1):
        if counts[size] > 0 and can_place(x,y,size):
            place(x,y,size,0)
            counts[size] -= 1
            solve(x,y,used+1)
            place(x,y,size,1)
            counts[size] += 1

solve(0,0,0)
print(answer if answer != float('inf') else -1)