import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = list(map(int,input().split()))
dp = l[:]

for i in range(1, n):
    if dp[i] < dp[i-1] + l[i]:
        dp[i] = dp[i-1] + l[i]
print(max(dp))