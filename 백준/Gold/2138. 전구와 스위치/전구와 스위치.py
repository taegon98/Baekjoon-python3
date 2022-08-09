import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int,input().rstrip()))
B = list(map(int,input().rstrip()))

def bulb(C,D):
    count = 0
    for k in range(1,len(C)):    #1번 인덱스 ~ 마지막 인덱스
        if C[k-1] != D[k-1]:    #왼쪽 전구의 값이 같지 않다면
            count+=1
            if k == len(C)-1:    #마지막 전구인 경우 index범위 벗어나는 예외처리
                for l in k-1,k:
                    if C[l] == 0: C[l] = 1
                    else: C[l] = 0
            else:    #전구 값 모두 switch
                for l in k-1,k,k+1:
                    if C[l] == 0: C[l] = 1
                    else: C[l] = 0
    if C == D:    #for문을 돌았을 때 같다면
        return count    #바꾼 횟수 return
    else: return 1e9    #같지 않다면 가장 큰수 return -> min 이용!

temp = A[:]    #사본을 temp에 저장
result = bulb(temp,B)    #첫번째 전구를 바꾸지 않은 경우(A(사본), B)
for i in 0, 1:    #첫번째 전구를 바꾼 경우
    if A[i] == 0: A[i] = 1
    else: A[i] = 0
result = min(result, bulb(A,B)+1)    #두 경우 중 최소값 저장
print(result if result != 1e9 else -1)    #if not A==B, -1출력
