import sys
from itertools import permutations

n = int(sys.stdin.readline())
result = []    #순열중에 조건을 만족하는 순열의 리스트들만 저장하는 2차원 리스트
l = []
l = sys.stdin.readline().split()

#0~9 숫자로 만들 수 있는 n+1순열
for i in permutations([0,1,2,3,4,5,6,7,8,9],n+1):
    flag = 1
    for j in range(n):
        if l[j] == '<':
            if i[j] < i[j+1]:    #만족할 경우 계속해서 실행
                continue
            else: flag = 0    #만족하지 않을경우 flag = 0, break
            break
        elif l[j] == '>':
            if i[j] > i[j+1]:
                continue
            else: flag = 0
            break
    if flag == 1:    #모두 만족하고 for문을 탈출했으면 result배열에 append
        result.append(i)

for i in range(len(result[-1])):    #가장 마지막에있는 순열리스트 = 가장 큰 값
    print(result[-1][i],end='')    #순열 안에있는 원소 하나하나를 출력
print()
for i in range(len(result[0])):    #가장 처음에있는 순열리스트 = 가장 작은 값
    print(result[0][i],end='')
