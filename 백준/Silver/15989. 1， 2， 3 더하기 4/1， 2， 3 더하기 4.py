import sys
input = sys.stdin.readline

dp = [_ for _ in range(10001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3

index = 1
for i in range(4, 10001):
    if i % 3 == 0:
        dp[i] = dp[index+1]+dp[index+2]-dp[index]+1
    else:
        dp[i] = dp[index+1]+dp[index+2]-dp[index]
    index+=1

T = int(input().rstrip())
for i in range(T):
    N = int(input().rstrip())
    print(dp[N])