import sys

input = sys.stdin.readline

n = int(input())

a, b, c = map(int, input().split())
max_dp = [a, b, c]
min_dp = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    temp_max_dp_0 = a + max(max_dp[0], max_dp[1])
    temp_max_dp_1 = b + max(max_dp[0], max_dp[1], max_dp[2])
    temp_max_dp_2 = c + max(max_dp[1], max_dp[2])

    temp_min_dp_0 = a + min(min_dp[0], min_dp[1])
    temp_min_dp_1 = b + min(min_dp[0], min_dp[1], min_dp[2])
    temp_min_dp_2 = c + min(min_dp[1], min_dp[2])

    max_dp = [temp_max_dp_0, temp_max_dp_1, temp_max_dp_2]
    min_dp = [temp_min_dp_0, temp_min_dp_1, temp_min_dp_2]

print(max(max_dp), min(min_dp))