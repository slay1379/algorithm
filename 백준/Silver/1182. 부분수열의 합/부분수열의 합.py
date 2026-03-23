N,S = map(int,input().split())
seq = list(map(int,input().split()))
answer = 0

def dfs(idx, total, cnt):
    global answer
    if idx == N:
        if total == S and cnt != 0:
            answer += 1
        return

    dfs(idx+1,total+seq[idx],cnt+1)
    dfs(idx+1,total,cnt)

dfs(0,0,0)
print(answer)