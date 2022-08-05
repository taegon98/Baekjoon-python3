import sys
from collections import deque

input = sys.stdin.readline

N,K = map(int,input().split())
dp = [-1 for _ in range(100001)]

def bfs(start):
    queue = deque()
    queue.append(start)
    dp[start] = 0

    while queue:
        x = queue.popleft()

        if x == K:
            print(dp[x])
            exit(0)

        if 0<=(x*2)<100001 and dp[x*2] == -1:
            dp[x*2] = dp[x]
            queue.append(x*2)

        for i in x-1,x+1:
            if 0<=i<100001 and dp[i] == -1:
                dp[i] = dp[x] + 1
                queue.append(i)
bfs(N)