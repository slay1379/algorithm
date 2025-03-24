import sys
input = sys.stdin.readline

T = int(input())
dp0 = [0]*41
dp1 = [0]*41
dp0[0] = 1
dp1[1] = 1
for i in range(2,41):
    dp0[i] = dp0[i-2] + dp0[i-1]
    dp1[i] = dp1[i-2] + dp1[i-1]

for _ in range(T):
    N = int(input())
    print(dp0[N], dp1[N])

