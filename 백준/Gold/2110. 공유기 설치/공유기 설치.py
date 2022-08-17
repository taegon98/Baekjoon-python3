import sys
input = sys.stdin.readline

N, K = map(int,input().split())
l = list()
for _ in range(N):
    l.append(int(input().rstrip()))
l.sort()
answer = []
start, end = 1, l[-1]-l[0]
for i in range(N):
    while start <= end:
        mid = (start+end)//2

        cnt = 1
        tot = l[i]+mid
        for j in range(i+1, N):
            if l[j] >= tot:
                cnt += 1
                tot = l[j]+mid
        if cnt >= K:
            answer.append(mid)
            start = mid + 1
        else:
            end = mid - 1
if not answer:
    print(1)
else:
    print(max(answer))