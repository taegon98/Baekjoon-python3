import sys
input = sys.stdin.readline

N, K = map(int,input().split())
l = list()
for _ in range(N):
    l.append(int(input().rstrip()))
l.sort()
answer = []
start, end = 1, l[-1]-l[0]    #최소거리:1, 최대거리
for i in range(N):    #모든 정점 검사
    while start <= end:
        mid = (start+end)//2
        cnt = 1
        tot = l[i]+mid    #설치 가능한 거리 = 현재 + mid값
        for j in range(i+1, N):
            if l[j] >= tot:    #설치 가능한 거리이면
                cnt += 1    #공유기 횟수 증감
                tot = l[j]+mid    #설치 가능한 거리 = 현재 + mid값
        if cnt >= K:    #설치해야하는 공유기 갯수보다 같거나 많으면
            answer.append(mid)    #정답에 일단 저장
            start = mid + 1    #최대거리를 구하기 위해
        else:    #설치해야하는 공유기 갯수보다 작으면
            end = mid - 1    #거리를 줄인다
            
if not answer:    #answer에 없으면 -> 최소거리인 1
    print(1)
else:    #answer 리스트중에 최대거리 출력
    print(max(answer))
