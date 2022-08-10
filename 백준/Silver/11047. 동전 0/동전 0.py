N,K = map(int,input().split())
coin = []
count = 0

for i in range(N):
    coin.append(int(input()))

coin.reverse()    #가장 큰 지폐부터이용 -> 동전 갯수 최소화

for i in coin:
    if K // i > 0:    #나누어지면
        count+=(K //i)    #나누어진 몫을 증감
        K = K % i    #나누어진 나머지로 K값 갱신
    if K == 0:    #다 나누어졌으면
        print(count)
        exit(0)
