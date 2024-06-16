import copy
import sys
input = sys.stdin.readline
from collections import deque
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def check(a,b):
    a, b = str(a),str(b)
    cnt = sum((1 for x,y in zip(a,b) if x!=y))
    return cnt == 1

def change(a,b):
    visit = set()
    visit.add(a)
    q = deque()
    q.append((a,0))
    while q:
        now, count = q.popleft()
        if now == b:
            return count
        for i in primes:
            if i not in visit and check(now,i):
                q.append((i,count+1))
                visit.add(i)
    return -1


primes = []
for i in range(1000,9999):
    if is_prime(i):
        primes.append(i)



T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    if change(a,b) == -1:
        print('Impossible')
    else:
        print(change(a,b))
