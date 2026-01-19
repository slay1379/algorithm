import sys
input = sys.stdin.readline

def solve(n):
    if int(n**0.5)**2 == n:
        return 1

    for i in range(1, int(n**0.5) + 1):
        if int((n- i*i)**0.5)**2 == (n - i*i):
            return 2

    for i in range(1, int(n**0.5) + 1):
        for j in range(1, int((n - i*i)**0.5) + 1):
            if int((n - i*i - j*j)**0.5)**2 == (n - i*i -j*j):
                return 3

    else:
        return 4

n = int(input())
print(solve(n))