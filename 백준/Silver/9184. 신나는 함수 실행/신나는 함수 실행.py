import sys
input = sys.stdin.readline
dp = [[[1]*51 for _ in range(51)]for _ in range(51)]
for a in range(1,51):
    for b in range(1,51):
        for c in range(1,51):
            if a > 20 or b > 20 or c > 20:
                dp[a][b][c] = 2**20
            elif a<=b or a<=c:
                dp[a][b][c] = 2**a
            else:
                dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]


while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    if a<0 or b<0 or c<0:
        print(f'w({a}, {b}, {c}) = 1')
    else:
        print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')

