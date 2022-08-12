import sys
input = sys.stdin.readline

N = int(input().rstrip())
l = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(1,N):
    for j in range(0, i):
        if l[i] > l[j]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
print(max(dp))