import sys
input = sys.stdin.readline

N,M = map(int, input().split())
l = list(map(int,input().split()))

start, end = 0, max(l)-1

while start<=end:
    mid = (start+end) // 2

    tree = 0
    for i in range(N):
        if l[i] - mid > 0:
            tree += l[i] - mid
    if tree >= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)