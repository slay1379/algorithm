import sys

N = int(sys.stdin.readline())

dp=[[0 for _ in range(10)]for _ in range(N+1)]

for i in range(10):
    dp[1][i]=1

for i in range(2,N+1):
    dp[i][0]=sum(dp[i-1])
    for j in range(1,10):
        dp[i][j]=(dp[i][j-1]-dp[i-1][j-1])

print(sum(dp[N])%10007)