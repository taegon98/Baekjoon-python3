import sys
input = sys.stdin.readline
N,K = map(int,input().split())
dp = [[1 for _ in range(200)] for _ in range(200)]
for i in range(200):
    dp[i][0] = i+1

for i in range(1,200):
    for j in range(1,200):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(dp[K-1][N-1] % 1000000000)