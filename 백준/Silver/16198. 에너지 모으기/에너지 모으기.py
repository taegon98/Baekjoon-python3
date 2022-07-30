import sys
N = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
result = 0    

def energy(tot):
    global result
    if len(l) <= 2:
        result = max(result, tot)    #max값 갱신
        return
    for i in range(1,len(l)-1):    #처음과 끝 인덱스를 제외하고 반복
        sum = l[i-1] * l[i+1]    #바로 이전 값 * 바로 이후 값
        temp = l.pop(i)    #재귀호출은 pop된 리스트로, for문은 원래의 리스트로
        energy(tot+sum)    
        l.insert(i,temp)    #다음 index에서 시작했을 때의 결과 -> 원래 리스트가 필요

energy(0)
print(result)