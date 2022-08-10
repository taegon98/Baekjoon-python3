N,K = map(int,input().split())
coin = []
count = 0
for i in range(N):
    coin.append(int(input()))
coin.reverse()

for i in coin:
    if K // i > 0:
        count+=(K //i)
        K = K % i
    if K == 0:
        print(count)
        exit(0)