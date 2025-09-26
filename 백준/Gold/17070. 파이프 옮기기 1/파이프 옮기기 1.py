import sys

input = sys.stdin.readline

N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]

dp = [[[-1]*N for _ in range(N)] for _ in range(3)]

def dfs(x,y,shape):
    if x == N-1 and y == N-1:
        return 1

    if dp[shape][x][y] != -1:
        return dp[shape][x][y]

    ways = 0

    if shape == 0 or shape == 2:
        if y+1<N and house[x][y+1] == 0:
            ways += dfs(x,y+1,0)

    if shape == 1 or shape == 2:
        if x+1<N and house[x+1][y] == 0:
            ways += dfs(x+1,y,1)

    if x+1<N and y+1<N:
        if house[x+1][y] == 0 and house[x][y+1] == 0 and house[x+1][y+1] == 0:
            ways += dfs(x+1,y+1,2)

    dp[shape][x][y] = ways
    return ways

if house[N-1][N-1] == 1:
    print(0)
else:
    print(dfs(0,1,0))
    