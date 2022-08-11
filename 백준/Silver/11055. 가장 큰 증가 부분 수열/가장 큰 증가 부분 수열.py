import sys
input = sys.stdin.readline

N = int(input().rstrip())
l = list(map(int, input().split()))
dp = l[:]    #dp table

for i in range(1, N):    #인덱스 1 ~ 마지막 인덱스까지
    for j in range(0,i):    #처음부터 i인덱스 전까지
        if l[i] > l[j] and dp[i] < dp[j]+l[i]:
            dp[i] = dp[j]+l[i]
print(max(dp))
