N, K = map(int,input().split())
list = ['B' for _ in range(N)]    #리스트 모두 B로 초기화
flag = 0
for i in range(N):    #경우의 수 모두 검사
    list[i] = 'A'
    count = 0
    for j in range(0,len(list)-1):    #0부터 마지막인덱스 전까지 -> 마지막에 'A'가 위치해도 count = 0
        if list[j] == 'A':    #인덱스에 'A'가 위치해있는 경우만
            for k in range(j+1, len(list)):    #'B'의 갯수만 카운트
                if list[k] == 'B':
                    count+=1
    if K == count:    #같으면
        flag = 1
        break
    elif K < count:    #count가 더 크다면 B로 돌려놓고 다음 분기문 실행
        list[i] = 'B'
if flag == 1: print("".join(list))    #일치해서 탈출한 경우
else: print(-1)    #만들어질 수 없는 경우 -1출력
