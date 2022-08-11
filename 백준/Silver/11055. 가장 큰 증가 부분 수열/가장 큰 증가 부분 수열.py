import sys
input = sys.stdin.readline

N = int(input().rstrip())
l = list(map(int, input().split()))
dp = l[:]

for i in range(1, N):
    for j in range(0,i):
        if l[i] > l[j] and dp[i] < dp[j]+l[i]:
            dp[i] = dp[j]+l[i]
print(max(dp))