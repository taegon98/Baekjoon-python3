import sys
input = sys.stdin.readline

K,N = map(int,input().split())
l = []
for i in range(K):
    l.append(int(input().rstrip()))

start, end = 1, max(l)    #최대로 가져갈 때, 최소로 가져갈 때

while start<=end:
    mid = (start+end) // 2

    LAN = 0
    for i in range(K):    #mid크기로 몇개로 나눌 수 있는지 저장
        LAN += (l[i] // mid)
    if LAN < N:    #원하는 갯수보다 적으면
        end = mid-1    #갯수 늘려야함 -> end감소(최대쪽으로)
    elif LAN >= N:    #원하는 갯수보다 많거나 같으면
        answer = mid
        start = mid + 1    #갯수 줄여야함 -> start증가(최소쪽으로)
print(answer)
