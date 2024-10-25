def solution(a):
    answer = 2
    dp = [1000000000]*(len(a))
    dp[0] = a[0]
    dp[len(a)-1] = a[len(a)-1]
    for i in range(len(a)-2,1,-1):
        if a[i] > dp[i+1]:
            dp[i] = dp[i+1]
        if a[i] < dp[i+1]:
            dp[i] = a[i]
    
    for i in range(1,len(a)-1):
        if a[i] < dp[i-1] or dp[i] < dp[i+1]:
            answer += 1
        if a[i] < dp[i-1]:
            dp[i] = a[i]
        else:
            dp[i] = dp[i-1]
    
    return answer