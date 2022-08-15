import sys
input = sys.stdin.readline

N,M = map(int, input().split())
l = list(map(int,input().split()))

start, end = max(l), sum(l)

while start<=end:
    mid = (start+end) // 2

    volume = 0
    disk = 1
    for i in range(N):
        volume += l[i]
        if volume > mid:
            disk+=1
            volume = l[i]
    if disk > M:
        start = mid + 1
    elif disk <= M:
        answer = mid
        end = mid - 1
print(answer)