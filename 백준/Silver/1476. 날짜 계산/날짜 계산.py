import sys

e,s,m = map(int,sys.stdin.readline().split())
E=1
S=1
M=1
cnt=1
while True:
    if E==e and S==s and M==m:
        print(cnt)
        break
    E = (E+1)%16
    if E == 0:
        E += 1
    S = (S + 1) % 29
    if S == 0:
        S += 1
    M = (M + 1) % 20
    if M == 0:
        M += 1
    cnt += 1
