import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stat = [list(map(int,input().split())) for _ in range(N)]
results = []
visit = [False]*N
first_team = []

def cal():
    first_team_stat = 0
    second_team_stat = 0
    second_team = []
    for i in range(N):
        if i not in first_team:
            second_team.append(i)

    for i in range(len(first_team)-1):
        for j in range(i+1,len(first_team)):
            first_team_stat += stat[first_team[i]][first_team[j]]
            first_team_stat += stat[first_team[j]][first_team[i]]

    for i in range(len(second_team)-1):
        for j in range(i+1,len(second_team)):
            second_team_stat += stat[second_team[i]][second_team[j]]
            second_team_stat += stat[second_team[j]][second_team[i]]

    return abs(first_team_stat - second_team_stat)

def solve(num,cnt):
    if cnt == N//2:
        results.append(cal())
        return

    for i in range(num+1,N):
        if not visit[i]:
            visit[i] = True
            first_team.append(i)
            solve(i,cnt+1)
            first_team.pop()
            visit[i] = False


for i in range(N):
    visit[i] = True
    first_team.append(i)
    solve(i,1)
    first_team.pop()
    visit[i] = False

print(min(results))