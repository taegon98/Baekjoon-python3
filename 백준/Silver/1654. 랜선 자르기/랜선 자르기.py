import sys
input = sys.stdin.readline

K,N = map(int,input().split())
l = []
for i in range(K):
    l.append(int(input().rstrip()))

start, end = 1, max(l)

while start<=end:
    mid = (start+end) // 2

    LAN = 0
    for i in range(K):
        LAN += (l[i] // mid)
    if LAN < N:
        end = mid-1
    elif LAN >= N:
        answer = mid
        start = mid + 1
print(answer)