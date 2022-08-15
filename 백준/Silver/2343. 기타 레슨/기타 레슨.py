import sys
input = sys.stdin.readline

N,M = map(int, input().split())
l = list(map(int,input().split()))

start, end = max(l), sum(l)    #최소크기(최대갯수), 최대크기(최소갯수)

while start<=end:
    mid = (start+end) // 2

    volume = 0
    disk = 1    #한개부터 시작
    for i in range(N):
        volume += l[i]
        if volume > mid:    #블루레이 크기를 넘어서면
            disk+=1    #블루레이 갯수 증가
            volume = l[i]    #크기 넘어선 강의부터 다시 누적
    if disk > M:    #갯수가 더 많으면
        start = mid + 1    #크기 증가
    elif disk <= M:    #갯수가 더 작거나 같으면
        answer = mid    
        end = mid - 1    #크기 감소
print(answer)
